# checking my repos
import requests
req = requests.get('https://api.github.com/users/GuySaar8/repos')
req_j = json.loads(req.content)
In [42]: type(req_j)
Out[42]: list
req_j[0]
req_j[0].get('name')

for i in req_j:
    print(f"{i.get('name')} is nice")



pip install selenium
python3 -m pip install --upgrade pip

# Q 1:
import selenium
from selenium import webdriver
driver_path = "/home/guy/Downloads/chromedriver"
chrome = webdriver.Chrome(driver_path)
chrome.get("https://walla.co.il")
chrome.quit()

driver_path = "/home/guy/Downloads/geckodriver"
firefox = webdriver.Firefox(executable_path=driver_path)
firefox.get("http://ynet.co.il")



# Q 2
# Was not sue about C
title=firefox.title
firefox.refresh
title2=firefox.title
In [24]: title
Out[24]: 'ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם'
In [30]: title2 == title
Out[30]: True

# Q 3
# on youtube search box
""""
    they both has the same locator becuase they are both getting the same
    html file.
"""
Ielement_firefox = firefox.find_element_by_id('search')
firefox.quit()

chrome = webdriver.Chrome("/home/guy/Downloads/chromedriver")
chrome.get("http://youtube.com")
chrome.find_element_by_id('search')

# Q 4
chrome.get('http://translate.google.com')
element_chrome = chrome.find_element_by_class_name('er8xn')
from selenium.webdriver.common.keys import Keys
element_chrome.send_keys("בדיקה")

# Q 5
chrome.get('http://youtube.com')
element_chrome = chrome.find_element_by_id('search')
element_chrome.send_keys("i got the power")
element_chrome.send_keys(keys.RETURN)


# Q 6
# using Xpath relative path
x=chrome.find_element_by_xpath("//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/span[1]/span[1]/div[1]/textarea[1]")

# using Xpath absolute path
x=chrome.find_element_by_xpath("/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/span[1]/span[1]/div[1]/textarea[1]")
print(x)
# using tag name
x=chrome.find_element_by_tag_name('textarea')
print(x)
# using class name
element_chrome = chrome.find_element_by_class_name('er8xn')
print(x)
# using css selector
# does not work
# x=chrome.find_element_by_css_selector("body.tQj5Y.ghyPEc.IqBfM.e2G3Fb.b30Rkd.l1ST5c.Ge9V1b.EIlDfe.cjGgHb.d8Etdd.LcUz9d:nth-child(2) c-wiz.zQTmif.SSPGKf.RvYhPd.BIdYQ.aL9XFd:nth-child(5) div.T4LgNb:nth-child(1) div.WFnNle c-wiz.MOkH4e.BSw7K.iYelWb.LUoOL div.OlSOob:nth-child(2) c-wiz.QsA0jb div.ccvoYb:nth-child(2) div.AxqVh div.OPPzxe c-wiz.rm1UF.YYaoY.nzsIKe span:nth-child(2) span:nth-child(1) div.QFw9Te > textarea.er8xn")


# Q 7
chrome.get('http://facebook.com')
email = chrome.find_element_by_id('email') .send_keys("user@gmail.com")
pas = chrome.find_element_by_id('pass') .send_keys("Aa123456")
from selenium.webdriver.common.keys import Keys
login = chrome.find_element_by_id('u_0_b') .send_keys(Keys.RETURN)

# Q 8
chrome.get_cookies()
chrome.delete_all_cookies()
chrome.get_cookies()

# other way to print to screen
import pickle
coockies = pickle.dump(chrome.get_cookies(),open("/home/guy/Desktop/coockies", "wb"))
In [61]: print (coockies)
# None


# Q 9
# is that what you wanted? or did we need to use chrome search function?
chrome.get("http://github.com")
y = chrome.find_element_by_name('q') .send_keys('selenium'+ Keys.RETURN)

# Q 10
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path='/home/guy/Downloads/chromedriver', chrome_options=chrome_options)
driver.get("http://github.com")

chrome_options = webdriver.FirefoxOptions()
chrome_options.add_argument("--disable-extensions")
driver_path = "/home/guy/Downloads/geckodriver"
firefox = webdriver.Firefox(executable_path=driver_path)
firefox.get("http://github.com")

# running on linux so no internet explorer here =]
