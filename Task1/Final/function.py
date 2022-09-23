def lambda_handler(event, context):

    # Read inputs of the function
    a = event['a']
    b = event['b']

    # Write the code of the function
    result = a + b

    # Return the output
    return {
        'result': result
    }