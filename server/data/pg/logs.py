from contextlib import contextmanager
from functools import wraps

from asyncpg.connection import Connection
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.span import SpanKind
from opencensus.trace.tracer import Tracer


@contextmanager
def con_context(handler, query, query_args):
    tracer = Tracer(
        exporter=AzureExporter(),
        sampler=AlwaysOnSampler(),
    )

    with tracer.span(name=query) as span:
        span.span_kind = SpanKind.CLIENT
        span.add_attribute("component", "PostgreSQL")
        span.add_attribute("QUERY", query)

        for i, value in enumerate(query_args):
            span.add_attribute(f"@p{i}", str(value))

        try:
            yield
        except Exception as ex:
            span.add_attribute("ERROR", str(ex))
            span.add_attribute("http.status_code", 500)
            raise


def wrap(coro):
    @wraps(coro)
    async def wrapped(self, query, *args, **kwargs):
        with con_context(self, query, args):
            return await coro(self, query, *args, **kwargs)

    return wrapped


def wrap_executemany(coro):
    @wraps(coro)
    async def wrapped(self, query, args, *_args, **kwargs):
        with con_context(self, query, args):
            return await coro(self, query, args, *_args, **kwargs)

    return wrapped


def tracing_connection(cls):
    cls.fetch = wrap(cls.fetch)
    cls.fetchval = wrap(cls.fetchval)
    cls.fetchrow = wrap(cls.fetchrow)
    cls.execute = wrap(cls.execute)
    cls.executemany = wrap_executemany(cls.executemany)
    return cls


@tracing_connection
class TracingConnection(Connection):
    pass
