import boto3

def handler(event, context):
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name='us-east-1'
    )

    src_bucket = 's3-start'
    dst_bucket = 's3-finish'

    for record in event['Records']:
        key = record['s3']['object']['key']
        copy_source = {'Bucket': src_bucket, 'Key': key}
        print(f"Copying {key} from {src_bucket} to {dst_bucket}")
        s3.copy_object(Bucket=dst_bucket, CopySource=copy_source, Key=key)
