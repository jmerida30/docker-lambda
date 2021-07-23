# docker-lambda
Minimal files to Dockerize a Lambda Function written on Python and deploy it to AWS.

## Requirements
1. Docker (On Windows and MacOS Docker Desktop)
2. aws-cli

```console
sudo apt-get update
sudo apt-get install docker-compose
sudo apt-get awscli -y
```

## AWS Services
1. EC2 (Local Machine works fine with enough permissions.)
2. ECR
3. IAM
4. Lambda Functions
    - Also an AWS role to give this function CloudWatch access to write logs.  
5. API Gateway

## Intro
To Dockerize a Lambda Function it is necessary first to have the code that is going to handle each request, this code can be written in any of the supported languages in Lambda Functions. For this research and first implementation we use **Python 3.8** have three files, `handler.py` with the functinoality, `requirements.txt` with the packages that we'll need, and `Dockerfile` to build the container and run the preparation commands.  

## 2. Dockerize function
Dockerize it

## 3. Push it to ECR (Elastic Container Registry)
Push it

## 4. Deploy to AWS Lambda Function
Deploy it 
