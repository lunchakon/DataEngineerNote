
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
