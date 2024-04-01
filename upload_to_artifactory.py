import requests
import sys

def upload_to_artifactory(file_path, upload_url, username, password):
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, data=file, auth=(username, password))
        if response.status_code == 201:
            print(f"WAR file uploaded successfully to Artifactory: {upload_url}")
        else:
            print(f"Failed to upload WAR file to Artifactory. Status code: {response.status_code}")
            print(response.text)
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python upload_to_artifactory.py <file_path> <upload_url> <username> <password>")
        sys.exit(1)

    file_path = sys.argv[1]
    upload_url = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    upload_to_artifactory(file_path, upload_url, username, password)
