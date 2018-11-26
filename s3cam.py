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

    # sleep
    sleep(60)
