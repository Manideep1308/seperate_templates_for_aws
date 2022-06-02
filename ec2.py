from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/ec2', methods=['POST'])

def fun():

    stacknumber = request.args.get('stacknumber') 
    vpcname = request.args.get('vpcname')
    securitygroup1name = request.args.get('securitygroup1name')
    securitygroup2name = request.args.get('securitygroup2name')
    instance1name = request.args.get('instance1name')
    instance2name = request.args.get('instance2name')
    instance1type = request.args.get('instance1type')
    instance2type = request.args.get('instance2type')
    instance1volume = request.args.get('instance1volume')
    instance2volume = request.args.get('instance2volume')
    keyname = request.args.get('keyname')




    data=(

'from aws_cdk import (\n'
'    aws_ec2 as ec2, aws_iam as iam, Stack\n'

')\n'

'from constructs import Construct\n'

'\n'
'class CdkEc2Stack' + str(stacknumber) + '(Stack):\n'
'\n'
'    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n'
'        super().__init__(scope, construct_id,  **kwargs)\n'
'\n'
'        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="' + str(vpcname) + '")\n'
'\n'
'        sec_group1 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg1", vpc=vpc, security_group_name="' + str(securitygroup1name) + '")\n'
'        sec_group2 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg2", vpc=vpc, security_group_name="' + str(securitygroup2name) + '")\n'
        
                
'        # Instance Role and SSM Managed Policy\n'
'        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))\n'
'        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))\n'


'        # ubuntu image\n'
'        ub_image = ec2.MachineImage.from_ssm_parameter("/aws/service/canonical/ubuntu/server/focal/stable/current/amd64/hvm/ebs-gp2/ami-id")\n'

'        # Instance1\n'
'        instance = ec2.Instance(self, "IaCInstance1", instance_name="' + str(instance1name) + '",\n'
'            instance_type=ec2.InstanceType("' + str(instance1type) + '"),\n'
'            machine_image=ub_image,\n'
'            block_devices=[\n'
'                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(' + str(instance1volume) + '))\n'
'            ],\n'
'            vpc = vpc,\n'            
'            vpc_subnets=ec2.SubnetSelection(\n'
'                subnet_type=ec2.SubnetType.PUBLIC\n'
'             ),\n'
'            role=role,\n'
'            security_group=sec_group1,\n'
'            key_name = "' + str(keyname) + '"\n'
'            )\n'
    

'        # Instance 2\n'
'        instance = ec2.Instance(self, "IaCInstance2", instance_name="' + str(instance2name) + '",\n'
'            instance_type=ec2.InstanceType("' + str(instance2type) + '"),\n'
'            machine_image=ub_image,\n'
'            block_devices=[\n'
'                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(' + str(instance2volume) + '))\n'                
'            ],\n'
'            vpc = vpc,\n'
'            vpc_subnets=ec2.SubnetSelection(\n'
'                subnet_type=ec2.SubnetType.PUBLIC\n'
'             ),\n'
'            role=role,\n'
'            security_group=sec_group2,\n'
'            key_name = "' + str(keyname) + '"\n'
'        )\n'
    )

    with open('ec2_template.py', 'w') as f:
        print(data, file=f)

    return data    

app.run(port=8003, host='0.0.0.0')    