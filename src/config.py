from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv
from pytz import BaseTzInfo, timezone


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class DB:
    host: str
    port: int
    name: str
    user: str
    password: str


@dataclass
class Payment:
    public_key: str
    private_key: str


@dataclass
class Config:
    tg_bot: TgBot
    debug: bool
    timezone: BaseTzInfo
    db: DB
    payment: Payment


def load_config(env_path: str = ".env") -> Config:
    load_dotenv(env_path)

    return Config(
        timezone=timezone(getenv("TIMEZONE", "")),
        debug=(getenv("DEBUG", "False") == "True"),
        tg_bot=TgBot(
            token=getenv("BOT_TOKEN", ""),
            admin_ids=[
                int(admin_id)
                for admin_id in getenv("ADMIN_IDS", "").split(",")
            ],
        ),
        db=DB(
            host=getenv("DB_HOST", ""),
            port=int(getenv("DB_PORT", "")),
            name=getenv("DB_NAME", ""),
            user=getenv("DB_USER", ""),
            password=getenv("DB_PASSWORD", ""),
        ),
        payment=Payment(
            public_key=getenv("LIQPAY_PUBLIC_KEY", ""),
            private_key=getenv("LIQPAY_PRIVATE_KEY", ""),
        ),
    )
