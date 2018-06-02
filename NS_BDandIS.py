# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:06:16 2018

@author: AChowdhury143777
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#insider trading
#   bse
#   https://www.bseindia.com/corporates/Insider_Trading_new.aspx?expandable=2
#nse
#   https://www.nseindia.com/corporates/shldStructure/pit/shareholding_pit_post.htm

#  nse
#  corporate information - https://www.nseindia.com/corporates/content/PIT_Disc.xls
#  Historial 2015 PIT -- https://www.nseindia.com/corporates/content/PIT_Disc.xls

#https://www.nseindia.com/corporates/corporateHome.html

#Bulk/block deals
#   nse
#   https://www.nseindia.com/products/content/equities/equities/bulk.htm

#  Shareholding information -- //*[@id="ext-gen60"]
#  PIT post  2015 -- //*[@id="ext-gen59"]/div/li[7]/ul/li[2]/div/a/span

#%%


# In[2]:
from selenium import webdriver
#from selenium.webdriver import ActionChains
import pandas as pd
import time
import os
import warnings
from bs4 import BeautifulSoup, Comment
import re
import numpy as np
warnings.filterwarnings(action='once')

#%%

newdatafolder = '31_03_2018'

#%%
cwd = os.getcwd()
oneupdirectory = os.path.dirname(cwd)
twoupdirectory = os.path.dirname(oneupdirectory)


# In[3]:
stocklistpath = oneupdirectory
os.path.join(cwd, 'data', newdatafolder, 'Annual')
pathannual=os.path.join(cwd, 'data', newdatafolder, 'Annual')
pathquaterly=os.path.join(cwd, 'data', newdatafolder, 'Quaterly')

#%%
#Delete the previous content of error file it it exist

try:
    errorfilename= 'error1.csv'
    fd = open(errorfilename,'w')
    fd.close()

except:
    pass


#%%

#stocklistfilename  = 'error1.csv'
stocklistfilename  = 'EQUITY_L_NSE.csv'

errorfilename= 'error1.csv'

path=r'C:\Users\achowdhury143777\OneDrive - Applied Materials\scripts\NSE_STOCKLIST'

#stocklist = pd.read_csv(os.path.join(stocklistpath,stocklistfilename), usecols=['SYMBOL'])
stocklist = pd.read_csv(os.path.join(stocklistpath, stocklistfilename), usecols=['SYMBOL'])
stocklist['downloadedflag'] = stocklist['SYMBOL']

#%%
alreadydownloaded = "downloaded.csv"

try:
    stocklist2 = pd.read_csv(alreadydownloaded, usecols=['SYMBOL', 'downloadedflag'])
    
except:
    stocklist2 = stocklist

#%%
    
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 

try:
    chromedriverpath = r"C:\Users\abhis\Desktop\Chromedrive\chromedriver.exe"
    
    browser = webdriver.Chrome(chromedriverpath, options=options)
    
except:

    browser = webdriver.PhantomJS(service_log_path=os.path.devnull)


# In[5]:


loginurl = "https://www.nseindia.com/corporates/corporateHome.html"
browser.get(loginurl)
time.sleep(2.22)

browser.find_element_by_xpath('//*[@id="ext-gen60"]').click()
time.sleep(3.16)
#browser.find_element_by_xpath('//*[@id="ext-gen59"]/div/li[7]/ul/li[2]/div/a/span"]').click()
browser.find_element_by_link_text('Post 15-May-2015').click()
time.sleep(6.16)
browser.find_element_by_link_text('Export to csv').click()
time.sleep(3.16)

#%%

browser.find_element_by_link_text('Export to csv').click()
time.sleep(3.16)

#%%

size = browser.find_element_by_tag_name("iframe")

#%%

print(size)



#%%

pagesource = browser.page_source.encode('utf-8')
data = pd.read_html(pagesource)

#%%
loginurl = "https://www.nseindia.com/corporates/shldStructure/pit/shareholding_pit_post.htm"
browser.get(loginurl)
time.sleep(6.22)

#%%
#browser.find_element_by_link_text('Export to csv').click()
#browser.find_element_by_xpath('//*[@id="csvLink"]').click()
browser.find_element_by_partial_link_text('csv').click()
#//*[@id="csvLink"]
time.sleep(3.16)


#%%

pagesource = browser.page_source.encode('utf-8')
data = pd.read_html(pagesource, encoding='latin1')






