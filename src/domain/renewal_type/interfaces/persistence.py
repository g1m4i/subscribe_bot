from typing import Protocol

from .. import dto


class IRenewalTypeRepo(Protocol):
    async def type_by_name(self, name: str) -> dto.RenewalTypeDTO:
        ...
