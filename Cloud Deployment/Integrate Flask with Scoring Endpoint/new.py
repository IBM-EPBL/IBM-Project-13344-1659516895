import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "DbnVb60NWCN5h5qNhluA4fBGkhD6DPJrwonUoPuAarfJ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["year1","year2","year3","year4","year5","year6","year7","year8","year9","year10"]], "values": [[0.43,0.44,0.45,0.44,0.46,0.47,0.46,0.48,0.49,0.50]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/bf470391-47f6-4850-a9ee-324df4a39f3e/predictions?version=2022-11-15', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print(response_scoring.json())