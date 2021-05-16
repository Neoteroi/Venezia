import asyncpg
from core.events import ServicesRegistrationContext
from domain.countries import CountriesDataProvider
from rodi import Container
from service.settings import Settings

from .countries import PostgresCountriesDataProvider
from .logs import TracingConnection


def register_postgres_services(
    container: Container, context: ServicesRegistrationContext, settings: Settings
) -> None:
    pool = None

    async def register_pool():
        nonlocal pool

        pool = await asyncpg.create_pool(
            database=settings.postgres_db,
            user=settings.postgres_user,
            password=settings.postgres_password,
            host=settings.postgres_host,
            connection_class=TracingConnection,
            command_timeout=60,
        )
        container.add_instance(pool)

    async def release_pool():
        nonlocal pool

        if pool is not None:
            await pool.close()

    context.initialize += register_pool
    context.dispose += release_pool

    container.add_singleton(CountriesDataProvider, PostgresCountriesDataProvider)
