import json
import logging

# import requests
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    record = event['Records'][0]['dynamodb']['NewImage']

    types = [
        {
            'type': 'Logiciel',
            'owner': 'ismael.gadji@orange.com'
        },
        {
            'type': 'Materiel',
            'owner': 'ismaelgadji@gmail.com'
        },
    ]

    request_type = record['type']['S']
    message = record['content']['S']
    responsable = None
    for task in types:
        if task['type'] == request_type:
            responsable = task['owner']
            break

    if responsable is not None:
        logger.info(f"Send email to {responsable}")

        try:
            client = boto3.client('ses')
            response = client.send_email(Source='ismaelgadji@gmail.com',
                              Destination={
                                  'ToAddresses': [responsable],
                                  'CcAddresses': [],
                                  'BccAddresses': []
                              },
                              Message={
                                  'Subject': {
                                      'Data': 'Myticket - Nouvelle demande',
                                      'Charset': 'utf-8'
                                  },
                                  'Body': {
                                      'Text': {
                                          'Data': f'Vous avez une nouvelle demande à traiter. \nDétails: {message}',
                                          'Charset': 'utf-8'
                                      }
                                  }
                              }
                            )
            return response
        except Exception as error:
            logger.error(error)
    else:
        logger.error("impossible de trouver le responsable de la tache")
        return

