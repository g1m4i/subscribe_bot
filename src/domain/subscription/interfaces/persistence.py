from typing import Protocol

from .. import dto


class ISubscriptionRepo(Protocol):
    def subscribe_user_for_month(self, user: dto.SubscribeUser) -> None:
        pass
