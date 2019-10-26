from twilio.rest import Client
import os

from dotenv import load_dotenv
load_dotenv()

auth_token = os.getenv("twillioAuth")
account_sid = os.getenv("twillioAccount")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447950878755",
    from_="+447480536962",
    body="Hello from Python again!")

print(message.sid)