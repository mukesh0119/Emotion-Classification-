import requests

# Endpoint URL
url = 'http://localhost:5000/predict'

# Create a JSON payload with the text input
payload = {'text': 'I feel excited about the upcoming event!'}

try:
    # Send a POST request to the endpoint
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print('Error:', response.text)

except requests.exceptions.RequestException as e:
    print('Error:', e)
