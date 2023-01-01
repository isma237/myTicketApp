import json
import logging

# import requests
import boto3


logger = logging.getLogger(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('myTicketTable')


def lambda_handler(event, context):
    logger.info("Nouvelle demande")
    try:
        query = event['queryStringParameters']
        data = table.get_item(Key={'Id': query.get('ticket_id')})
        print(data)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world",
                "data": data
            }),
        }
    except Exception as error:
        logger.error('Impossible de recuperer la fonnée %s', error.response['Error']['Message'])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Un probleme est survénu",
                "error": error
            }),
        }


