import json
import boto3
import zipfile


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    s3.download_file('tomessa.cdk.config', 'mail.zip', './mail.zip')
    with zipfile.ZipFile('./mail.zip', 'r') as zip_ref:
        zip_ref.extractall('./mail')
        print("unzippped")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from dtsarting!')
    }

