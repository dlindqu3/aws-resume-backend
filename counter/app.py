import json

# import requests
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'Counter'
counter_table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """    
    try:
        my_count = 0
    
        return {
            "statusCode": 200,
            "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "GET" 
            },
            "body": json.dumps({
                "message": "res from lambda",
                "newCount": my_count
            }),
        }
    
    except Exception as e: 
        return {
            "statusCode": 500,
            "body": {
                "event": event,
                "exception": e
            }
        }