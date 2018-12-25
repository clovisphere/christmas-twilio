from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with an 'X-Mas' message"""
    resp = VoiceResponse()
    resp.say("Hi, Clovis is away.. on his behalf, merry christmas, and happy holidays!", voice='alice')
    return str(resp)

if __name__ == "__main__":
    # For testing purposes. Not important on
    # Google App Engine.
    app.run(host='127.0.0.1', port=8080, debug=True)
