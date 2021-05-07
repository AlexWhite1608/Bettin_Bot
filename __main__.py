
from Login import *
from Bet import *

# apre homepage SNAI e chiude cookie
driver.get('https://www.snai.it\live')
driver.find_element_by_xpath('//*[@id="cookie-panel"]/div/div/span[2]/span/button[2]').click()

# esegue login
# Login()

bet = Bet()

bet.open_match()