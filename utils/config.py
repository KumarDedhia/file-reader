import configparser

class Config():
    try:
        config = configparser.ConfigParser()
        config.read('/etc/temp/config.ini')
        aws_access_key_id = config['DEFAULT']['aws_access_key_id']
        aws_secret_access_key = config['DEFAULT']['aws_secret_access_key']
        region_name = config['DEFAULT']['region_name']
    except:
        print('Cannot load config.ini, using default setting.')
        aws_access_key_id = None
        aws_secret_access_key = None
        region_name = None
