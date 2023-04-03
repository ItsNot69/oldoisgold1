from pyrogram import Client, filters
from database.user import db
from bot.config import Config
from bot.utils import accept_all_requests, add_new_user


@Client.on_message(filters.command("start"))
async def start(client, message):
    await add_new_user(message.from_user.id)
    await message.reply_text<b>("ɪᴛ ᴄᴀɴ ᴀᴄᴄᴇᴘᴛ ʙᴏᴛʜ ɴᴇᴡ ᴀɴᴅ ᴘᴇɴᴅɪɴɢ ʀᴇQᴜᴇꜱᴛ. ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴄᴄᴇᴘᴛ ᴘᴇɴᴅɪɴɢ ʀᴇQᴜᴇꜱᴛ/ɢʀᴏᴜᴘ/n/nᴄᴏɴᴛᴀᴄᴛ ᴜꜱ @Botadmin44"
                            contact_button = InlineKeyboardButton("📱 Contact", url=f"t.me/Botadmin44")</b>)


@Client.on_message(filters.command("approve") & filters.private & filters.user(Config.OWNER_ID))
async def approve(client, message):
    sts = await message.reply_text("Approving...")
    requests, accepted = await accept_all_requests(client)
    await sts.edit_text("Done!, Total Requests: {}, Total Accepted: {}".format(requests, accepted))


@Client.on_message(filters.command("users") & filters.private & filters.user(Config.OWNER_ID))
async def users(client, message):
    sts = await message.reply_text("Getting users...")
    users = await db.get_all_users_count()
    await sts.edit_text("Total Users: {}".format(users))
