import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import pyautogui
import docs

lista_drzava = ['_bih','_crna_gora','_hrvatska','_makedonija','_slovenija','_srbija']
path_ = r'C:\Users\XXXX\OneDrive\zagadjenje_vazduha_slike\zagadjenje_vazduha'
datum = str(datetime.date.today().strftime("%d.%m.%Y"))
new_path=''
for ld in lista_drzava:
    new_path = new_path + '"'+path_+ld+datum+'" '

s = Service('C:\Program Files\chrome_manager\chromedriver.exe')
link = 'https://instagram.com'
driver = webdriver.Chrome(service=s)
driver.get(link)
username = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.NAME,'username')))
username[0].send_keys(docs.username)
time.sleep(2)
pass_ = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.NAME,'password')))
pass_[0].send_keys(docs.password)
time.sleep(2)
btn = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')))
btn[0].click()

not_now = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="New post"]'))).click()

select_from_comp = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[text()="Select from computer"]'))).click()
time.sleep(5)
pyautogui.typewrite(path_+datum)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
for i in range(len(lista_drzava)):
    if i == 0:
        new_pic = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="Open media gallery"]'))).click()
    time.sleep(2)
    plus = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="Plus icon"]'))).click()
    time.sleep(2)
    pyautogui.typewrite(path_+lista_drzava[i]+datum+'.png')
    pyautogui.press('enter')
    time.sleep(5)

select_crop = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="Select crop"]'))).click()
time.sleep(5)
original = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"Original")]'))).click()
time.sleep(5)
next = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[text()="Next"]'))).click()
time.sleep(5)
next_ = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[text()="Next"]'))).click()
#time.sleep(2000)
caption = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[contains(@aria-label,"Write a caption...")]')))
caption.send_keys("#banjaluka #tuzla #doboj #trebinje #bihac #sarajevo #novisad #kragujevac #zenica #split")

share = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[text()="Share"]'))).click()
shared = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//div[text()="Post shared"]')))
close = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="Close"]'))).click()
driver.close()