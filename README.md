# GitHub Issue Email Grabber

This Python script allows you to retrieve the email address of a user who filed an issue in a public GitHub repository.

## Prerequisites

Before running the script, make sure you have the following set up:

1. **Install Requests:** You'll need the `requests` library to interact with the GitHub API. You can install it using `pip`:

   ```bash
   pip install requests


**GitHub Token:** Obtain a GitHub personal access token with the necessary permissions to access the repository and user information.


## Usage

1. Clone this repository or download the Python script.
2. Replace `'YOUR_GITHUB_TOKEN'` in the script with your actual GitHub token.
3. Customize the `REPO_OWNER` and `REPO_NAME` variables to match the repository you're interested in.
4. Run the script using Python:

   ```bash
   python get_issue_email.py

