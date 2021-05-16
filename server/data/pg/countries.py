from typing import Any, List

from asyncpg import Connection, Pool
from domain.countries import CountriesDataProvider, Country
from essentials.exceptions import ObjectNotFound


def _record_to_country(record: Any) -> Country:
    if record is None:
        raise ObjectNotFound

    return Country(
        id=record["id"],
        name=record["name"],
    )


class PostgresCountriesDataProvider(CountriesDataProvider):
    def __init__(self, pool: Pool) -> None:
        super().__init__()
        self.pool = pool

    async def get_countries(self) -> List[Country]:
        con: Connection
        albums: List[Country] = []

        async with self.pool.acquire() as con:
            records = await con.fetch("SELECT * FROM country")

            for record in records:
                albums.append(_record_to_country(record))

        return albums
