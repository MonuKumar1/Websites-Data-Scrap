from typing import List
import gspread
# from models import ScrapedWebsite
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json
from config import *
# from utils import Utils

class GoogleSheets:

    @staticmethod
    def saveToSheets(scrapedWebsites: List[ScrapedWebsite], disallowed_usernames):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('%s.json' % (google_service_key_file_path), scope)

        client = gspread.authorize(creds)

        # sheet = client.open(sheet_name_for_writing_scraped_emails)
        sheet = client.open_by_key("1CKFg4HPF5fsTdUR4uLnG_MeQGbD8dfjW_qU1EQFy6Jw")

        # sheet_instance = sheet.get_worksheet(sheet_number_for_writing_scraped_emails)
        sheet_instance = sheet.get_worksheet(0)

        data : List[dict]  = []

        
        for website in scrapedWebsites:
            emails_strings = ""
            for i in range(len(website.emails)):
                email = website.emails[i]
            
                if Utils.email_contains_disallowed_username(email, disallowed_usernames):
                    continue

                emails_strings += email + "%s" % ("" if (i==len(website.emails) - 1) else ",")
            data.append(website.toMap(emails_strings))

        jsonData = json.dumps(data)

        print("data to be written to sheets - ")
        print(jsonData)

        records_df = pd.DataFrame.from_dict(eval(jsonData))

        sheet_instance.clear()
        sheet_instance.insert_rows(records_df.values.tolist())


        
