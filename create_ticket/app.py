import json
import boto3
import uuid

# import requests
from botocore.exceptions import ClientError
import logging
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('myTicketTable')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        request = json.loads(event['body'])
        now = datetime.now()
        ticket = {
            "title": request.get('title'),
            "content": request.get('content'),
            "category": request.get('category'),
            "type": request.get('type'),
            "priority": request.get('priority'),
            "owner_email": request.get('owner_email'),
            "terminated": False,
            "created_at": now.strftime("%m/%d/%Y, %H:%M:%S")
        }
        table.put_item(Item=ticket)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "New Ticket created!",
                "data": ticket
            })
        }
    except ClientError as err:
        logger.error(err)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Problem",
                "error": "Un probleme est survenu"
            })
        }
    except Exception as error:
        logger.error(error)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Problem",
                "error": "Un probleme est survenu"
            })
        }
