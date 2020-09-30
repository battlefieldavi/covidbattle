from plyer import notification#for notification
from bs4 import BeautifulSoup#Web grabber
import requests
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\steal\\Downloads\\virus.ico",
        timeout=4
    )

def getd(url):
    r=requests.get(url)
    return r.text


if __name__ == "__main__":
    print('done')
    #notifyMe("AVI", "lets do this")
    html=getd("https://www.mohfw.gov.in/")
    
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    mydatastr=""
    for table in soup.find_all('tbody'):#[1].find_all(''tr')
        mydatastr+=table.get_text()
    items=(mydatastr[1:].split('\n\n'))
    state=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']  
    for item in items[0:35]:
        dl=item.split('\n')
        
        if dl[2] in state:
            print(dl)
            t="COVID-19 Status"
            m=f"{dl[2].upper()}\nActive {dl[3]}\nCured {dl[4]}\nDeaths {dl[5]}\nTotal Confirmed cases {dl[6]}"
            notifyMe(t,m)
            time.sleep(3)
                    
