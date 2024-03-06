import subprocess
import requests


## CREATE FREE API KEY
# https://platform.openai.com/api-keys


def get_last_command_output():
    # Get last command from history
    history_command = "tail -1 ~/.bash_history"
    last_command = subprocess.getoutput(history_command)

    last_command_output = subprocess.getoutput(last_command)
    return last_command_output

def analyse_with_oracle(command_output):
    api_url = "https://api.theoracle.com/analyse"
    api_key = "your_api_key_here"  # Consider retrieving this from an environment variable for security
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "command_output": command_output
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        
        # Assuming the API returns JSON with a field "suggestion"
        suggestion = response.json().get("suggestion", "I couldn't find any suggestions for you.")
        return f"Hmmm, I took a look at that and I think... {suggestion}"
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't analyse that due to an error: {e}"

def main():
    last_output = get_last_command_output()
    suggestion = analyse_with_oracle(last_output)
    print(suggestion)


if __name__ == "__main__":
    main()