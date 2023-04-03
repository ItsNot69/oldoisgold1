import asyncio
from pyrogram import Client, errors
from pyrogram.types import ChatJoiner
from bot.config import Config, Script
import logging
from database.user import db
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def accept_all_requests(client: Client):
    total_requests = 0
    total_accepted = 0
    for chat in Config.CHAT_ID:
        try:
            try:
                requests = client.USER.get_chat_join_requests(chat_id=chat)
            except errors.FloodWait as e:
                await asyncio.sleep(e.value)
                requests = client.USER.get_chat_join_requests(chat_id=chat)
            async for request in requests:

                try:
                    request: ChatJoiner
                    if request.pending:
                        try:
                            await client.send_message(
                                chat_id=request.user.id,
                                text=Script.ACCEPT_MESSAGE,
                            )
                        except errors.FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(
                                chat_id=request.user.id,
                                text=Script.ACCEPT_MESSAGE,
                            )
                        except (errors.UserIsBlocked, errors.UserNotParticipant, errors.ChatWriteForbidden, errors.UserDeactivated, errors.UserBannedInChannel, errors.PeerIdInvalid, errors.RPCError):
                            logger.info(
                                f"User {request.user.id} is not available")
                        try:
                            await client.USER.approve_chat_join_request(
                                chat_id=chat,
                                user_id=request.user.id,
                            )
                        except errors.FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.USER.approve_chat_join_request(
                                chat_id=chat,
                                user_id=request.user.id,
                            )
                        await asyncio.sleep(1)
                        add_new_user(request.user.id)
                        total_accepted += 1

                except Exception as e:
                    logger.error(e, exc_info=True)
                total_requests += 1
        except Exception as e:
            logger.error(e, exc_info=True)
    return total_requests, total_accepted


async def add_new_user(user_id):
    try:
        if not await db.is_user_exist(user_id):
            await db.add_user(user_id)
            return True
    except Exception as e:
        logger.error(e, exc_info=True)
