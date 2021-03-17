mport requests
import json
import base64

def getHeader(client_id,client_secret):
    encoded=base64.b64encode("{}:{}".format(client_id,client_secret).encode("utf-8")).decode("ascii")
    header={"Authorization":"Basic {}".format(encoded)}
    return header

def getToken(client_id,client_secret):
    header=getHeader(client_id,client_secret)
    payload={"grant_type":"client_credentials"}
    endpoint="https://accounts.spotify.com/api/token"
    raw=requests.post(endpoint,headers=header,data=payload)
    
    if raw.status_code==400:
        raise ValueError("Error due to malforemd syntax")
    elif raw.status_code==409 or raw.status_code==200:
        if raw.status_code==409:
            retry=json.loads(raw.headers)['Retry-After']
            time.sleep(retry)
            raw=requests.get(endpoint,headers=header,data=payload)
        token=json.loads(raw.text)['access_token']
        return {"Authorization":"Bearer {}".format(token)}
