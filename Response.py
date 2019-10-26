from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

start = False
reset = False

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
    global reset
    resp = MessagingResponse()
    body = body.lower()

    while start == False:
        if body == 'start game':
            message = "Hello and welcome to Text Based Mini Games by Murray's Angels"
            message += "\n Please enter one of the following options;"
            message += "\n\n 1 - Hangman \n 2- Survive The Midlands"
            resp.message(message)
            start = True
        else:
            resp.message("Please enter one of the following commands; \n '- Start Game'")

    if (body == '1'):
        resp.message(HangmanInit())
    elif (body == '2'):
        resp.message(SurviveInit())
    elif (body=='reset'):
        resp.message("Thanks for playing!")
        start = False
    else:
        resp.message("Please enter either 1 or 2!")

    return str(resp)

def HangmanInit():
    return 'This is hangman!'

def SurviveInit():
    return 'This is Survive The Midlands!'


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT', 5000), host='0.0.0.0')
