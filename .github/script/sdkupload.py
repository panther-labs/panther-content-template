import os
import sys
import json
import base64
import requests

# Replace this with PAT command once it's available

with open('.panther/panther-sdk-cache') as f:
    contents = f.read()

    query = 'mutation SDKUpload(){ uploadDetectionEntities(input:{data:"'
    query += base64.b64encode(contents.encode('utf-8')).decode('utf-8')
    query += '", mode: PANTHER_SDK}) { rules { modified new total } queries { modified new total } } }'

    req = {'operationName': 'SDKUpload', 'query': query}

    resp = requests.post(
        os.environ["API_ENDPOINT"],
        json=req,
        headers={"X-API-Key": os.environ["API_TOKEN"]},
    )

    if resp.status_code != 200:
        print("RESPONSE CODE:", resp.status_code)
        sys.exit(1)

    print("RESPONSE BODY:", resp.json())

    resp_data = json.loads(resp.text)
    if resp_data.get('errors', None) is not None:
        sys.exit(1)
