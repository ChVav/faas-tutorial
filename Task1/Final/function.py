def lambda_handler(event, context):
    a = event['a']
    b = event['b']
    result = a + b
    return {
        'statusCode': 200,
        'result': result
    }