from typing import List, Type

from src.domain.common.events.event import Event
from src.domain.common.events.observer import Handler, Observer


class EventDispatcher:
    def __init__(self, **kwargs):
        self.domain_events = Observer()
        self.notifications = Observer()
        self.data = kwargs

    async def publish_events(self, events: List[Event]) -> None:
        await self.domain_events.notify(events, data=self.data.copy())

    async def publish_event(self, event: Event) -> None:
        await self.domain_events.notify([event], data=self.data.copy())

    async def publish_notifications(self, events: List[Event]) -> None:
        await self.notifications.notify(events, data=self.data.copy())

    def register_domain_event(
        self,
        event_type: Type[Event],
        handler: Handler,
    ) -> None:
        self.domain_events.register(event_type, handler)

    def register_notify(
        self,
        event_type: Type[Event],
        handler: Handler,
    ) -> None:
        self.notifications.register(event_type, handler)
