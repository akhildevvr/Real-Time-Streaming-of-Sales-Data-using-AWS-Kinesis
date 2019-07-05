# Real-Time-Streaming-of-Stock-Data-using-AWS-Kinesis
 
The project starts with a Python program to  source stock data online, but also optimise its use of downloaded data, to avoid excessive network traffic. Users will have the possibility of searching for specific stocks, and query specified time ranges for downloading the data.


Part 1 : AWS Basics

AWS IAM user and AWS configure command line utility
S3 buckets
Kinesis Data Stream
Kinesis Firehose
EC2 and security group for SuperSet
AWS IAM User
IAM user are like ID card equivalent of real world. They just show who you are and what you can do (Permissions). We will create a user with name first_time_aws_user with ADMIN Privilages.

**Procedure create IAM user**

Go to top right corner click on your name, then select my security credentials. 


**AWS Configure Command Line Utility**

At times we will eexcute some commands from terminal, without using the webiste console. In order to do that, we need set up the credentials so the commands can login on our behalf.

Procedure to configure command line
Open up terminal and install the awscli and boto3 library, verify the installation using the --version command.

pip install awscli boto3 --user
aws --version

Now we can configure the credentials using the following command

aws configure

Enter the access key and secret key from the credentails file we downloaded in previous section. Write the region as eu-west-1 and output format as json 

**S3 Buckets**

S3 Buckets

They are storage options, like google drive where you can put anything you want.

**Kinesis Data Stream and FireHose**

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.


Create a new file/jupyter notebook and past the code, also change the StreamName value to your streamName in the last line. After one minute check the S3 bucket for a newley created file.

# Save this File as : stock_data_streaming.py

import boto3
import json

def generate_data_json():
    stock = {
            'Date':df['Date'],
            'High':df['High'],
            'Low': df['Low'],
             'Open' : df['Open'],
             'Close' : df['Close'],
             'Adj Close': df['Adj Close']
             }
    return stock

kinesis_client = boto3.client('kinesis', region_name='eu-west-1')
while(1):
    # generate data
    data = generate_data_json()
    
    response = kinesis_client.put_record(Data=json.dumps(data) + "\n", # convert to json before sending the data
                          PartitionKey = data['Date'], 
                          StreamName='workshop_stream_1') 
    pprint(response['ResponseMetadata']['HTTPStatusCode'])

    time.sleep(0.8)
