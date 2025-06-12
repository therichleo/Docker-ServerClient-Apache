import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://192.168.92.129:8080/')

print("Status:", response.status)
print("Response data:", response.data.decode('utf-8'))