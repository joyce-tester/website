import requests

# Replace with your API key
api_key = "AIzaSyDh0IAmD1lkEcdPZXkT1yTMrkMalpakmhM"

# URL for the Gemini API
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

# Headers and payload
headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Explain how AI works"}
            ]
        }
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
if response.status_code == 200:
    print("Response:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
