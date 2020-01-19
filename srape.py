import requests
from lxml import html

USERNAME = "client UN" #get from html elements?
PASSWORD = "client PW" 

LOGIN_URL = "https://members.bellevueclub.com/?returnUrl=/Departments/Tennis/"
URL = "https://BC.GameTime.net/scheduling/index/index/sport/1"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "CSIMember.username": USERNAME, 
        "CSIMember.password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
