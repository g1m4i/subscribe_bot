from .. import dto
from ..interfaces import IRenewalTypeUoW


class RecordTypeService:
    def __init__(self, uow: IRenewalTypeUoW) -> None:
        self.uow = uow

    async def get_record_type(self, name: str) -> dto.RenewalTypeDTO:
        return await self.uow.renewal_type_repo.type_by_name(name)
