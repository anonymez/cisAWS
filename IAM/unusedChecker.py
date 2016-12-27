import csv
from collections import defaultdict
from datetime import datetime
#import pytz # $ pip install pytz
import dateutil.parser



#TODO: investigate timezone aws

LAST_USED=90
def last_used(day,last_used):
    result = dateutil.parser.parse(day)
    #now=(datetime.now(pytz.timezone("America/New_York")))
    now = datetime.utcnow()
    delta = now-result
    if (delta.days>=90):
        return False
    else:
        return True



def unused90(client):
    try:
        response = client.get_credential_report()
        report = csv.DictReader(response["Content"].split('\n'))

    except Exception as e:
        print "ERROR"
        if e.response.get("Error").get("Code") == 'ReportNotPresent':
            print "not created"
            response = client.generate_credential_report()
            print response

    finally:
        found=True;
        columns = defaultdict(list)
        for row in report:  # read a row as {column1: value1, column2: value2,...}
           if not(row["password_enabled"]=="true" and lastused(row["password_last_used"],LAST_USED)):
               return False
    return found