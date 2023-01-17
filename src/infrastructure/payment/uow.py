from typing import Type
from src.domain.payment.interfaces import IPaymentUoW, IPaymentRepo


class PaymentUoW(IPaymentUoW):
    payment_repo: IPaymentRepo

    def __init__(
        self,
        public_key: str,
        private_key: str,
        payment_repo: Type[IPaymentRepo],
    ) -> None:
        self.payment_repo = payment_repo(public_key, private_key)
