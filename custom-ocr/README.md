pip install requirements...
# this is how
cd src
python -u "c:\nav\gith\custom-ocr\src\main.py" -m poll




# gcp
gcp account on mrevanishere@gmail.com


https://cloud.google.com/vision/docs/ocr#vision_text_detection_gcs-python

-> three dots -> Billing Account Management

https://console.cloud.google.com/billing/





to test, screenshot then run:
cd \nav\gith\jp-card-gen\custom-ocr\src\
python -u "main.py" -m test


to run main:
cd \nav\gith\jp-card-gen\custom-ocr\src
python -u "main.py" -m main -i "file/img.jpg" -o ".\file\imgjpg.txt"


if DefaultCredentialsError:
    try main and see if env variables are there,
    need to be IN THE DIR since python checks relative files to the working dir
    so need to cd into it first...

# Account Management
https://cloud.google.com/vision/pricing
Note: price per 1000 lookups
- first 1k is FREE
- $1.50 per 1k lookups

Billing
Quotas
APIs & Services -> 
    Enabled APIs & services -> 
        Cloud Vision API -> 
            google.cloud.vision.v1.ImageAnnotator.BatchAnnotateImages	
        for safety disable everything except Cloud Vision API 


