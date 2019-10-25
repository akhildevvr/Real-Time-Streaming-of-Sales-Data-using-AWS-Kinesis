# Real-Time-Streaming-of-Sales-Data-using-AWS-Kinesis
 
The project starts with a Python program to  source stock data online, but also optimise its use of downloaded data, to avoid excessive network traffic. Users will have the possibility of searching for specific stocks, and query specified time ranges for downloading the data.


Part 1 : AWS Basics

AWS IAM user and AWS configure command line utility
S3 buckets
Kinesis Data Stream
Kinesis Firehose
EC2 and security group for SuperSet
AWS IAM User
IAM user are like ID card equivalent of real world. They just show who you are and what you can do (Permissions). We will create a user with name first_time_aws_user with ADMIN Privilages.



AWS Configure Command Line Utility
At times we will eexcute some commands from terminal, without using the webiste console. In order to do that, we need set up the credentials so the commands can login on our behalf.

Procedure to configure command line
Open up terminal and install the awscli and boto3 library, verify the installation using the --version command.

    pip install awscli boto3 --user
    aws --version
Now we can configure the credentials using the following command

aws configure
Enter the access key and secret key from the credentails file we downloaded in previous section. Write the region as eu-west-1 and output format as json.

S3 Buckets
They are storage options, like google drive where you can put anything you want.

Postgres RDS
RDS is a service for managed (maintained-backup, storage, update etc) databases - Oracle, Postgres, Mysql, Microsoft Sql Server, Aurora.

Kinesis Data Stream and FireHose
Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.


Let's send some data to the kinesis stream
Create a new file/jupyter notebook and past the code, also change the StreamName value to your streamName in the last line. After one minute check the S3 bucket for a newley created file.

    # Save this File as : sample_producer.py
    import boto3
    import json

    kinesis_client = boto3.clinet("kinesis", region='eu-west-1')

    data = {'store_id': 13
            'transaction_id': 1234,
            'sale': 15,
            'item': ["apples", "plums", "grapes", "oranges", "beans"]
           }

    # send the record
    kinesis_client.put_record('Data':json.dumps(data) + "\n", # convert to json before sending the data
                              'PartitionKey': data['city'], 
                              StreamName='my-first-stream')   # change me
                          
                   
AWS Lambda Function
AWS Lambda is a compute service that lets you run code without provisioning or managing servers. AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume - there is no charge when your code is not running.


AWS EC2 and Security groups
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction.

Setup Security Group
If you have worked in a company, you need to open specific ports for connection. Security groups tells which ports are open and for which IP addrees. We will run superset on port 8080, so we need to open that port. Currently only port 22 is open, which we need for SSHing into the remote computer. Click on the EC2 machine, in the description section, click on inbound rules. This will show the ports which are open.


Install superset
Lets install superset on the machine

# dependencies
  sudo apt update &&  sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev
  sudo pip3 install pandas==0.23.4 SQLAlchemy==1.2.2 psycopg2-binary pymssql superset

# one time setup
  export FLASK_APP=superset
  flask fab create-admin  --username admin123 --password admin1234 --firstname admin --lastname admin --email admin@gma.com
  superset db upgrade 
  superset init

# start superset
  superset runserver -p 8080
Find public IP of your machine and go to this website

public-IP:8080

Login ID : admin123

Password : admin1234

Public IP from the description
