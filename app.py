from operator import le
from time import sleep
from datetime import datetime
from wsgiref import headers
from wsgiref.util import shift_path_info
from flask import Flask, render_template, request, json, send_from_directory
import requests as r 
from threading import *
from bs4 import BeautifulSoup
from flask import jsonify
# from openpyxl import Workbook
import pygsheets
import os
from urllib.parse import urlparse
from time import sleep

app = Flask(__name__, static_url_path='', static_folder='static')

app.config['APP_ROOT'] = os.path.dirname(os.path.abspath(__file__))

print(app.static_url_path)
print(app.static_folder)
print(app.root_path)


ROOT_URL = 'https://www.sitelike.org/'

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

# session = r.Session()

@app.route('/')
def home():
    return render_template('home2.html')
    # return "Hello World!"

@app.route('/submit',methods=["POST"])
def submit():
    
    print("request recieved")

    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    URLS = data['urls']
    URLS = URLS.split(" ")


    sheet_url=[]

    t1 = Thread(target=main_scrape,args=[sheet_url,URLS])
    # t1 = Thread(target=main_scrape,args=[url,query])
    t1.start()
    while len(sheet_url) == 0:
        None
    # text = (','.join(URLS))
    # if len(text) > 45:
    #     text = text[0:45] + '...'
    # data = {'sheets_url':sheet_url[0], 'query_str': text}
    # return render_template(request,'home2.html',data)
    print(sheet_url[0])
    return {"gsheet_link": sheet_url[0]}





def main_scrape(sheet_url,URLS):

    gs = pygsheets.authorize(service_file='service_account_sheets.json')
    try:
        sh = gs.open(title='SiteLike Links')
    except pygsheets.PyGsheetsException:
        print('Spreadsheet Not Found!\nCreating New Spreadsheet...')
        sh = gs.create(title='SiteLike Links')
        # sh.share('store3age@gmail.com',role='writer',type='user')
        sh.share('', role='reader', type='anyone')


    try:
        gs = pygsheets.authorize(service_file='service_account_sheets.json')
    except Exception as e:
        print(e)
        return  jsonify({"status": "error", "message": "Error in connecting to google sheets"})
    print("sheet done")
    print(sh.url)    

    worksheet_title = "Srcrapped_at"+  "__"+ str( datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
    wks = sh.add_worksheet(title=worksheet_title,cols=2)
    wks.update_value('A1', "Similar Websites")
    wks.cell('A1').set_text_format('bold', value=True) 
    print("worksheet title: ",worksheet_title)    

    sheet_link = sh.url + '/view#gid=' + str(wks.id)  
    sheet_url.append(sheet_link)


    try:

        websites=[]
        for URL1 in URLS:
            sleep(5)
            print("working on wesite: ", URL1)
            
            # sleep(10)

            # removing http:// and https:// and www. from the SLUG_URL using urlparse
            # SLUG_URL = urlparse(SLUG_URL).netloc
            SLUG_URL = URL1.replace("http://","").replace("https://","").replace("www.","")
            # print("SLUG_URL: ",SLUG_URL)    
            print("scraping: ",SLUG_URL)
            # website = SLUG_URL
            # print("SLug url in var: ", website)
            # sleep(10)
            s = r.get(ROOT_URL + 'similar/' +SLUG_URL,headers=headers)
            contents = BeautifulSoup(s.content, 'html.parser')
            panels_blocks = contents.find_all('div', class_='row panel panel-default rowP')
            # worksheet_title = "Srcrapped_at"+  "__"+ str( datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
            # worksheet_title = SLUG_URL.split(".")[0] + str( datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
            # wks = sh.add_worksheet(title=worksheet_title)
            
            # col_name = "Results for "+ str(SLUG_URL)
            # wks.update_value('A1',"Similar Websites")
            # wks.cell('A1').set_text_format('bold', value=True) 

            # print("worksheet title: ",worksheet_title)

            # sheet_link = sh.url + '/view#gid=' + str(wks.id)
            # contents = BeautifulSoup(s.content, 'html.parser')
            # panels_blocks = contents.find_all('div', class_='row panel panel-default rowP')


            # if URL1 == URLS[0]:
            #     # print("appending")
            #     sheet_link = sh.url + '/view#gid=' + str(wks.id)
            #     sheet_url.append(sheet_link)
                # print("appended")

            # i = 2    
            # print("going in block loop")
            for block in panels_blocks:
                # sleep(3)
                # print("inside block loop")
                links = block.find_all('a', class_ = 'btn btn-link btn-lg')
                website_name = links[0].text.split('\n')[1]
                website_sitelike_url = links[0].get('href')
                website_url = website_name
                if len(links)>1:
                    website_url = links[1].get('href')
                websites.append(website_url)
                # wks.append_table(values=[[website_name, website_url, website_sitelike_url]])

                # row = 'A' + str(i)
                # wks.update_value(row, website_url)
                # i = i+1
                print("data added to sheet for website: ",website_url)
                # print(website_name,'----->', website_sitelike_url, '----->',website_url)

        
            gsheet_link = sh.url + '/view#gid=' + str(wks.id)
            print('Sheet Link for', SLUG_URL, ': ', gsheet_link)
        # sleep(10)
        # wks.insert_cols(1, number=len(websites), values=websites, inherit=False)
        wks.insert_cols(1, number=2, values=websites, inherit=False)
        # wks.insertRows(wks.getLastRow(), websites.length)

        # sleep(2)

        return {"gsheet_link": sheet_link}

    except Exception as e:
        print(e)
        return  jsonify({"status": "error", "message": "Error in Scrapping data"})





    
    # wb = Workbook()
    # sheet = wb.active
    # x=len(websites)
    # for i in range(x):
    #     sheet.append([websites[i]])
    # file_name = 'urls.xlsx'
    # PATH = 'static/files/'
    # file_path = os.path.join(app.config['APP_ROOT'], PATH)
    # # print(file_path)
    # wb.save(file_path+file_name)



    # try:
    #     print("trying to send file")
    #     return send_from_directory(file_path, file_name, as_attachment=True)
    # except Exception as e:
    #     print(e)
    #     return {"error":str(e)}






@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error2.html'), 404



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    app.run(debug=True)