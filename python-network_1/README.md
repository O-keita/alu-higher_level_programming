import urllib.request

url = https://alu-intranet.hbtn.io/status

with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')

    print(Body response:)
    print(t- type:, type(content))
    print(t- content:, content)

