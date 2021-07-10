def portalLogin(mail, pwd):
    driver.get("https://www.placement.iitbhu.ac.in/accounts/login/?next=/students/")
    driver.find_element_by_id("id_login").send_keys(mail)
    driver.find_element_by_id("id_password").send_keys(pwd)
    driver.find_element_by_class_name("loginmodal-submit").click()

def getWillingness():
    result = []
    # -- If filters/search terms are to be passed then add params. 
    res = []
    for num in range(1,5):
        driver.get("https://www.placement.iitbhu.ac.in/company/opportunities?page="+ str(num))
        # -- modify link if filters and/or search keywords are passed
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
