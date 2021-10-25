import requests

param ={'name':'HGR','email':'hanamanatste@gmail.com','number':'9+199868328434'}
# headerdata = {'T1':'First_Headers','T2':'Second_Header'}
response = requests.get("http://httpbin.org/get",params=param)
print(response.text)
print(response.status_code)

