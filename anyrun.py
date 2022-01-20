import requests
import json
import time

File = input("Enter File name: ")
headers = {
    'Authorization': 'API-Key ', # Enter your API key here
}

files = {
    'file': (File, open(File, 'rb')),
    'env_os': (None, 'windows'),
    'env_bitness': (None, '64'),
    'env_version': (None, '10'),
}

response = requests.post('https://api.any.run/v1/analysis', headers=headers, files=files)
parsed = json.loads(response.content)
data1 = (parsed["data"])
taskid = (data1["taskid"])
print("File uploaded & your taskid is : " + taskid)
print("Please wait ...")
time.sleep(100)
getresults = requests.get('https://api.any.run/report/' + taskid +'/summary/html', headers=headers)
with open(taskid +'.html', 'w') as file:
    file.write(getresults.text)
