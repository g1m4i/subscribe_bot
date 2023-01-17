from src.domain.common.dto.base import DTO

from ..models import TypeName


class RenewalTypeDTO(DTO):
    id: int
    name: TypeName
