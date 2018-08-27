from datetime import datetime
import json

import boto3
from botocore.exceptions import ClientError

def get_secret_key(secret_name, secret_key, region):
    endpoint_url = f'https://secretsmanager.{region}.amazonaws.com'

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region,
        endpoint_url=endpoint_url
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        secret = json.loads(get_secret_value_response['SecretString'])
        return secret[secret_key]
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)

class DynamoDB(object):

    def __init__(self, table_name):
        self.table_name = table_name
        self.table = self.connect()


    def connect(self):
        if self.table_name == 'LOCAL':
            dynamodb = boto3.resource('dynamodb',
                aws_access_key_id="anything",
                aws_secret_access_key="anything",
                endpoint_url='http://localhost:8000')
            table = dynamodb.Table(self.table_name)
            return table
        else:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(self.table_name)
            return table

    def get_user(self, email):
        response = self.table.get_item(
            Key={
                'email': email
            }
        )
        return response.get('Item', None)


    def create_user(self, email, password):
        response = self.table.put_item(
            Item={
                'email': email,
                'password': password
            },
            ConditionExpression='attribute_not_exists(email)'
        )
        return response

    def save_lifting_info(self, email, msq, mbe, mdl, program):
        maxes = {
            'squat': msq,
            'press': mbe,
            'dead': mdl
        }
        saved_routine = {
            'created': datetime.utcnow(),
            'workout': program
        }
        response = self.table.put_item(
            Item={
                'email': email,
                'maxes': maxes,
                'routine': saved_routine
            }
        )
        return response
