# AWS Lambda Functions as Docker Containers

## Overview
Given the scenario where we need to add packages or files that overpass the space limit for code stablished by AWS then an alternative that lifts this limit is to containerize the function using Docker and pushing it to ECR and then deploying it as an image in Lambda Function service. 

To Dockerize a Lambda Function it is necessary first to have the code that is going to handle each request, this code can be written in any of the supported languages in Lambda Functions. For this research and first implementation we use **Python 3.8** have three files, `handler.py` with the functinoality, `requirements.txt` with the packages that we'll need, and `Dockerfile` to build the container and run the preparation commands.  

## Github repository with the files used on this research.
- https://github.com/jmerida30/docker-lambda.git

**NOTE:** In the `Dockerfile`, the `FROM` statement has been looked up in https://gallery.ecr.aws/lambda/python where we selected the Image Tag correspondig to Python version 3.8.

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

## Hello Vana! - Practical Steps
## ECR
- Once the repository is cloned, we need to log in into the AWS console and go into the Elastic Container Registry (ECR) service. 
- This that will bring us to a page where we can configure our container image.
- Here we (can) set our image as private and give this repository a name (for this example we named it **hello-vana**). 
- Create repository.
- Once the repository is created we can go in *ECR > Repositories > hello-vana*.
- On the right up corner go in "View push commands" and this will bring us to this page
![](images/push-commands.png)
- Follow this steps and it will push the image into our **hello-vana** repository.

**NOTE:** On Linux it is possible to get an error pushing the image 'Error saving credentials', to solve this error we just need to run `sudo apt-get install gnupg2 pass`. Also it may be necessary to run each command with `sudo`.
- With this steps completed we already have an image on our repository ready to be deployed as a Lambda Function.

![](images/repository-images.png)

## Lambda Function
On the Lambda Functions page go into **Create function**
- Select **Container image**
- Give a name to the function (for this example we named it **hello-vana**).'
- Browse images.
- On the field "Amazon ECR image repository" select **hello-vana**.
- This will list all the images pushed into the repository, select the desired Image tag (in our case it is **latest**).

![](images/select-container-iamge.png)

- On **Permissions** select any role that can allow this Lambda to write logs into **CloudWatch**.
- On this same page, inside "Container image overrides" you can add configuration such as the _working directory_, this will override the `Dockerfile` configuration, in this case we left it empty.
- Create function.

## Make it accessible 
*This step was ommitted on the example.*

On the Lambda Function control panel for **hello-vana** go into the configuration tab.
- Add a trigger.
- API Gateway.
- Create an API.
- HTTP API.
- Add security.
- Add additional settings.
- Add.

With all this steps completed the Lambda Functino should be ready to run.
