import json

# import requests
import boto3

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table("aws-resume-stack-CounterTable-1A5PBB6IXPXTO")


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "GET" 
        },
        "body": json.dumps({
            "message": "res from lambda",
            "newCount": 0
        }),
    }
    # try: 
    #     res = table.get_item(Key={ "isMainItem": True })
    #     ##  if res contains an Item, put_item with current count + 1
    #     if res["Item"]: 
    #         return {
    #         "statusCode": 200,
    #         "headers": {
    #         "Access-Control-Allow-Headers" : "Content-Type",
    #         "Access-Control-Allow-Origin": "*",  
    #         "Access-Control-Allow-Methods": "GET" 
    #         },
    #         "body": json.dumps({
    #             "message": "res from lambda get_item",
    #             "res": res
    #         }),
    #     }
    #     ## else if res contains NO Item, put_item with count = 0 
    #     else: 
    #         table.put_item(
    #             Item={
    #                 "isMainItem": True,
    #                 "count": 0
    #             }
    #         )       
    #         return {
    #             "statusCode": 200,
    #             "headers": {
    #                 "Access-Control-Allow-Headers" : "Content-Type",
    #                 "Access-Control-Allow-Origin": "*",  
    #                 "Access-Control-Allow-Methods": "GET" 
    #             },
    #             "body": json.dumps({
    #                 "message": "res from lambda",
    #                 "newCount": 0
    #             }),
    #         }
    
    # except Exception as e: 
    #     return {
    #         "statusCode": 500,
    #         "body": {
    #             "event": event,
    #             "exception": e
    #         }
    #     }