from pyrogram import Client, types, errors
from bot.config import Script
import logging

from bot.utils import add_new_user

logger = logging.getLogger(__name__)


@Client.on_chat_join_request()
async def join_request(client, update: types.ChatJoinRequest):
    await add_new_user(update.from_user.id)
    try:
        await client.send_message(
            chat_id=update.from_user.id,
            text=Script.ACCEPT_MESSAGE,
        )

    except (errors.UserIsBlocked, errors.UserNotParticipant, errors.ChatWriteForbidden, errors.UserDeactivated, errors.UserBannedInChannel, errors.PeerIdInvalid, errors.RPCError):
        logger.info(f"User {update.from_user.id} is not available")

    await update.approve()
