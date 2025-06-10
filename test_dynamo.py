import boto3
from boto3.dynamodb.conditions import Key

# Use the local endpoint
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test',
)

table = dynamodb.Table('Vehicles')

# 1) List tables is implicit by having table object
print("Table name:", table.table_name)

# 2) Insert a sample item
print("Putting item...")
table.put_item(Item={'vin': '1HGBH41JXMN109186', 'make': 'Honda'})

# 3) Query it back
print("Getting item...")
response = table.query(
    KeyConditionExpression=Key('vin').eq('1HGBH41JXMN109186')
)
print("Query result:", response['Items'])
