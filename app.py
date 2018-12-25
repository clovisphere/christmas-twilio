from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Merry X-Mas' message"""
    # Start our TwiML response
    resp = VoiceResponse()
    # Read a message aloud to the caller
    resp.say("Hi, Clovis is away.. on his behalf, merry christmas, and happy holidays!", voice='alice')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
