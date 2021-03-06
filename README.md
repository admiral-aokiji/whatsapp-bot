# Custom Whatsapp Bot for Admiral Aokiji
## Git repository of data hosted at Heroku for continuous deployment.

It scrapes the Training and Placement Website of IIT BHU after logging in and sends the user information about the willingnesses available.
This custom bot works on the webhooks provided by the TwilioML package. 
Chrome Driver, Google Chrome and Python need to be installed on Heroku. Follow the instructions given in <a href='https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/'>this article</a> to complete it.
Environment variables need to be also added there itself.

Starting guide- <a href='https://github.com/Jatin-8898/covid-bot'>this repo on Github</a>

**Painpoints**:
- Cron jobs to automate TPC scraping every 6 or 12 hours is not happening currently
- How to store email ids and passwords for documents and TPC login
- "Read More/Next" feature based on last message received
- Future issues of maintaining Twilio sandboxes on scaling
- Sending custom error messages based on last message sent 
- Maintaining a DB of users and messasges 
  1. so that multiple users can use it at the same time
  2. Persistenency of messages

## Proposed menu of top level messages:
Allowed Messages  | Function                                                              |
------------------|-----------------------------------------------------------------------| 
Hi, Hey, Menu     | Shows menu/possible messages                                          | 
TPC               | Shows menu of TPC commands                                            | 
Documents         | Shows menu of possible commands for retrieving personal documents     | 
Puzzles           | Send a random puzzle from GFG                                         | 
Creator           | View details of creators to share your regards, suggestions or doubts | 
Signup            | Signup for this service to unlock more features                       |

## Proposed menu of sub-level messages for TPC portal:
Allowed Messages                           | Function                                                                              |
-------------------------------------------|---------------------------------------------------------------------------------------| 
TPC -signup [email] [pwd]                  | Add email id and password to database to get updates from the TPC portal              |
TPC -update [email/pwd] [new_value]        | Update email id and password in case password changed                                 |
TPC -download [final_resume_number]        | Download resume from portal                                                           |
TPC -willingness -short, TPC -w -s         | List of companies willingness status and deadlines and other important dates          |
TPC -willingness -details, TPC -w -d       | List of companies willingness status, deadlines, other important dates, packages, etc.|
TPC -experience [company_name], TPC -e     | Shares a placement experience of the company mentioned                                |
TPC -stats [year] [profile]                | Shares stats of companies open for the branch of the user for the given year and field|

- Possible values of profile: SDE, DA, BA, PM, ML, DS, WD, Other
- Possible values of year: 2019, 2020
- Add warning on signup that it would be better for the user to signup by first messaging the Creators

## Proposed menu of sub-level messages for Documents:
Allowed Messages                | Function                                                     |
--------------------------------|--------------------------------------------------------------|
Documents -get_doc [name], -g   | Sends the file for the input document                        |
Documents -list, -l             | Shows list of uploaded files                                 |
Documents -send_doc [name], -s  | Share and save a document on our server for future retrieval |

- Include naming convention when showing commands for Documents message
- Possible values of document: POR_certificate(i), internship_certificate(i), aadhar, sem(i)_marksheet, 12th_marksheet, 10th_marksheet, rfid, bonafide(i), resume-(profile)


## Proposed menu of sub-level messages for Puzzles:
Allowed Messages            | Function                              |
----------------------------|---------------------------------------|
Puzzle -random, -r          | Share a random puzzle                 |
Puzzle [number]             | Share a specific puzzle               |
Puzzle -list, -l            | Show full list of puzzles             |
Puzzle [number] -answer, -a | Share the answer of a specific puzzle |

## Proposed menu of sub-level messages for Admin:
Allowed Messages            | Function                              |
----------------------------|---------------------------------------|
Admin -dashboard, -d        | Get link for the app's live portal    |
Admin add_puzzle [number]   | Add a puzzle                          |
Admin add_article [number]  | Add an article                        |
 
## Possible addition of features in future:

1. Dictionary, word of the day and vocab_test
2. RC test ??
3. Company info for HR interview
4. Custom notes retrieval (HR answers template, cheatsheets, etc.)
5. Helpful Articles Link sharing
6. Custom articles saving
7. Send amazing sticker 