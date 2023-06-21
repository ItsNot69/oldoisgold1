
from pyrogram import Client, filters, errors
import datetime
import time
from database.user import db
from bot.config import Config
import asyncio
import logging


@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID))
async def b_handler(bot, message):
    if not message.reply_to_message:
        await message.reply_text(
            text="Reply /broadcast to a message to broadcast."
        )
        return

    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )

    start_time = time.time()
    total_users = await db.get_all_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed = 0

    success = 0

    sem = asyncio.Semaphore(25)  # limit the number of concurrent tasks to 100

    async def run_task(user):
        async with sem:
            res = await broadcast_func(user, b_msg)
            return res

    tasks = []

    for user in users:
        task = asyncio.ensure_future(run_task(user))
        tasks.append(task)

    for res in await asyncio.gather(*tasks):
        success1, blocked1, deleted1, failed1, done1 = res
        done += done1
        blocked += blocked1
        deleted += deleted1
        failed += failed1
        success += success1

        if not done % 50:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")

    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")


async def broadcast_func(user, b_msg):
    success, blocked, deleted, failed, done = 0, 0, 0, 0, 0
    pti, sh = await broadcast_messages(int(user['user_id']), b_msg)
    if pti:
        success = 1
    elif pti == False:
        if sh == "Blocked":
            blocked = 1
        elif sh == "Deleted":
            deleted = 1
        elif sh == "Error":
            failed = 1
    done = 1
    return success, blocked, deleted, failed, done


async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except errors.FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except errors.InputUserDeactivated:
        
        logging.info(
            f"{user_id} - Removed from Database, since deleted account.")
        return False, "Deleted"
    except errors.UserIsBlocked:
        
        logging.info(f"{user_id} -Blocked the bot.")
        return False, "Blocked"
    except errors.PeerIdInvalid:
        
        logging.info(f"{user_id} - PeerIdInvalid")
        return False, "Error"
    except Exception as e:
        return False, "Error"
