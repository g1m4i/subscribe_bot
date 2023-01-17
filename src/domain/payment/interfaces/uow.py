from typing import Protocol

from .persistence import IPaymentRepo


class IPaymentUoW(Protocol):
    payment_repo: IPaymentRepo
