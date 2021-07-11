from flask import Flask, request
import os
from utils import puzzles,tpc
from twilio.twiml.messaging_response import MessagingResponse
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
app = Flask(__name__)


def getMenu():
    #-- Refine
    return f'Hello\n Main menu: \n *TPC*- TPC portal willingness \n *Puzzle*- Solves puzzles from GFG '

def getCreator():
    #-- Refine
    return f'For any suggestions or requests, contact using 👇 \n 📞 : 9537701631 \n ✉ : rohit.saxena.met17@itbhu.ac.in'

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    dispatch = {
                'hey': getMenu,
                'hi': getMenu,
                'menu': getMenu,
                'tpc': tpc.checkTPC,
                'puzzle': puzzles.checkPuzzles,
                'creator': getCreator
            }

    if incoming_msg and len(incoming_msg.split(' ')):
        msg_string = dispatch[incoming_msg[0]](incoming_msg)
        msg.body(msg_string)
        responded = True

    if responded == False:
        msg.body('Please enter valid commands')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)


