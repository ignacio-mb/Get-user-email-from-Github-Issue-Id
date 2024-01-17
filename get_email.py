import requests

GITHUB_TOKEN = 'YOUR_TOKEN'
REPO_OWNER = 'metabase'
REPO_NAME = 'metabase'

def get_email_of_issue_creator(issue_number):
    issue_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}'

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
    }

    response = requests.get(issue_url, headers=headers)

    if response.status_code == 200:
        issue_data = response.json()
        user_login = issue_data['user']['login']

        # Now, get the user's email address
        user_url = f'https://api.github.com/users/{user_login}'
        user_response = requests.get(user_url, headers=headers)

        if user_response.status_code == 200:
            user_data = user_response.json()
            email = user_data.get('email')
            if email:
                return email
            else:
                return f"Email not available for user: {user_login}"
        else:
            return f"Failed to fetch user data for {user_login}"
    else:
        return f"Failed to fetch issue data for issue {issue_number}"

if __name__ == "__main__":
    issue_number = input("Enter the issue number: ")
    email = get_email_of_issue_creator(issue_number)
    print(f"Email of the issue creator: {email}")
