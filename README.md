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



