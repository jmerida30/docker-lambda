# AWS Lambda Functions as Docker Containers

## Overview
Given the scenario where we need to add packages or files that overpass the space limit for code stablished by AWS then an alternative that lifts this limit is to containerize the function using Docker and pushing it to ECR and then deploying it as an image in Lambda Function service. 

To Dockerize a Lambda Function it is necessary first to have the code that is going to handle each request, this code can be written in any of the supported languages in Lambda Functions. For this research and first implementation we use **Python 3.8** have three files, `handler.py` with the functinoality, `requirements.txt` with the packages that we'll need, and `Dockerfile` to build the container and run the preparation commands.  

## Hello Vana! - Github repository with the files used to this research.
- https://github.com/jmerida30/docker-lambda.git

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

## Practical Steps


## 3. Push it to ECR (Elastic Container Registry)
Push it

## 4. Deploy to AWS Lambda Function
Deploy it 

