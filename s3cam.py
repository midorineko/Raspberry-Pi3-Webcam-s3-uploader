#!/usr/bin/env python
from datetime import datetime
from time import sleep
import datetime
import os
import boto3

sleep(2)

# endlessly capture images awwyiss
while True:
    # Build filename string
    localPhotoName = "lot.jpg"
    
    os.system('fswebcam -r 1280x720 '+localPhotoName)

    bucketName = "iot-lot-photos"
    s3SaveName = "lot_{}.jpg".format(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
    s3 = boto3.client('s3')
    s3.upload_file(localPhotoName,bucketName,s3SaveName)

        
    # sleep
    sleep(60)
