from selenium.common.exceptions import NoSuchElementException
from setup import *
import time

min_minute = 75

def set_bet():
    container_leghe = []
    # Trova il container con tutte le partite
    container_partite = driver.find_element_by_xpath('//*[@id="contentLivePage"]/div')
    time.sleep(1)

    # Apri tutte le date
    container_chiusi = container_partite.find_elements_by_class_name('accordionLeague.collapsed')
    for container_chiuso in container_chiusi:
        container_chiuso.click()

    # Trova singoli container
    container_leghe = container_partite.find_elements_by_class_name('leagueWrapperLive.ng-scope')

    return container_leghe


def find_match():
    list_matches = []
    try:
        container_leghe = set_bet()
        for container_lega in container_leghe:

            # Trova le singole partite in una certa lega
            singole_partite = container_lega.find_elements_by_class_name(
                'container-fluid.noPadLeftRight.overflowHidden.ng-scope.rowColored')

            for singola_partita in singole_partite:
                # Trova le squadre
                tempo = singola_partita.find_element_by_class_name('minutesWatchLivePage')
                if tempo.text != '' and tempo.text != '-':
                    if int(tempo.text) > min_minute:
                        match = singola_partita.find_element_by_class_name('heightRowMatchLive.descriptionMatchLivePage')
                        list_matches.append(match.text)
    except NoSuchElementException:
        pass


    return list_matches