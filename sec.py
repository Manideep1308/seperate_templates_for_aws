from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/secgroup', methods=['POST'])

def fun():

    
  stacknumber = request.args.get('stacknumber') 
  vpcname = request.args.get('vpcname')
  securitygroup1name = request.args.get('securitygroup1name')
  securitygroup2name = request.args.get('securitygroup2name') 
  sec1outboundrule = request.args.get('sec1outboundrule')
  sec1sourceaddress = request.args.get('sec1sourceaddress')
  protocol = request.args.get('protocol')
  sec1port = request.args.get('sec1port')
  sec2outboundrule = request.args.get('sec2outboundrule')
  sec2sourceaddress = request.args.get('sec2sourceaddress')
  sec2port = request.args.get('sec2port')

  data = (

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
'        sec_group1 = ec2.SecurityGroup(self, "iac_sg1",\n'
'            vpc=vpc, security_group_name="' + str(securitygroup1name) + '",\n'
'           allow_all_outbound=' + str(sec1outboundrule) + ',\n'
'            )\n'
        
'      # add a new ingress rule to allow port 22 to internal hosts\n'
'        sec_group1.add_ingress_rule(\n'
'            peer=ec2.Peer.ipv4("' + str(sec1sourceaddress) + '"),\n'
'            description="Allow SSH connection", \n'
'            connection=ec2.Port.' + str(protocol) + '(' + str(sec1port) + ')\n'
'            )'

'        # Security group 2\n'
'        #create a new security group\n'
'        sec_group2 = ec2.SecurityGroup(self, "iac_sg2",\n'
'            vpc=vpc, security_group_name="' + str(securitygroup2name) + '",\n'
'            allow_all_outbound=' + str(sec2outboundrule) + ',\n'
'            )\n'

'        # add a new ingress rule to allow port 22 to internal hosts\n'
'        sec_group2.add_ingress_rule(\n'
'            peer=ec2.Peer.ipv4("' + str(sec2sourceaddress) + '"),\n'
'            description="Allow SSH connection", \n'
'            connection=ec2.Port.' + str(protocol) + '(' + str(sec2port) + ')\n'
'            )\n'
    )

  with open('sec_template.py', 'w') as f:
        print(data, file=f)

  return data

app.run(port=8002, host='0.0.0.0')        