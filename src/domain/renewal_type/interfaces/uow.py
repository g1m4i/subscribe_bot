from typing import Protocol

from .persistence import IRenewalTypeRepo


class IRenewalTypeUoW(Protocol):
    renewal_type_repo: IRenewalTypeRepo
