#not working 17-august02021
#
# source: https://www.youtube.com/watch?v=H_rRlnSw_5s&t=37s
# https://stackoverflow.com/questions/48286217/simplest-lambda-function-to-copy-a-file-from-one-s3-bucket-to-another
# https://www.askvikram.com/copy-move-files-between-buckets-using-boto3/#copy-s3-object-to-another

import boto3
import urllib

def lambda_handler(event, context):
    """
    :event is the event that triggered the lambda function to be invoked
    :#1 first get bucket name
    """
    bucket = event['records'][0]['s3']['bucket']['name']
    """
    #2 get the file/key name
    """
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    client = boto3.client('s3')

    # create a source dictionary that specifies bucket name and key name of the object to be copied
    copy_source = {
        'Bucket': 'your_source_bucket_name',
        'Key': 'Object_Key_with_file_extension'}

















   try:
        """#3 fetch the file to the s3 source bucket """
        fetch = client.get_object(Bucket=bucket, Key=key)

        upload_file_bucket = "danish-tst-backup-bucket"
        upload_file_key = 'lambdabackup/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)


    except Exception as e:
        print(e)
        raise e


