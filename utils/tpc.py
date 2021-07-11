import os

def portalLogin(mail, pwd):
    driver.get("https://www.placement.iitbhu.ac.in/accounts/login/?next=/students/")
    driver.find_element_by_id("id_login").send_keys(mail)
    driver.find_element_by_id("id_password").send_keys(pwd)
    driver.find_element_by_class_name("loginmodal-submit").click()

def getWillingness():
    result = []
    # -- If filters/search terms are to be passed then add params. 
    for num in range(1,5):
        driver.get("https://www.placement.iitbhu.ac.in/company/opportunities?page="+ str(num))
        # -- modify link if filters and/or search keywords are passed
        companies = driver.find_elements_by_class_name("company")
        for c in companies:
            company = {}
            # -- Add try except
            company['name'] = c.find_element_by_class_name("company_name").text
            company['profile'] =c.find_element_by_class_name("company_profile").text
            company['deadline'] =c.find_element_by_class_name("willingness_dead").text[23:]
            company['status'] = c.find_element_by_class_name("status").text[9:]
            company['exam_date'] = c.find_element_by_class_name("exam_date").text
            company['idd_package'] = c.find_elements_by_tag_name("td")[-2].text
            result.append(company)
    return result

def shortWillingness():
    input = getWillingness()
    # -- Add try except
    final_txt = str()
    for company in input:
        for (stat, value) in company.items():
            if stat not in ['status', 'exam_date', 'idd_package']:
                final_txt += '*' + stat + '* : ' + value + '\n'
    print(final_txt)
    return final_txt

def longWillingness():
    input = getWillingness()
    # -- Add try except
    final_txt = str()
    for company in input:
        for (stat, value) in company.items():
            final_txt += '*' + stat + '* : ' + value + '\n'
    print(final_txt)
    return final_txt

def getInterviewExperience(companyName):
    # ! fetch experiences from DB
    pass

def checkTPC(imsg):
    if imsg == 'tpc':
        return 'Menu of options for TPC command'
    
    # ! Retrieve email ID and pwd from DB if feature implemented 
    portalLogin(os.environ.get('TPC_EMAIL'),os.environ.get('TPC_PWD'))
    imsg = imsg[4:] # to skip the 'tpc ' part of the msg

    # ! Restructure this part and add try except
    tpc_dispatch = {
        '-willingness -short': shortWillingness,
        '-w -s': shortWillingness,
        '-willingness -details': longWillingness,
        '-w -d': longWillingness,
        # ! Both functions and options can be merged
    }
    if imsg[:15] == '-experience' or (imsg[4:7] == '-e ' and len(imsg) > 8):
        companyName = imsg.split(' ')[2]
        print(companyName)
        getInterviewExperience(companyName)
        # ? How to send company name for interview experiences with dispatch as other functions not taking input
    
    tpc_dispatch[imsg]()
    #! If all options fail, then return via this return statement. Edit it as well to show menu of options
    return 'I could not retrieve the results at this time, sorry.'
