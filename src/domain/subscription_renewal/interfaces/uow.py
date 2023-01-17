from typing import Protocol

from .persistence import ISubscriptionRenewalRepo


class ISubscriptionRenewalUoW(Protocol):
    subscription_renewal_repo: ISubscriptionRenewalRepo
