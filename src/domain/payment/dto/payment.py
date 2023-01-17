from src.domain.common.dto.base import DTO

from ..constants import CURRENCY, SUBSCRIPTION_MONTH_COST
from ..models import Periodicity


class CreateSubscriptionPaymentUrl(DTO):
    amount: int = SUBSCRIPTION_MONTH_COST
    currency: str = CURRENCY
    periodicity: Periodicity
    user_id: int
    server_url: str
    result_url: str
