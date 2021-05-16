import logging
from functools import wraps
from typing import Awaitable, Callable, Optional

from blacksheep.messages import Request, Response
from blacksheep.server import Application
from blacksheep.server.routing import RouteMatch
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace import config_integration
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.span import SpanKind
from opencensus.trace.tracer import Tracer
from service.settings import Settings

# configures span id
config_integration.trace_integrations(["logging"])


def configure_logging(app: Application, settings: Settings) -> None:
    logger = logging.getLogger("blacksheep.server")

    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # For telemetry sent with the Azure Monitor logs exporter, logs appear under traces.
    # Exceptions appear under exceptions.
    # So, `logger.info` are found in traces logs, `logger.exception` under exceptions
    logger.addHandler(
        AzureLogHandler(
            connection_string=f"InstrumentationKey={settings.monitoring_key}"
        )
    )

    # For telemetry sent with the Azure Monitor logs exporter, logs appear under traces.
    # Exceptions appear under exceptions.
    tracer = Tracer(
        exporter=AzureExporter(
            connection_string=f"InstrumentationKey={settings.monitoring_key}"
        ),
        sampler=AlwaysOnSampler(),
    )

    # wrap app.handle to log every web request, even those that fail due to exceptions
    # and are handled by BaseApplication class
    def wrap_handle(
        fn: Callable[[Request], Awaitable[Response]]
    ) -> Callable[[Request], Awaitable[Response]]:
        @wraps(fn)
        async def handle(request: Request) -> Response:
            with tracer.span(name="request") as span:
                span.span_kind = SpanKind.SERVER
                request_path = request.url.path.decode("utf8")
                span.add_attribute("http.method", request.method)
                span.add_attribute("http.path", request_path)
                span.add_attribute("http.url", request.url.value.decode())
                response = await fn(request)
                span.add_attribute("http.route", request.route)  # type: ignore
                span.add_attribute("http.status_code", response.status)
                return response

        return handle

    app.handle = wrap_handle(app.handle)  # type: ignore

    def wrap_get_route_match(
        fn: Callable[[Request], Optional[RouteMatch]]
    ) -> Callable[[Request], Optional[RouteMatch]]:
        @wraps(fn)
        def get_route_match(request: Request) -> Optional[RouteMatch]:
            match = fn(request)
            if match:
                request.route = match.pattern.decode()  # type: ignore
            else:
                request.route = "Not Found"  # type: ignore

            return match

        return get_route_match

    app.get_route_match = wrap_get_route_match(app.get_route_match)  # type: ignore
