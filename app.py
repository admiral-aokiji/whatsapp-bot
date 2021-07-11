from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
app = Flask(__name__)
import utils

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if incoming_msg in ['Hi', 'Hey', 'Menu']:
        text = f'Hello\n For any suggestions or requests 👇 \n 📞 : 9537701631 \n ✉ : rohit.saxena.met17@itbhu.ac.in \n\n Please enter one of the following option 👇 \n *TPC*. TPC portal willingness \n *B*. __________. '
        msg.body(text)
        responded = True

    elif 'TPC' in incoming_msg:
        if incoming_msg == 'TPC':
            text = 'Menu of options for TPC command'
            msg.body(text)
            h = 7
            responded = True
         
        utils.portalLogin(os.environ.get('TPC_EMAIL'),os.environ.get('TPC_PWD'))
        if incoming_msg == 'TPC -willingness -short' or incoming_msg == 'TPC -w -s':
            utils.getWillingness()
            utils.shortenWillingness()
        elif incoming_msg == 'TPC -willingness -details' or incoming_msg == 'TPC -w -d':
            utils.portalLogin(os.environ.get('TPC_EMAIL'),os.environ.get('TPC_PWD'))
            utils.getWillingness()
        elif incoming_msg == 'TPC -willingness -details' or incoming_msg == 'TPC -w -d':
            utils.portalLogin(os.environ.get('TPC_EMAIL'),os.environ.get('TPC_PWD'))
            utils.getWillingness()
        elif incoming_msg[:15] == 'TPC -experience' or (incoming_msg[:7] == 'TPC - e ' and len(incoming_msg)>8):
            utils.portalLogin(os.environ.get('TPC_EMAIL'),os.environ.get('TPC_PWD'))
            companyName = incoming_msg.split(' ')[2]
            print(companyName)
            utils.getInterviewExperience(companyName)
        else:
            # send custom error msg for TPC commands
            pass
    else:
        # Checking for formality
        if responded == False:
            msg.body('Please enter valid commands')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)


