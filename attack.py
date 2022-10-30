import requests
for i in range(1,100):
    URL= f"http://ec2-3-111-8-121.ap-south-1.compute.amazonaws.com/api/get-provile?id={i}"
    r=requests.get(url=URL)
    if r.status_code==250:
        print(URL)
