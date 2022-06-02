from aws_cdk import (
    aws_ec2 as ec2, aws_iam as iam, Stack
)
from constructs import Construct

class CdkEc2Stack2(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id,  **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="VPC1")

        sec_group1 = ec2.SecurityGroup(self, "iac_sg1",
            vpc=vpc, security_group_name="sec1",
           allow_all_outbound=True,
            )
      # add a new ingress rule to allow port 22 to internal hosts
        sec_group1.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22)
            )        # Security group 2
        #create a new security group
        sec_group2 = ec2.SecurityGroup(self, "iac_sg2",
            vpc=vpc, security_group_name="sec2",
            allow_all_outbound=True,
            )
        # add a new ingress rule to allow port 22 to internal hosts
        sec_group2.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22)
            )

