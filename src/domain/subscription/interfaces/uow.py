from typing import Protocol
from .persistence import ISubscriptionRepo


class ISubscribeUoW(Protocol):
    subscribe_repo: ISubscriptionRepo
