
## Requests library:

Requests is an external library you'll need to install using pip install requests.
It simplifies making HTTP requests (like GET, POST) to access and interact with APIs.

## Choose the HTTP method:

GET: Used to retrieve data from the API (common for reading data).

POST: Used to send data to the API (common for creating or updating data).

PUT/PATCH: Similar to POST for updating data (specific update methods).

DELETE: Used to delete data from the API.

    import requests
    response = requests.get(API_URL)  # Replace with actual API URL

## Handle the response:

Check the status code using response.status_code. Common codes:

    200: Success
    400: Bad request (incorrect data format)
    401: Unauthorized (requires authentication)
    404: Not found (requested resource doesn't exist)

Access the response data using response.text for plain text or response.json() for JSON data (common format).


## Example (Public API for Date Jokes)
    
    import requests
    
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}  # Optional header for JSON data
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
      data = response.json()
      joke = data["joke"]
      print(joke)
    else:
      print("Error:", response.status_code)
