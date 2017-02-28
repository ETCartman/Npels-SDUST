from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.action_chains import ActionChains
from clickList import csslist,clicks,csslist2,clicks2
import random

csslist = csslist.split(',')
clicks = clicks.split(',')


TIME = 46

driver = webdriver.Chrome()
driver.get('http://192.168.100.117/NPELS/')

def login(username,userpassword,uc,un):
    driver.find_element_by_id("tbName").send_keys(username)
    driver.find_element_by_id("tbPwd").send_keys(userpassword)
    driver.find_element_by_id('btnLogin').click()
    time.sleep(5)
    # for i in range(1,8):
    #     global TIME
    #     TIME = 46
    if uc == 1:
        ALL = 8
    else:
        ALL = 14
    if uc <= 0 or un <= 0:
        print('BAD number')
    elif un <= 8:
        start(uc,un - 1)
    elif un == 100:
        for i in range(0,ALL):
            global TIME
            TIME = 46
            start(uc,i)
    driver.quit()


    #start('#ctl00_ContentPlaceHolder1_aContinue')


def start(uc,i):
    global TIME
    driver.switch_to.frame('mainFrame')
    if uc == 2:
        ccss1 = '.mainmenu > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
        ccss2 = '.mainmenu > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
        css = '#aspnetForm > div.content > div.main_right > div:nth-child(3) > div > div.class_container > div > ul:nth-child(2) > a'
    else:
        ccss1 = '#menu-container > ul > li:nth-child(3) > a'
        ccss2 = '#menu-container > ul > li:nth-child(1) > a'
        css = '#aspnetForm > div.content > div.main_right > div:nth-child(3) > div > div.class_container > div > ul:nth-child(1) > a'
    driver.find_element_by_css_selector(css).click()
    time.sleep(5)
    above = driver.find_element_by_css_selector(csslist[i])
    time.sleep(3)
    ActionChains(driver).move_to_element(above).perform()
    driver.find_element_by_css_selector(clicks[i]).click()
    time.sleep(8)
    driver.switch_to.frame('contentFrame')
    while (TIME):
        driver.find_element_by_css_selector(ccss1).click()
        time.sleep(50)
        driver.find_element_by_css_selector(ccss2).click()
        time.sleep(50)
        TIME = TIME - 2
        print('已进行 %s 分钟' % (46 - TIME))
    driver.refresh()




username = input('输入用户名 ：')
userpassword = input('请输入密码 ：')
print('###############################################')
print('选择科目')
print('1.综合')
print('2.听说')
userchs = int(input(''))
print('###############################################')
print('选择单元(1-8或1-14) 100为全部')
usernum = int(input(''))
print("###############################################")
if userchs == 2:
    csslist = csslist2.split(',')
    clicks = clicks2.split(',')
###############我就想知道多少人用了####################
param = {
    'uid':username
}
requests.post('http://www.jhanlin.com/jilu.php' ,data=param)

##############你不介意对吧#####################
login(username,userpassword,userchs,usernum)




