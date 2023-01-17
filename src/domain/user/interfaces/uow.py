from typing import Protocol

from .persistence import IUserRepo


class IUserUoW(Protocol):
    user_repo: IUserRepo
