import json
import logging
# import requests

logger = logging.getLogger(__name__)

def lambda_handler(event, context):

    logger.info("Premier test")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
