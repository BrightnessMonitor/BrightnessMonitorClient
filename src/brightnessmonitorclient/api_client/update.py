import urllib2
from datetime import datetime
import requests
import json

from brightnessmonitorclient.config.read_config import read_config


def upload(value, time):
    '''
    Upload the value & time to the website
    
    Args:
        value: The value which should be uploaded
        time: The datetime which should be uploaded

    Returns:
        True if the upload was successful
        False if the upload was not successful

    '''
    config = read_config()

    url = config['protocol'] + "://" + config['host'] + "/api/device/"
    data = {
        "uuid": config['uuid'],
        "datetime": time,
        "value": value
    }
    response = requests.post(url,
                             data=data,
                             headers={'Authorization': 'Token {}'.format(config['token'])}
                             )
    responseContent = json.loads(response._content)

    if responseContent['status'] == "Success: data saved":
        return True
    else:
        return False

def internet_on():
    try:
        urllib2.urlopen('http://google.de', timeout=1)
        return True
    except urllib2.URLError as err:
        return False