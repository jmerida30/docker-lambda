import json
import requests


def handler(event, context):
    return {
        'headers': {'Content-Type': 'application/json'},
        'statusCode': 200,
        'body': json.dumps({
            "message": "Hello Vana!",
            "event": event
        })
    }
