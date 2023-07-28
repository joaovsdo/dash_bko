import os.path 

from ../.config.py import SCOPES, HEADERS_SPREADSHEET_ID, HEADERS_RANGE, TOKEN_PATH, CREDENTIALS_PATH

from google.auth.transport.requests import Requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.erros import HttpError

class Headers:
    # Initiate class variables
    def __init__(self, SCOPES, HEADERS_SPREADSHEET_ID, HEADERS_RANGE, TOKEN_PATH, CREDENTIALS_PATH):
        self.scopes = SCOPES
        self.sheet_id = HEADERS_SPREADSHEET_ID
        self.range = HEADERS_RANGE
        self.token_path = TOKEN_PATH
        self.creds = None
        

        self.getCreds()
        self.getService()
        # self.credentials_path = CREDENTIALS_PATH

    def getCreds(self)-> None:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                # Get a error
                pass
            

    def getService(self) -> None:
        try:
        # Mount a service that use the CREDENTIALS_PATH to autheticate google sheets api
            self.service = build('sheets', 'v4', credentials=self.creds)
        except expression as identifier:
            # If identifier gets a error must be on credentials object so we refresh her.
            getCreds()
        
        finally:
            # Finally we try to get service object again.
            self.service = build('sheets', 'v4', credentials=self.creds)
        
    
    def getHeaders(self) -> List:
        try:
            # Use the service obj tu access the HEADERS_SPREADSHEET_ID values from the RANGE
            header_data = self.service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id, range=self.range
                ).execute().get('values', [])
        except error as e:
            getService()
        finally:
             header_data = self.service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id, range=self.range
                ).execute().get('values', [])

        return header_data

