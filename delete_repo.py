import requests

# Variable used for authentication through users' github token
headers = {
    'Authorization': 'token xxxxx'
}
repo = 'test_api'

# Variable containing the delete request that will delete a repo
login = requests.delete('https://api.github.com/repos/Lamia7/' + repo, headers=headers, timeout=3)

print(login.text)
