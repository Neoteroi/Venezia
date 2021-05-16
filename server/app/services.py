"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see:
    https://www.neoteroi.dev/blacksheep/dependency-injection/
"""
import os
from typing import Tuple

from core.events import ServicesRegistrationContext
from data.pg.services import register_postgres_services
from roconfiguration import Configuration
from rodi import Container
from service.handlers import register_handlers
from service.settings import Settings


def configure_services(
    configuration: Configuration,
) -> Tuple[Container, ServicesRegistrationContext, Configuration, Settings]:
    container = Container()

    context = ServicesRegistrationContext()

    container.add_instance(configuration)

    settings = Settings.from_configuration(configuration)

    # set an env variable that is used internally by
    # opencensus.ext.azure.trace_exporter.AzureExporter
    os.environ[
        "APPLICATIONINSIGHTS_CONNECTION_STRING"
    ] = f"InstrumentationKey={settings.monitoring_key}"

    container.add_instance(settings)

    register_handlers(container)

    register_postgres_services(container, context, settings)

    return container, context, configuration, settings
