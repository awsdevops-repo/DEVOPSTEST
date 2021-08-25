'''
Challenge #2
Summary
We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to you.

'''
import subprocess
import json

def Get_Instancedetails(ec2_details):
    #Get the Token for the curl commands this is required for v2 for v1 Token not required

    cmd = "curl -X PUT \"http://169.254.169.254/latest/api/token\" -H \"X-aws-ec2-metadata-token-ttl-seconds: 21600\""
    TOKENSTRING = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    TOKENSTRING = TOKENSTRING.stdout.read().splitlines()
    TOKEN=str(TOKENSTRING[0],'utf-8')

    cmd = "curl -H \"X-aws-ec2-metadata-token: "+TOKEN+"\" -v http://169.254.169.254/latest/meta-data/"+ec2_details
    DETAILSSTRING = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    DETAILSSTRING = DETAILSSTRING.stdout.read().splitlines() #This is to avoid \n and \r
    EC2_RESULT=str(DETAILSSTRING[0],'utf-8') # this is to remove \b
    #This is for defining Json
    data = {}
    data['instance'] = []
    data['instance'].append({
        ec2_details: EC2_RESULT,
    })
    with open('output.json', 'w') as outfile:
        json.dump(data, outfile)
    return


ec2_details=input("Please enter what details are required from the machine:") #You can give ami-id instance-action ,instance-id ,instance-life-cycle,instance-type,local-ipv4,etc
Get_Instancedetails(ec2_details):


