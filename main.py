import asyncio
from message_sender import message_funnel

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(message_funnel())