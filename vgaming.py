import boto3
import os
from botocore import UNSIGNED
from botocore.client import Config


def download(client, bucket: str, prefix: str):
    objects = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
    path = os.path.join(os.getcwd(), bucket)
    try:
        os.mkdir(path)
    except:
        pass

    for _ in objects.get('Contents'):
        filename, filesize = _.get('Key'), _.get('Size')
        if filename != '' and filesize > 0:
            print(f'> copy {filename} to {path}')
            try:
                os.mkdir(os.path.join(path, prefix))
            except:
                pass
            client.download_file(BUCKET, filename, os.path.join(path, filename))
        else:
            print(f'> skip {filename}')


if __name__ == '__main__':
    BUCKET, KEY_PREFIX, REGION = 'nvidia-gaming', 'windows/latest', 'us-east-1'

    client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    prefixes = ['windows/', 'linux/']

    for prefix in prefixes:
        download(client, BUCKET, prefix)
