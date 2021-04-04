# Custom Whatsapp Bot for Admiral Aokiji
### Git repository of data hosted at Heroku for continuous deployment.

This custom bot works on the webhooks provided by the TwilioML package. It scrapes the Training and Placement Website of IIT BHU after logging in and sends the user information about the willingnesses available.
Chrome Driver, Google Chrome and Python need to be installed on Heroku. FOllow the instructions given in <a href='https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/'>this article</a> to complete it.
Environment variables need to be also added there itself.

Overall guide- <a href='https://github.com/Jatin-8898/covid-bot'>this repo on Github</a>
Painpoints:
- Add more features
- Need to hit the TPC route every 6 or 12 hours which is not happening currently
- Maintaining a DB of users so that multiple users can use it at the same time