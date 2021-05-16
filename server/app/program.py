from blacksheep.server import Application
from core.events import ServicesRegistrationContext
from roconfiguration import Configuration
from rodi import Container
from service.settings import Settings

from . import controllers  # NoQA
from .di import dependency_injection_middleware
from .docs import docs
from .errors import configure_error_handlers
from .logs import configure_logging


async def before_start(application: Application) -> None:
    application.services.add_instance(application)
    application.services.add_alias("app", Application)


def configure_application(
    services: Container,
    context: ServicesRegistrationContext,
    configuration: Configuration,
    settings: Settings,
) -> Application:
    app = Application(
        services=services,
        show_error_details=configuration.show_error_details,
        debug=configuration.debug,
    )

    app.on_start += before_start

    app.on_start += context.initialize
    app.on_stop += context.dispose

    app.middlewares.append(dependency_injection_middleware)

    configure_error_handlers(app)
    configure_logging(app, settings)

    docs.bind_app(app)
    return app
