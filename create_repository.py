import requests
import sys

def create_repository(api_url, repository_name, username, password):
    # Check if the repository exists
    response = requests.head(f"{api_url}/{repository_name}", auth=(username, password))
    if response.status_code == 404:
        # Repository does not exist, create it
        repository_data = {
            "rclass": "local",  # You can change this to 'remote' or 'virtual' based on your requirements
            "packageType": "maven",  # Specify the package type
            "repoLayoutRef": "maven-2-default",
            "description": "My repository description",
            # Add other necessary parameters as needed
        }
        create_response = requests.post(f"{api_url}/{repository_name}", json=repository_data, auth=(username, password))
        if create_response.status_code == 201:
            print(f"Repository created: {repository_name}")
        else:
            print(f"Failed to create repository: {create_response.text}")
            sys.exit(1)
    elif response.status_code == 200:
        print(f"Repository already exists: {repository_name}")
    else:
        print(f"Failed to check repository existence. HTTP response code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python create_repository.py <api_url> <repository_name> <username> <password>")
        sys.exit(1)

    api_url = sys.argv[1]
    repository_name = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    create_repository(api_url, repository_name, username, password)
