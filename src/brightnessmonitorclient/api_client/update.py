import urllib2
import httplib
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
    print responseContent

    if responseContent['status'] == "Success: data saved":
        return True
    else:
        return False


def internet_on():
    """
    Check if there is a connection to the website
    
    Returns:
        True == Website is on
        False == Website is offline

    """
    config = read_config()

    if config['protocol'] == "https":
        c = httplib.HTTPSConnection(config['host'])
    else:
        c = httplib.HTTPConnection(config['host'])

    try:
        c.request("GET", "/")
    except Exception as e:
        print("Connection error:")
        print(e)
        return False

    response = c.getresponse()
    if response.status == 200:
        return True
    else:
        return False
