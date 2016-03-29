# Embedded file name: c:\users\coen\documents\visual studio 2015\Projects\webScraping\webScraping\webScraping.py
import re
import mechanize
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
links = ['http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=267', 'http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=268', 'http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=114']
linkCount = 0
link = links[linkCount]
browser = webdriver.PhantomJS('D:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')

class scraper(object):

    def getSiteName(self):
        print 'getting site name'
        browser.get(link)
        siteName = browser.find_element_by_xpath('//*[@id="ctl00_tarPw"]').text
        print siteName

    def getPowerNow(self):
        print 'getting current power'
        print linkCount
        print link
        browser.get(link)
        powerNow = browser.find_element_by_xpath('//*[@id="ctl00_childPanel_lblNow"]').text
        print powerNow

    def getPowerToday(self):
        print "getting today's power"
        browser = webdriver.PhantomJS('D:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        browser.get(link)
        powerToday = browser.find_element_by_xpath('//*[@id="ctl00_childPanel_lblDEQ"]').text
        print powerToday

    def getPowerMonthly(self):
        print 'getting monthly power'
        browser = webdriver.PhantomJS('D:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        browser.get(link)
        powerMonthly = browser.find_element_by_xpath('//*[@id="ctl00_childPanel_lblMEQ"]').text
        print powerMonthly

    def getPowerYearly(self):
        print 'getting data'
        browser = webdriver.PhantomJS('D:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        browser.get(link)
        powerYearly = browser.find_element_by_xpath('//*[@id="ctl00_childPanel_lblYEQ"]').text
        print powerYearly


scraper = scraper()
for link in links:
    scraper.getSiteName()
    scraper.getPowerNow()
    scraper.getPowerToday()
    scraper.getPowerMonthly()
    scraper.getPowerYearly()
    linkCount += 1