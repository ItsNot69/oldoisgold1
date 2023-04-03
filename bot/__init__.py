from uvloop import install
install()

from bot.config import Config
from aiohttp import web
from pyrogram import Client
import logging.config
import logging



# Get logging configurations

logging.getLogger().setLevel(logging.INFO)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Approver Bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="bot/plugins"),
        )

    async def start(self):

        await super().start()
        self.USER = await Client(name="user", api_hash=Config.API_HASH, api_id=Config.API_ID, session_string=Config.SESSION_STRING).start()
        me = await self.get_me()
        self.owner = await self.get_users(int(Config.OWNER_ID))
        self.username = f"@{me.username}"

        logging.info(f"Bot started successfully. © {self.username}\n")
        logging.info(f"Owner: {self.owner.first_name}\n")
        logging.info(f"User: {self.USER.me.first_name}\n")

        if Config.WEB_SERVER:
            routes = web.RouteTableDef()

            @routes.get("/", allow_head=True)
            async def root_route_handler(request):
                res = {
                    "status": "running",
                }
                return web.json_response(res)

            async def web_server():
                web_app = web.Application(client_max_size=30000000)
                web_app.add_routes(routes)
                return web_app

            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8000).start()

    async def stop(self, *args):
        await super().stop()
