import requests, json, time, sys

sys.tracebacklimit = 0

apiKey = 'API-Key ' # Enter your API key here

def checkUpload(taskID, count):
    getresults = requests.get(f'https://api.any.run/report/{taskID}/summary/html', headers=headers)

    if(getresults.status_code != 200):
        checkUpload(taskID, (count + 1))
    else:
        file = f'{taskID}.html'
        print('[COMPLETE]', 'Saving as file', file)
        with open(file, 'w') as file:
            file.write(getresults.text)

file = input("Enter File name: ")

headers, files = [{'Authorization': apiKey}, {
    'file': (file, open(file, 'rb')),
    'env_os': (None, 'windows'),
    'env_bitness': (None, '64'),
    'env_version': (None, '10'),
}]
    
response = requests.post('https://api.any.run/v1/analysis', headers=headers, files=files)
parsed = json.loads(response.content)

try:
    taskid = (parsed["data"]["taskid"])
except Exception as e:
    if(parsed['error']):
        print('[ERROR]', parsed['message'])
    else:
        print('[ERROR]', e)
    exit()

print("File uploaded & your taskid is:", taskid)
print('Please wait...')

checkUpload(taskid, 0)
