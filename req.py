import requests

payload = {
    'amount': 300000,
    'machineIdentifier': '03f0b542-67e3-4f98-aaff-3df08a9b62e0'
}

headers = {
    "Content-Type": "application/json",
    "Subscription-Key": "2d290a4fa71a48b4a1086eae98aa3798"
}

r = requests.post('https://ipn-dev.qrsoundboxnepal.com/api/v1/notify', json=payload, headers=headers)
print(r.text)


# import requests  # Import the requests library to make HTTP requests
# import time      # Import the time module to use the sleep function

# # Define the base payload (data) that will be sent in the POST request
# payload = {
#     'amount':None,  # Initially set to None, will be updated in the loop
#     'machineIdentifier': '03f0b542-67e3-4f98-aaff-3df08a9b62e0'  # Unique identifier for the machine
# }

# # Define the headers for the HTTP request, specifying the content type and subscription key
# headers = {
#     "Content-Type": "application/json",  # Indicate that the payload is in JSON format
#     "Subscription-Key": "2d290a4fa71a48b4a1086eae98aa3798"  # API key used for authentication
# }

# # List of different amounts to send in each request
# amounts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# # Loop through the list of amounts and send a request for each
# for amount in amounts:
#     payload['amount'] = amount  # Update the 'amount' in the payload for each iteration
#     # Send the POST request to the specified URL with the current payload and headers
#     r = requests.post('https://ipn-dev.qrsoundboxnepal.com/api/v1/notify', json=payload, headers=headers)
#     # Print the response text for the current request, indicating the amount sent
#     print(f"Response for amount {amount}: {r.text}")
#     # Pause for 1 second before sending the next request
#     time.sleep(1)
