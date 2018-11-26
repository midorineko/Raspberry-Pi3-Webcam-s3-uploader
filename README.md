# Raspberry-Pi3-Webcam-s3-uploader
Upload a photo to s3 every x seconds using a webcam.

Install the python libraries [datetime, boto3, os] using 

```sudo pip install [library]```

Setup AWSCLI, which is how we will get the AWS credentials to post to your bucket.

run ```sudo pip install awscli```

run ```AWS configure```

set ```AWS access key```

set ```AWS secret key```

set ```region (us-east-1)```

set ```output format (json)```


Update the ```localPhotoName, bucketName, and s3SaveName```.

Currently images are saved in the same directory as 'lot.jpg', they override each other locally, but save to s3 with name + date 

and time and do not overwrite. 

