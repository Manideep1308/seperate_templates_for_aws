from aws_cdk import (Stack, aws_ec2 as ec2, aws_iam as iam)
from constructs import Construct
class CdkEc2Stack1(Stack):
   def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
       super().__init__(scope, construct_id, **kwargs)
       vpc = ec2.Vpc(
           self, 'Vpc', vpc_name = 'VPC1',
           cidr = '10.0.0.0/16',
           max_azs=1,
           nat_gateways= 0,
           subnet_configuration=[
                   ec2.SubnetConfiguration(name='Subnet1', cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                   ec2.SubnetConfiguration(name='Subnet2', cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)])

