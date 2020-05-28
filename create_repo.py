import json

import requests


headers = {
    'Authorization': 'token xxx'
}
repo = 'my_repo_name'
description = 'My repo description'

# Payload is the json content that we want to send
payload = {'name': repo, 'description': description, 'auto-init': 'true'}
# This is a post request that will create a repo
login = requests.post('https://api.github.com/user/repos', headers=headers, timeout=3, data=json.dumps(payload))

print(login.text)
