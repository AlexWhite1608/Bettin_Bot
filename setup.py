from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)
