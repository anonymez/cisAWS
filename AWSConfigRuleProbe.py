__author__ = 'Filippo Gaudenzi'
__email__ = 'filippo.gaudenzi@unimi.it'

from testagent.probe import Probe
import boto3

# TODO controlli
class AWSConfigRuleProbe(Probe):
    def ec2Run(self, inputs):
        client = boto3.client('config',
                              aws_access_key_id=self.testinstances["config"]["aws_access_key"],
                              aws_secret_access_key=self.testinstances["config"]["aws_secret_access_key"],
                              region_name=self.testinstances["config"]["region"])
        try:
            response = client.get_compliance_details_by_config_rule(
                ConfigRuleName=self.testinstances["rule"]["rulename"],
            )
        except:
            return False
        print response
        for ev in response["EvaluationResults"]:
            if (ev['ComplianceType'] == 'NON_COMPLIANT'):
                return False
        return True


    def ec2RunR(self, inputs):
        return

    def appendAtomics(self):
        self.appendAtomic(self.ec2Run, self.ec2RunR)
        # seld.appendAtomic(self.nmapParse,self.nmapParseR)


probe = AWSConfigRuleProbe

