#!/usr/bin/env bash
pip2 install -r requirements.txt
echo -e "MOON Cloud\n\n******** Installing AWS Config probe\n\n"
cp AWSConfigRuleProbe.py /usr/lib/python2.7/site-packages/testagent-0.1.0-py2.7.egg/testagent/probes/
