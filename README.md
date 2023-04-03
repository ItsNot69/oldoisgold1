README

This code block consists of several environment variables used in a Python program. These variables are set using the `os` module, which is used for interacting with the operating system.

*   `API_ID`: An integer value representing the API ID of the Telegram app, obtained from the Telegram API website. This variable is used to authenticate the bot's API requests to the Telegram servers.
    
*   `API_HASH`: A string value representing the API hash of the Telegram app, also obtained from the Telegram API website. This variable is used along with `API_ID` to authenticate the bot's API requests.
    
*   `BOT_TOKEN`: A string value representing the token of the Telegram bot, obtained from the BotFather bot. This variable is used to authenticate the bot with the Telegram servers and make API requests.
    
*   `OWNER_ID`: An integer value representing the Telegram user ID of the bot owner. This variable is used to restrict certain bot functions to the owner only.
    
*   `WEB_SERVER`: A boolean value indicating whether a web server is enabled or not. This variable is used to control certain bot functions related to web requests.
    
*   `CHAT_ID`: A list of integers representing the Telegram chat IDs of the chats that the bot will listen to. This variable is used to restrict the bot to specific chats and prevent it from responding to messages in other chats. Separate multiple chat IDs with a space.
    
*   `SESSION_STRING`: A string value representing the session string of the Telegram bot, obtained by running the Python script that creates a new session using the `pyrogram` library. This variable is used to keep the bot authenticated with the Telegram servers even after restarting the program.