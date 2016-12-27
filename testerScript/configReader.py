import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("aws/credentials.ini")

dict1 = {}
options = Config.options("default")
for option in options:
    try:
        dict1[option] = Config.get("default", option)
        if dict1[option] == -1:
            print("skip: %s" % option)
    except:
        print("exception on %s!" % option)
        dict1[option] = None
ACCESS_KEY=dict1["aws_access_key_id"]
SECRET_KEY=dict1["aws_secret_access_key"]
DEFAULT_REGION=dict1["aws_default_region"]