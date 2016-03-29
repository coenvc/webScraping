import re 
import mechanize
from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities   
from peewee import * 
import decimal
from itertools import izip 
import lxml.html 
from selenium.common.exceptions import NoSuchElementException
from pprint import pprint
links = ["http://www.solarmanpv.com/portal/terminal/TerminalMain.aspx?come=Public&pid=163","http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=267" 
         ,"http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=268","http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=114",
         "http://www.solarmanpv.com/portal/terminal/TerminalMain.aspx?come=Public&pid=255"
         ]   

accountInfo = [{'username': "vogelzichtpebble@gmail.com", 'password' : "Pebble01",'siteName':"vogelzicht"}, 
               {'username': "torenzichtpebble@gmail.com", 'password' : "Pebble01",'siteName': "TorenZicht"}, 
               ]

linkCount = 0 
link = links[linkCount] 
browser = webdriver.PhantomJS('D:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')   
sleep = time.sleep 
db = SqliteDatabase('gegevens.db') 
gegevens = []
dictionary = {}
class Site(object):  
    def getTable(self, i, Count): 
        while Count < 1: 
            userNameAccount =  raw_input("voer de gebruikersnaam in van het systeem ")  
            userPassAccount = raw_input("voer het wachtwoord in voor het systeem ") 
            accountInfo.append({'username': userNameAccount, 'password':userPassAccount}) 
            done = raw_input("Klaar Y\N ?") 
            if(done == "Y"): 
                Count += 1  
                break   
        #Let the user know from which account we're getting data from  
        print "gegevens aan het ophalen voor " + accountInfo[i]['siteName']
        #Select the username and password for the site we are going to get data for
        username = accountInfo[i]['username']
        password = accountInfo[i]['password']
        browser.get("http://www.solarmanpv.com/portal/LoginPage.aspx")  
        #browser.find_element_by_xpath["//input[@id='uNam'"].clear()
        #Write Username in Username TextBox 
        browser.find_element_by_xpath("//input[@id='uNam']").send_keys(username)
        #Clear Password TextBox if already allowed "Remember Me" 
        browser.find_element_by_xpath("//input[@id='uPwd']").clear()
        #Write Password in password TextBox
        browser.find_element_by_xpath("//input[@id='uPwd']").send_keys(password)
        #Click Login button
        browser.find_element_by_xpath("//input[@id='Loginning']").click()
        #let the user know you are logging in  
        print "logging in!"  
        browser.get("http://www.solarmanpv.com/portal/Terminal/TerminalReal.aspx?pid=9805&key=77DJJE6") 
        sleep(2) 
        print "I'm digging in there!"
        root = lxml.html.fromstring(browser.page_source) 
        cells = []   
        i = 1
        for row in root.xpath('.//table[@id="list_block"]//tr'):
            cells = row.xpath('.//td/text()')    
            try:
                serienummer = browser.find_element_by_xpath('//*[@id="Item'+str(i)+'.2"]/td[2]/a').text  
            except:   
                serienummer
            if (len(cells) > 10):       
                i += 1 
                rij = {  
                        "Serienummer" : serienummer,  
                        "Energie": cells[9] 
                    }     
                pprint(rij) 
                gegevens.append(dict(rij))            


site = Site()   
i = 0 
Count = 0;
for account in accountInfo: 
    site.getTable(i, Count);   
    i += 1


class user(Model): 
        serial = CharField(max_length = 100, primary_key = True) 
        power = FloatField(default = 0) 
        class Meta: 
            database = db 

def add_site():   
    i = 0 
    for items in gegevens:  
        serial= gegevens[i]['Serienummer'] 
        power =  gegevens[i]["Energie"]
        try: 
            user.create( serial = serial, power = power)    
            i += 1

        except IntegrityError: 
            user_record = user.get(serial = serial )  
            user_record.power = power
            user_record.save() 

if __name__ == '__main__': 
    db.connect()
    db.create_tables([user], safe = True)   
    add_site() 
