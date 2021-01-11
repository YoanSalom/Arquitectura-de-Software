import os

from pymongo import MongoClient

# Create the RevyBot Class
class RevyBot:

    # Create a constant that contains the default texts for the message
    FRASES = [
        {
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "HELLO!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "BIG BOSSU!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "BUENOS DIAS!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NICE TO MEET YA!"
                }
            }

        }
    ]

    
    # The constructor for the class.
    def __init__(self, channel):
        self.channel = channel
        self.client = MongoClient(os.environ.get("MONGO_PORT"))
        self.db = self.client.frases
        self.frases = self.db.frases
        self.frases.insert_many(self.FRASES)

    
    #Get random message from db
    def _choose_message(self):
        return self.frases.aggregate([{ "$sample": {"size": 1} }]).next()["dict"]
    

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._choose_message()
            ]
        }
