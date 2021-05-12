
from setup import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

###### VARIABILI #####

min_minute = 50
min_odd = 1.05


######################

class Bet:
    container_leghe = []

    # Nel costruttore si individua il container di tutte le partite disponibili attualmente
    def __init__(self):
        # WebDriverWait(driver, 5).until(
        # EC.presence_of_element_located((By.CLASS_NAME, 'accordionLeague.collapsed')))

        # Apri tutte le leghe disponibili
        container_chiusi = driver.find_elements_by_class_name('accordionLeague.collapsed')
        for container_chiuso in container_chiusi:
            container_chiuso.click()
            time.sleep(0.1)

        # Trova il container generale in cui sono presenti tutte le leghe in cui ci sono le partite
        time.sleep(1)
        container_generale = driver.find_element_by_xpath('//*[@id="contentLivePage"]/div')

        # Trova tutti i container delle leghe
        Bet.container_leghe = container_generale.find_elements_by_class_name('leagueWrapperLive.ng-scope')

    def open_match(self):

        # Trova ed apre le partite (in un tab separato) dal min_minute in poi
        for lega in Bet.container_leghe:
            matches = lega.find_elements_by_class_name(
                'row.noMargin')

            # Trova singole parite presenti nella lega
            for container_partita in matches:
                match = container_partita.find_element_by_class_name('homeAwayTeamsLivePage.capitalize.ng-binding')

                # Verifica tempo di gioco e apre parite in un altro tab
                time_match = container_partita.find_element_by_class_name('minutesWatchLivePage')
                if time_match.text != '-' and time_match.text != '' and int(time_match.text) >= min_minute:
                    match_url = match.get_attribute('href')

                    self.open_tab(match_url)

                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

    # Trova le due squadre che giocano
    def find_teams(self):
        teams = driver.find_element_by_id('headAvvName').text
        return teams

    # Metodo che apre la partita in un nuovo tab
    def open_tab(self, matchUrl):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(matchUrl)

    # Metodo per trovare la quota più bassa
    def find_odds(self):
        try:
            odds = []
            odds.append(float(driver.find_element_by_xpath(
                '//*[@id="quoteLive"]/div[2]/table[1]/tbody/tr[1]/td[1]/div/div/div[2]/span').text.replace(',', '.')))
            odds.append(float(driver.find_element_by_xpath(
                '//*[@id="quoteLive"]/div[2]/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/span').text.replace(',', '.')))
            odds.append(float(driver.find_element_by_xpath(
                '//*[@id="quoteLive"]/div[2]/table[1]/tbody/tr[1]/td[3]/div/div/div[2]/span').text.replace(',', '.')))
            odd = min(odds)
            return odd
        except NoSuchElementException:
            return 'Quota non disponibile'
        except ValueError:
            return 'Quota troppo bassa'
