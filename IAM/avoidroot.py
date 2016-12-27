from collections import defaultdict
import dateutil.parser
import csv

#date in iso 8601
def checklastaccess(aws_result, expected_access):
    #print aws_result
    #print expected_access
    result=dateutil.parser.parse(aws_result)
    expected=dateutil.parser.parse(expected_access)
    delta = expected-result
    if(expected>result):
        return True
    else:
        return False


def  rootlastaccess(client,expected_access):
    try:
        response = client.get_credential_report()
        report = csv.DictReader(response["Content"].split('\n'))
        # report = csv.reader(response["Content"].split('\n'))
        # print response["Content"]
    except Exception as e:
        print "ERROR"
        if e.response.get("Error").get("Code") == 'ReportNotPresent':
            print "not created"
            response = client.generate_credential_report()
            print response

    finally:
        columns = defaultdict(list)
        for row in report:  # read a row as {column1: value1, column2: value2,...}
            if row["user"] == "<root_account>":
                #expected_access = "2017-09-03T20:56:35.450686Z"
                if checklastaccess(row["password_last_used"], expected_access):
                    return True
                else:
                    return False