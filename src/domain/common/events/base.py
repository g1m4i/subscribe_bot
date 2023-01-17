from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict, Union

from src.domain.common.events.event import Event
from src.domain.common.events.middleware import BaseMiddleware

NextMiddlewareType = Callable[[Event, Dict[str, Any]], Awaitable[Any]]
MiddlewareType = Union[
    BaseMiddleware,
    Callable[[NextMiddlewareType, Event, Dict[str, Any]], Awaitable[Any]],
]
