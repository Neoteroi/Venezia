from dataclasses import dataclass

from roconfiguration import Configuration


@dataclass
class Settings:

    postgres_db: str

    postgres_user: str

    postgres_password: str

    postgres_host: str

    monitoring_key: str

    @classmethod
    def from_configuration(cls, configuration: Configuration) -> "Settings":
        return cls(
            postgres_db=configuration.postgres_db,
            postgres_user=configuration.postgres_user,
            postgres_password=configuration.postgres_password,
            postgres_host=configuration.postgres_host,
            monitoring_key=configuration.monitoring_key,
        )
