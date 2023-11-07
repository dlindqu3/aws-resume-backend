import json

# import requests
import boto3

dynamodb = boto3.resource('dynamodb')
table1 = dynamodb.Table("MyCounterTable")


def lambda_handler(event, context):
    ## this line added to test GitHub Actions with SAM build / deploy & tests 

    count = 0

    print("lambda called")

    try: 
        res = table1.get_item(Key={ "id": str(1) })
        print("res from get item:", res)
        # print("item from res: ", res["Item"])

        new_count = res["Item"]["count"] + 1

        res2 = table1.put_item(
                Item={
                    "id": str(1),
                    "count": new_count
                }
            )
        print("res2 after update: ", res2) 

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers" : "Content-Type",
                "Access-Control-Allow-Origin": "*",  
                "Access-Control-Allow-Methods": "GET" 
            },
            "body": json.dumps({
                # "newCount": str(new_count)
                "newCount": "-5"
            }),
        }
    
    except Exception as e: 
        print(str(e))
        return {
            "statusCode": 500,
            "body": {
                "event": event,
                "exception": str(e)
            }
        }