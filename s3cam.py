#!/usr/bin/env python
from datetime import datetime
from time import sleep
import datetime
import os
import tinys3
import yaml

sleep(2)

# endlessly capture images awwyiss
while True:
    # Build filename string
    filepath = "~/Desktop/s3-cam/lot_{}.jpeg".format(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
    
    os.system('fswebcam '+filepath)

    # Upload to S3
    conn = tinys3.Connection("aws access key", "aws secret key")
    f = open(filepath, 'rb')
    conn.upload(filepath, f, "bucketname",
               headers={
               'x-amz-meta-cache-control': 'max-age=60'
               })
    
    
    AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXX'
    AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXXXXX'

    s3_connection = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    bucket = s3_connection.get_bucket('iot-lot-photos')
    key = boto.s3.key.Key(bucket, filepath)
    with open(filepath) as f:
        key.send_file(f)

    # sleep
    sleep(60)
