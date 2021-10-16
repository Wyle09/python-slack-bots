import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv('SLACK_BOT_USER_OAUTH_TOKEN'))
print(os.getenv("OBSIDIAN"))