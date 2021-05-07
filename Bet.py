from selenium.common.exceptions import NoSuchElementException
from setup import *
import time

###### VARIABILI #####

min_minute = 40
min_odd = 1.05

######################

class Bet:

    container_leghe = []

    # Nel costruttore si individua il container di tutte le partite disponibili attualmente
    def __init__(self):

        # Apri tutte le leghe disponibili
        container_chiusi = driver.find_elements_by_class_name('accordionLeague.collapsed')
        for container_chiuso in container_chiusi:
            container_chiuso.click()
            time.sleep(0.1)

        time.sleep(1)
        container_generale = driver.find_element_by_xpath('//*[@id="contentLivePage"]/div')
        time.sleep(1)
        Bet.container_leghe = container_generale.find_elements_by_class_name('leagueWrapperLive.ng-scope')

    def open_match(self):

        # Trova ed apre le partite (in un tab separato) dal min_minute in poi
        for lega in Bet.container_leghe:
            matches = lega.find_elements_by_class_name(
                'row.noMargin')
            for container_partita in matches:
                match = container_partita.find_element_by_class_name('homeAwayTeamsLivePage.capitalize.ng-binding')

                time_match = container_partita.find_element_by_class_name('minutesWatchLivePage')
                if time_match.text != '-' and time_match.text != '' and int(time_match.text) >= min_minute:
                    match_url = match.get_attribute('href')
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(match_url)
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
