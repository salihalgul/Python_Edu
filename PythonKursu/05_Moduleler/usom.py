import requests 
response=requests.get("https://usom.gov.tr/url-list.txt",verify=False)
dosya=open("usom.txt","w")
dosya.write(str(response.content))
dosya.close()