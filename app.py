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
    
    if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'Menu' in incoming_msg:
        text = f'Hello\n For any suggestions or requests 👇 \n 📞 : 9537701631 \n ✉ : rohit.saxena.met17@itbhu.ac.in \n\n Please enter one of the following option 👇 \n *TPC*. TPC portal willingness \n *B*. __________. '
        msg.body(text)
        responded = True

    if 'TPC' in incoming_msg:
        # return total cases
        driver.get("https://www.placement.iitbhu.ac.in/accounts/login/?next=/students/")
        driver.find_element_by_id("id_login").send_keys(os.environ.get('TPC_EMAIL'))
        driver.find_element_by_id("id_password").send_keys(os.environ.get('TPC_PWD'))
        driver.find_element_by_class_name("loginmodal-submit").click()
        result = []
        def companyData(pagesNo):
            res = []
            for num in range(1,pagesNo+1):
                driver.get("https://www.placement.iitbhu.ac.in/company/opportunities?page="+ str(num))
#                 r = requests.get('https://www.placement.iitbhu.ac.in/company/opportunities?page="+ str(num)')
#                 if r.status_code == 200:
                companies = driver.find_elements_by_class_name("company")
                for z in companies:
                    x = {}
                    x['name'] =z.find_element_by_class_name("company_name").text
                    x['profile'] =z.find_element_by_class_name("company_profile").text
                    x['deadline'] =z.find_element_by_class_name("willingness_dead").text[23:]
                    x['status'] =z.find_element_by_class_name("status").text[9:]
                    x['exam_date'] = z.find_element_by_class_name("exam_date").text
                    x['idd_package'] = z.find_elements_by_tag_name("td")[-2].text
                    res.append(x)
            return res
        result = companyData(3)
        text = ''
        for company in result:
            for (stat,value) in company.items():
                text += '*' + stat + '* : ' + value + '\n'
        print(text)
#         else:
#             text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if responded == False:
        msg.body('Please enter valid commands')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)


