import speech_recognition as sr
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from selenium import webdriver
options = Options()
options.add_argument("--headless")


def main(query):
    ##change the executable_path after downloadinng geckodriver
    executable_path="C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe"
    browser = webdriver.Firefox(executable_path=executable_path)
    browser.get('https://gaana.com/search/'+query)
    browser.find_element_by_class_name('hover-events-parent').click()
    browser.find_element_by_class_name('_ply').click()
    
