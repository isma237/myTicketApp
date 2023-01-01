import json
import boto3
import uuid

# import requests
from botocore.exceptions import ClientError
import logging

dynamodb = boto3.resource('dynamodb')
ticket = dynamodb.Table('myTicketTable')
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    try:
        request = json.loads(event['body'])
        print(request)
        response = ticket.put_item(
            Item={
                "Id": str(uuid.uuid4()),
                "title": request.get('title'),
                "content": request.get('content'),
                "category": request.get('category')
            })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "New Ticket created!",
                "data": response
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
