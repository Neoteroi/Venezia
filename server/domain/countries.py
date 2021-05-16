from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Country:
    id: str
    name: str


class CountriesDataProvider(ABC):
    @abstractmethod
    async def get_countries(self) -> List[Country]:
        ...
