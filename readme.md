# FaaS Tutorial

This repository introduces four tasks to learn how to work with FaaS, at the moment on AWS Lambda. It covers tutorial for developing your first Python AWS Lambda function, how to use BaaS (Backend-as-a-Service) services AWS S3 and AWS Rekognition in AWS Lambda, and how to automatize deployment of a function using Terraform and GitHub Actions.

Each task has a starting point code example in the folder *Initial*, while one possible solution can be found in the folder *Final*. The complete description of the task is given in the readme file in the respective folder of the task.

## Brief description of tasks

### Task 1 - Develop a simple AWS Lambda function

This task is some kind of a "Hello World" task to introduce into FaaS basics, covering all necessary steps how to develop your first function, including reading the data input and returning the data output.

### Task 2 - Develop an AWS Lambda function for object recognition

This task introduces how to use AWS BaaS services S3 and AWS Rekognition. In particular, how to crop faces from an image that is stored on AWS S3 storage and store them back to S3 as separated images.

### Task 3 - Deploy a Lambda function with Terraform

This task introduces how to code your infrastructure (in this case your Lambda function) and deploy it with Terraform. You can use the function that you developed in Task 3. For this purpose, you would need to have deployed a layer.

### Task 4 - Automatize the deployment of a Lambda function with GitHub Actions and Terraform

With this task you will learn how to create a workflow with GitHub Actions on your GitHub repository in order to automatize the deployment of the function on each commit. 
In the background, you will use the Terraform script that you developed in Task 3.


## Contribution

- Sashko Ristov
- Serafin Plattner 

