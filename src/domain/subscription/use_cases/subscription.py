from ..interfaces import ISubscribeUoW

from .. import dto


class SubscriptionService:
    def __init__(self, uow: ISubscribeUoW) -> None:
        self.uow = uow

    def subscribe_for_month(self, user: dto.SubscribeUser) -> None:
        return self.uow.subscribe_repo.subscribe_user_for_month(user)
