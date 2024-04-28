import requests
import sys

access_token = sys.argv[1]
user_id = sys.argv[2]
posting_file = sys.argv[3]

posting_content = open(posting_file).read()

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept-Charset": "utf-8"
}

data = {
    "title": posting_file.split('.')[0],
    "contentFormat": "markdown",
    "content": posting_content,
    "publishStatus": "draft",
}

response = requests.post(f'https://api.medium.com/v1/users/{user_id}/posts', json=data, headers=headers)
print(response.json())
