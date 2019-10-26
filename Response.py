from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

start = False

@app.route("/", methods=['GET'])
def test():
    return 'hello'

@app.route("/sms", methods=['GET','POST'])
def Start():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    global start
    resp = MessagingResponse()
    body = body.lower()

    while start == False:
        if body == 'start game':
            resp.message("Hello and welcome to Text Based Mini Games by Murray's Angels")
            start = True
        else:
            resp.message("Please enter one of the following commands; \n '- Start Game'")
    else:
        if body == 'reset':
            resp.message("Thanks for playing!")
            start = False

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT', 5000), host='0.0.0.0')
