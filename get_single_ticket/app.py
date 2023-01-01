import json
import logging

# import requests
import boto3


logger = logging.getLogger()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('myTicketTable')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        query = event['queryStringParameters']
        response = table.get_item(Key={'Id': query.get('ticket_id')})
        logger.info(f"Data: {response['Item']}")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "data": response['Item']
            }),
        }
    except Exception as error:
        logger.error(f"Document non disponible: Id:  {query.get('ticket_id')}")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Document non disponible: Id:  {query.get('ticket_id')}",
            }),
        }


