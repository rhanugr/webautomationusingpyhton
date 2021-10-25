import requests

#Created a Dictonariescls
headerdata = {'T1':'First_Headers','T2':'Second_Header'}
response = requests.get("http://httpbin.org/get",headers=headerdata)
print(response.text)