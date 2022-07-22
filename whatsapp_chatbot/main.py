import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.pythonREPL import execute_python

app = Flask (__name__)

@app.route("/bot", methods = ['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    print(incoming_msg)

    resp= MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith('#!python3'):
        code = incoming_msg.strip('#!python3')
        output = execute_python(code)
        msg.body(output)

    # output = execute_python(incoming_msg)
    # msg.body(output)
    return str(resp)

if __name__ == '__main__':
    app.run()
