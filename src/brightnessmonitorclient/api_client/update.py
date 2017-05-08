from datetime import datetime
import requests
import json

from brightnessmonitorclient.config.read_config import read_config


def upload(value, time):
    '''
    Upload the value & time to the website
    
    Args:
        value: The value witch should be upload
        time: The datetime witch should be upload

    Returns:
        True if the upload was successfull
        False if the upload was not successfull

    '''
    config = read_config()





    url = 'http://localhost:8000/api/device/'
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
