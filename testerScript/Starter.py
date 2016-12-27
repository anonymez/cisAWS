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


def startProbe(rulename):
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=DEFAULT_REGION,
        # aws_session_token=SESSION_TOKEN,
    )
    client = boto3.client('config')
    try:
        response = client.get_compliance_details_by_config_rule(
            ConfigRuleName=rulename,
        )
    except :
        return False
    for ev in response["EvaluationResults"]:
        if (ev['ComplianceType']=='NON_COMPLIANT'):
            return False
    return True

if __name__ == '__main__':
    result=startProbe('rule-lambda-1')
    print "COMPLIANT:"+str(result)