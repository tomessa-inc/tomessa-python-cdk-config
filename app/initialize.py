#import boto3
#import zipfile

#s3 = boto3.client('s3')

#match boo:
#    case "":
#        asdasdf
#    case "":
#        asasdfasdf
#    case "":
#        asasdfasdf



#objectNames = ['files']
#s3.download_file('tomessa.cdk.config', 'mail.zip', './mail.zip')


#with zipfile.ZipFile('./mail.zip', 'r') as zip_ref:
#    zip_ref.extractall('./mail')
#    print("unziipped")



#bucket = s3.bucket.get

#for bucket in s3.buckets.all():
 #   print(bucket.name)
import io
import json
import logging
import zipfile
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class LambdaWrapper:
    def __init__(self, lambda_client, iam_resource):
        self.lambda_client = lambda_client
        self.iam_resource = iam_resource


    def update_function_code(self, function_name, deployment_package):
        """
        Updates the code for a Lambda function by submitting a .zip archive that contains
        the code for the function.

        :param function_name: The name of the function to update.
        :param deployment_package: The function code to update, packaged as bytes in
                                   .zip format.
        :return: Data about the update, including the status.
        """
        try:
            response = self.lambda_client.update_function_code(
                FunctionName=function_name, ZipFile=deployment_package
            )
        except ClientError as err:
            logger.error(
                "Couldn't update function %s. Here's why: %s: %s",
                function_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response

test = LambdaWrapper();
