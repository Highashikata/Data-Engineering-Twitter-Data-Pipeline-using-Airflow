# Data-Engineering-Twitter-Data-Pipeline-using-Airflow

In this project we will use this architecture ![image](https://github.com/Highashikata/Data-Engineering-Twitter-Data-Pipeline-using-Airflow/assets/96960411/3e42197d-bef8-468d-b4e7-6ccc1af9497c)
in order to build a data pipeline by extarcting data from twitter using the ```tweepy``` which is Python API that enables us to connect to Twitter.

So we are going to get data from Twitter and transform it in Airflow using Python (Deployed in AWS EC2 instance) and then stored in the AWS S3.

We will begin by creating an account in X(ex Twitter) then go to [Twitter Developper Portal](https://developer.x.com/en/portal/dashboard)
in order to create our project and apps.

After creating the app we will need to save these keys locally in a secure folder :
- **API key**
- **API key Secret**
- **Access Token**
- **Access Token Secret**

**Tuto**

The difference between the 4 concepts:
- API Key and API Key Secret
  Purpose: To authenticate the application.
  Usage: For the application's global requests to the API.

-Access Token and Access Token Secret:
  Purpose: To authenticate the user.
  Usage: For requests that require user permissions (such as reading or writing tweets).

-Example of Use
When you make a request to the Twitter API:

- Application Authentication:

Use the API Key and API Key Secret to authenticate your application.
User Authentication:

Use the Access Token and Access Token Secret to authenticate the user and access their data and permissions.


Then we will be installing our packages using the prompt command in Windows :

```
pip3 install pandas
pip3 install tweepy
pip3 install s3fs
```

#### Creating a virtual environment 

We will proceed instead by creating a virtual environment.

1. Creating a virtual environment
```
python -m venv myenv
```
2. Then we will activate the VE
```
myenv\Scripts\activate  # On Windows
source myenv/bin/activate  # On macOS/Linux
```

3. Finally installing the required packages
```
pip3 install pandas
pip3 install tweepy
pip3 install s3fs
```

4. Launching the Python script
```
python twitter-ETL.py
```

After searching the new updates of the Twitter API, with the free version of X Developer we have a limited requies that we can make.

### Updates of the Project

During the project developpement, we've met a 'problem' related to limited queries access with the Free access Twitter API.

So we've downloaded trump tweets from this website [Twitter Dataset](https://data.world/lovesdata/trump-tweets-5-4-09-12-5-16).
And now we're gonna develop the pipeline based on these data.

#### Creating AWS EC2 instance
We're going to create an EC2 instance in order to Launch Airflow on it.

We are going to create an IAM User that (we're not gonna be working with the Root account).
EC2 Config:
- Amazon Machine Image : Amazon Linux 2 AMI(HVM).
- Instance Type : t2.micro.
- Security Group: Allowing SSH traffic, HTTP traffic.
- Key Pair : Creating a new key pair RSA (.pem).

Then we move on the directory where our Key Pair is downloaded and we execute the following command:

```
ssh -v -i "C:\Users\UserName\..\Twitter-data-pipeline-key-pair.pem" ec2-user@your-ec2-public-ip

```

Remark: we can get a connection timed out when launching this command, if we obtain that problem we will need to verify our EC2 instance Public IP and the Inbound rules of our security group.

#### Installing Apache Airflow

##### Step 1: First, update the packages installed on your EC2 instance. 
```
sudo yum update -y
```

##### Step 2: Install Python 3, pip and other necessary tools.
```
sudo yum install -y python3 python3-pip
sudo yum install -y git
```

##### Step 3:  Install Apache Airflow
```
pip3 install apache-airflow
pip3 install apache-airflow-providers-amazon
pip3 install boto3
pip3 install pandas
```

#### Step 4: launching Airflow 
```
airflow standalone      
```




