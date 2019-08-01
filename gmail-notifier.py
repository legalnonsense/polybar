# -*- coding: utf-8 -*-

# Importing required libraries
from googleapiclient import discovery
from googleapiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import time
import os

# Creating a storage.JSON file with authentication details
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage(os.path.expanduser('~/.config/i3/py3status/token.json'))
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(os.path.expanduser('~/.config/i3/py3status/credentials.json'), SCOPES)
    creds = tools.run_flow(flow, store)
    
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))


def check_mail():

    qx=GMAIL.users().messages().list(userId='me', q='category:primary in:inbox is:unread').execute()
    number = qx['resultSizeEstimate']

    print(number)


while True:
    check_mail()
    time.sleep(10)
