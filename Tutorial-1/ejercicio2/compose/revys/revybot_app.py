import os

from slack import WebClient
from revybot import RevyBot

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Create a new RevyBot
revy_bot = RevyBot("general")

# Get the onboarding message payload
message = revy_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
