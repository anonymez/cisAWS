import boto3

from testerScript.configReader import *

'''
client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN,
)
'''
# Or via the Session


def aws_connect(aws_service):
    #session = boto3.Session(
    #    aws_access_key_id=ACCESS_KEY,
    #    aws_secret_access_key=SECRET_KEY,
    #    region_name=DEFAULT_REGION,
    #    # aws_session_token=SESSION_TOKEN,
    #)

    client = boto3.client( aws_service,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
    return client
