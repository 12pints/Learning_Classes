# working august 2021
# this code will connect to an s3 bucket,
#
# it will check the working directory for python files and
# copy to an s3 bucket, create a directory, and copy the files over
# import environment variables, stored locally.
# source https://www.youtube.com/watch?v=dqkoBrgFSus

import os
import boto3


AWS_access_key = os.getenv('AWS_Python_access_key')
AWS_secret_access_key = os.getenv('AWS_Python_secret_access_key')

client = boto3.client('s3',
                      aws_access_key_id = AWS_access_key,
                      aws_secret_access_key = AWS_secret_access_key)

for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = "danish-tst-bucket"
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)


