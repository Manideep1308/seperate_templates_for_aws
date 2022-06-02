from aws_cdk import (
    aws_ec2 as ec2, aws_iam as iam, Stack
)
from constructs import Construct

class CdkEc2Stack3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id,  **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="VPC1")

        sec_group1 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg1", vpc=vpc, security_group_name="sec1")
        sec_group2 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg2", vpc=vpc, security_group_name="sec2")
        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))
        # ubuntu image
        ub_image = ec2.MachineImage.from_ssm_parameter("/aws/service/canonical/ubuntu/server/focal/stable/current/amd64/hvm/ebs-gp2/ami-id")
        # Instance1
        instance = ec2.Instance(self, "IaCInstance1", instance_name="FirstEC2",
            instance_type=ec2.InstanceType("t2.large"),
            machine_image=ub_image,
            block_devices=[
                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(50))
            ],
            vpc = vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
             ),
            role=role,
            security_group=sec_group1,
            key_name = "iacvpc"
            )
        # Instance 2
        instance = ec2.Instance(self, "IaCInstance2", instance_name="SecondEC2",
            instance_type=ec2.InstanceType("t2.large"),
            machine_image=ub_image,
            block_devices=[
                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(50))
            ],
            vpc = vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
             ),
            role=role,
            security_group=sec_group2,
            key_name = "iacvpc"
        )

