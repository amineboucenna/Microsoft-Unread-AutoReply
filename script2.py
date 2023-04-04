#Importing libraries
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


#Inserting email and password in their fields function 
def Input_cardinals(browser,name,text):
    field = browser.find_element(By.NAME,name)
    field.click()
    field.send_keys(text)
    field.send_keys(Keys.ENTER)
    browser.reconnect(0.1)

#main methods
def main():

    #You can edit the message,the email and the password
    custom_message = "Bonsoir,\nSaha ftourkoum u'\1F600' "
    email = 'wearyscuttles@outlook.com'
    password = 'H7G4cLq$eG'

    #Creating a browser instance
    browser = uc.Chrome(driver_executable_path='./chromedriver/chromedriver.exe')
    url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1680572331&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d80c93f96-d98a-e00e-3c7b-d45327f2c2aa&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015'
    
    #making a request to microsoft website
    browser.get(url)

    #Inserting the email then the password in their field 
    Input_cardinals(browser,'loginfmt',email)
    Input_cardinals(browser,'passwd',password)

    #Saving login info 
    stay_signed_in = browser.find_element(By.ID,'idSIButton9')
    stay_signed_in.click()
    

    #Switching from all inbox to unread
    browser.reconnect(10.0)
    unread_messages_switch = browser.find_element(By.XPATH,"//i[@data-icon-name='FilterRegular']")
    unread_messages_switch.click()
    browser.reconnect(3)
    unread_messages_switch = browser.find_element(By.XPATH,"//i[@data-icon-name='MailUnreadRegular']")
    unread_messages_switch.click()
    browser.reconnect(3)



    #Getting unread messages list
    messages_list = browser.find_elements(By.XPATH,"//div[@class='IjzWp XG5Jd gy2aJ Ejrkd']")


    for message in messages_list :
        message.click()
        browser.implicitly_wait(30)
        #Finding the reply button and clicking on it
        reply_button = browser.find_element(By.XPATH,"//i[@data-icon-name='ArrowReplyRegular']")
        reply_button.click()
        browser.implicitly_wait(30)

        #Finding the replying text area and inserting the custom message
        text_area = browser.find_element(By.XPATH,"//div[@class='elementToProof']")
        text_area.send_keys(custom_message)

        #Sending the message using a Key binding (Crtl+Enter)
        text_area.send_keys(Keys.CONTROL+Keys.ENTER)
        browser.implicitly_wait(30)
        #Repeating the process untill the end of the messages_list
    
    #making unread messages read
    check_all = browser.find_element(By.XPATH,"//div[@title='Select all messages']")
    check_all.click()
    browser.implicitly_wait(2)

    #click on the button : make all as read
    make_all_as_read = browser.find_element(By.XPATH,"//i[@data-icon-name='MailReadRegular']")
    make_all_as_read.click()
    

    #leaving the browser
    browser.implicitly_wait(9999)

    while True:
        pass





if __name__ == '__main__' :
    main()