__author__ = 'shashir'


from splinter import Browser
import time
import logging

def ConnectionSetup():
    global browser
    browser = Browser()
    global browser1
    browser1= Browser()
    browser.visit("https://oneplus.net/invites?kolid=FDO5LS")
    print '--opened one plus site'
    browser1.visit("http://temp-mail.org/")
    print '--opened fake email generation site'

def OnePlus():
    if browser.is_element_present_by_id('email', wait_time=15):
        browser.find_by_id('email').click()
        print '--found email text box'
        browser.type('invite-email', email, slowly=True)
        print '--entered email id'

        if browser.is_element_present_by_id('submit_email', wait_time=15):
            browser.find_by_id('submit_email').click()
            print '--clicked on Submit button'

def FakeMail():
    if browser1.is_element_present_by_id("click-to-delete", wait_time=30):
        browser1.find_by_id("click-to-delete").click()
        print '--clicked on Delete button'
        time.sleep(5)
        global email
        emailid = browser1.find_by_xpath(".//*[@id='mail']").first
        email = str(emailid.value)
        print email
        print '--copied email id'

def ConfirmSign():
    try:

        if browser1.is_element_present_by_xpath(".//*[@id='mails']/tbody/tr/td[2]/a", wait_time=30):
            print '--checked for email received '
            time.sleep(8)
            browser1.find_by_xpath(".//*[@id='mails']/tbody/tr/td[2]/a").click()
            print '--clicked on received email'
            time.sleep(3)
            browser1.find_by_xpath("html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/div[1]/div/div/p/a").click()
            print '--clicked on confirm signup button'
    except Exception, e:
        logging.log('','')
        print e
        pass
def SuccessOrFailure():
    if browser.is_element_present_by_id('totalInvited', wait_time=15):
        print '--successful run:' + str(j)
        browser.reload()
        print '--reloaded one plus website'
        browser1.back()
        print '--backwarded fake mail website'
    else:
        print '--failed run:' + str(j)


def MasterFunction():
    ConnectionSetup()
    global i
    i = 1
    global j
    j = 1
    while i != 0:

        FakeMail()
        OnePlus()
        ConfirmSign()
        SuccessOrFailure()
        j += 1

try:
    MasterFunction()
except:
    logging.log('','')
    pass
finally:
    browser.quit()
    browser1.quit()
    MasterFunction()







