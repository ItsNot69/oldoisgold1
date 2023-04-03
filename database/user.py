from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(Config.MONGO_DB_URI)
        self.db = self.client[Config.MONGO_DB_NAME]
        self.users = self.db.users

    async def get_user(self, user_id: int):
        user = await self.users.find_one({"user_id": user_id})
        return user

    async def add_user(self, user_id: int):
        await self.users.insert_one({"user_id": user_id})

    async def is_user_exist(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            return True
        return False

    async def update_user(self, user_id: int, data: dict):
        await self.users.update_one({"user_id": user_id}, {"$set": data})

    async def delete_user(self, user_id: int):
        await self.users.delete_one({"user_id": user_id})

    async def get_all_users(self):
        return await self.users.find().to_list(length=None)

    async def get_all_users_count(self):
        return await self.users.count_documents({})


db = Database()
