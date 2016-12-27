from client import aws_connect
import ConfigParser
from avoidroot import rootlastaccess
from mfachecker import mfaenabled
#from unusedChecker import unused90


if __name__ == '__main__':

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
    ACCESS_KEY = dict1["aws_access_key_id"]
    SECRET_KEY = dict1["aws_secret_access_key"]
    DEFAULT_REGION = dict1["aws_default_region"]
    client = aws_connect("iam")
    #1.1
    print rootlastaccess(client,"2017-09-03T20:56:35.450686Z")
    #1.2
    print mfaenabled(client)
    #1.3
    #print unsed90(client)
