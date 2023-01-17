from enum import Enum


class TypeName(str, Enum):
    free_trial = "free_trial"
    payment = "payment"
    referral = "referral"
