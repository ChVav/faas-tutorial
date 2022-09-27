# Task 1: Develop a simple AWS Lambda function 

In this task you will learn how to develop a simple AWS Lambda function that receives two numbers and returns their sum.

Note that in general, a function needs to read the input data, which is in JSON format, execute the code, and return output data, also in JSON format.

## Prerequisites

- AWS account with access to AWS Management Console


## Steps

Follow these steps:

- Select the AWS Lambda service
- Select the region if you do not want to use the default one AWS North Virginia ($us-east-1$)
- create function 
    - write a name
    - select runtime (Python)
- configure the function (if needed) with 
    - Memory
    - Timeout
- write your code
    - read the data inputs
    - write the code to sum two numbers
    - return the output 
- deploy your function
- test your function with the JSON from *input.json*

## Notes 

The handler in the runtime settings is *lambda_function.lambda_handler*, which specifies which method to be called when the function is invoked.

## Hints

If you need help, see one possible solution in the folder *Final*

