from datetime import datetime
import requests
import json

from brightnessmonitorclient.config.read_config import read_config


def upload(value, dateNow):
    '''
    
    Args:
        value: The value witch should be upload
        datetime: The datetime witch should be upload

    Returns:

    '''
    config = read_config()





    url = 'http://localhost:8000/api/device/'
    data = {
        "uuid": config['uuid'],
        "datetime": dateNow,
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
