# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_latest_email_subject_and_sender(k=10):
	"""Shows basic usage of the Gmail API.
	Lists the user's Gmail labels.
	"""
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists("token.json"):
		creds = Credentials.from_authorized_user_file("token.json", SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
					"credentials.json", SCOPES
			)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open("token.json", "w") as token:
			token.write(creds.to_json())

	response = []
	# Call the Gmail API
	service = build("gmail", "v1", credentials=creds)
	results = service.users().messages().list(userId="me").execute()
	messages = results.get("messages", [])
	# iterate through all the messages 
	for msg in messages[:min(len(messages), k)]: 
		# Get the message from its id 
		txt = service.users().messages().get(userId='me', id=msg['id']).execute() 
		payload = txt['payload'] 
		headers = payload['headers'] 

		# Look for Subject and Sender Email in the headers 
		for d in headers: 
				if d['name'] == 'Subject': 
						subject = d['value'] 
				if d['name'] == 'From': 
						sender = d['value'] 
		response.append((subject, sender))
	return response

def funcs():
	functions = [
			{
			"name": "get_latest_email_subject_and_sender",
			"description": "Gets latest emails from gmail - only subject and sender",
			"parameters": {
				"type": "object",
				"properties": {
					"k": {
						"type": "integer",
						"description": "Number of emails to return",
					},
				},
				"required": [],
			},
		}
	]
	return functions
