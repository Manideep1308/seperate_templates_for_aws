
from flask import Flask, request
 
app = Flask(__name__)
 
 
@app.route('/vpc', methods=['POST'])

def with_parameters():

    stacknumber = request.args.get('stacknumber')
    vpcname = request.args.get('vpcname')
    vpcaddress = request.args.get('vpcaddress')   
    max_azs = request.args.get('max_azs')
    nat_gateway = request.args.get('nat_gateway')
    subnet1name = request.args.get('subnet1name')
    subnet1address = request.args.get('subnet1address')
    subnet_type1 = request.args.get('subnet_type1')
    subnet2name = request.args.get('subnet2name')
    subnet2address = request.args.get('subnet2address')
    subnet_type2 = request.args.get('subnet_type2')
    cloudenv = request.args.get('cloudenv')
   
   
    data = (
        "from aws_cdk import (Stack, aws_ec2 as ec2, aws_iam as iam)\n"
        "from constructs import Construct\n"
        "class CdkEc2Stack" + str(stacknumber) + "(Stack):\n"
        "   def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n"
        "       super().__init__(scope, construct_id, **kwargs)\n" 
        "       vpc = ec2.Vpc(\n"
        "           self, 'Vpc', vpc_name = '"  + str(vpcname)  + "',\n"
        "           cidr = '" + str(vpcaddress) + "',\n"
        "           max_azs=" + str(max_azs) + ",\n" 
        "           nat_gateways= " + str(nat_gateway) + ",\n"
        "           subnet_configuration=[\n"
        "                   ec2.SubnetConfiguration(name='" + str(subnet1name) + "', cidr_mask=" + str(subnet1address) + ", subnet_type=ec2.SubnetType." + str(subnet_type1) + "),\n"
        "                   ec2.SubnetConfiguration(name='" + str(subnet2name) + "', cidr_mask=" + str(subnet2address) + ", subnet_type=ec2.SubnetType." + str(subnet_type2) + ")])\n"
            

    )

    data1= (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n'
'      "vnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "'+ str(vpcname)+ '",\n'
'        "metadata": {\n'
'          "description": "VNet name"\n'
'        }\n'
'      },\n'
'      "vnetAddressPrefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(vpcaddress) + '",\n'
'        "metadata": {\n'
'          "description": "Address prefix"\n'
'        }\n'
'      },\n'
'      "subnet1Prefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet1address) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Prefix"\n'
'        }\n'
'      },\n'
'      "subnet1Name": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet1name) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Name"\n'
'        }\n'
'      },\n'
'      "subnet2Prefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet2address) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 2 Prefix"\n'
'        }\n'
'      },\n'
'      "subnet2Name": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet2name) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 2 Name"\n'
'        }\n'
'      },\n'
'      "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "resources": [\n'
'      {\n'
'        "type": "Microsoft.Network/virtualNetworks",\n'
'        "apiVersion": "2020-06-01",\n'
'        "name": "[parameters(''\'vnetName\''')]",\n'
'        "location": "[parameters(''\'location\''')]",\n'
'        "properties": {\n'
'          "addressSpace": {\n'
'            "addressPrefixes": [\n'
'              "[parameters(''\'vnetAddressPrefix\''')]"\n'
'            ]\n'
'          },\n'
'          "subnets": [\n'
'            {\n'
'              "name": "[parameters(''\'subnet1Name\''')]",\n'
'              "properties": {\n'
'                "addressPrefix": "[parameters(''\'subnet1Prefix\''')]"\n'
'              }\n'
'            },\n'
'            {\n'
'              "name": "[parameters(''\'subnet2Name\''')]",\n'
'              "properties": {\n'
'                "addressPrefix": "[parameters(''\'subnet2Prefix\''')]"\n'
'              }\n'
'            }\n'
'          ]\n'
'        }\n'
'      }\n'
'    ]\n'
' }\n'
    )

    if(str(cloudenv) =='aws'):
        with open('vpc_template.py', 'w') as f:
            print(data, file=f)

        return data

    if(str(cloudenv) == 'azure'):
        with open('vpc_template.json', 'w') as f:
            print(data1, file=f)

        return data1

    else:
        return 'not matched'                
    
app.run(port=8001, host='0.0.0.0')