import asyncio
import logging
import sys
import asyncio_gevent

logger = logging.getLogger("uvicorn.error")


def asyncio_setup(reload: bool = False) -> None:  # pragma: no cover
    asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())
