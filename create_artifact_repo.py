import requests
import sys

def create_artifact_repo(base_url, repo_name, repo_type, username, password):
    url = f"{base_url}/artifactory/api/repositories/{repo_name}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "rclass": repo_type
    }
    # Authenticate using username and password
    auth = (username, password)
    response = requests.put(url, json=data, headers=headers, auth=auth)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully")
    else:
        print(f"Failed to create repository '{repo_name}'. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python create_artifact_repo.py <base_url> <repo_name> <repo_type> <username> <password>")
        sys.exit(1)

    base_url = sys.argv[1]
    repo_name = sys.argv[2]
    repo_type = sys.argv[3]
    username = sys.argv[4]
    password = sys.argv[5]
    create_artifact_repo(base_url, repo_name, repo_type, username, password)
 
