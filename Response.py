from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
app = Flask(__name__)

@app.route("/", methods=['GET'])
def test():
    return 'hello'

@app.route("/sms", methods=['GET','POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT', 5000))