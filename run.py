
import os

import boto3

from workoutgenerator import app

if __name__ == "__main__":
  # Configure for DynamoDB local
  client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
  tables = client.list_tables()
  # Create table if it doesn't exist
  if 'LOCAL' not in tables['TableNames'][0]:
    client.create_table(
      TableName='LOCAL',
      AttributeDefinitions=[
        {
          'AttributeName': 'email',
          'AttributeType': 'S'
        }
      ],
      KeySchema=[
        {
          'AttributeName': 'email',
          'KeyType': 'HASH'
        }
      ],
      ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
      }
    )  
  os.environ["ENV_REGION"] = "us-east-2"
  os.environ["USER_TABLE"] = "LOCAL"
  app.run(debug=True, host='127.0.0.1')
