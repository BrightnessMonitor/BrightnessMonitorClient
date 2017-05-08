from pathlib import Path
import ConfigParser

def read_config():
    '''
    Read the config '/etc/brightnessmonitorclient.conf' and return it's content
    Returns:
        Config Dict with 'host', 'token', 'uuid'
    '''
    ConfigPath = "/etc/brightnessmonitorclient.conf"
    configFile = Path(ConfigPath)

    # check if config exists
    if configFile.is_file() == False:
        return "Missing config '%s", ConfigPath

    # read config
    Config = ConfigParser.ConfigParser()
    Config.read(ConfigPath)

    return {
        'host': Config.get('Login', 'host'),
        'token': Config.get('Login', 'token'),
        'uuid': Config.get('Login', 'uuid'),
    }