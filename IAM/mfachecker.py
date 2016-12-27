import csv
from collections import defaultdict


def mfaenabled(client,users=[]):
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
            if row["mfa_active"] == "false":
                if len(users)==0:
                    found=False
                else:
                    changeB=True
                    for us in users:
                        if row["user"]==us:
                            changeB=False
                            break;
            # expected_access = "2017-09-03T20:56:35.450686Z"
    return found