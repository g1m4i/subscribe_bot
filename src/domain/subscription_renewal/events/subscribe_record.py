from src.domain.common.events.event import Event

from .. import dto


class SubscriptionRenewalCreated(Event):
    def __init__(self, renewal: dto.SubscriptionRenewalDTO) -> None:
        self.renewal = renewal
