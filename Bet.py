from selenium.common.exceptions import NoSuchElementException
from setup import *
import time

# TODO: far si che il numero dei match, dei risultati e delle quote combaci
# TODO: bug fix delle quote sotto il valore minimo


###### VARIABILI #####

min_minute = 40
min_odd = 1.05

######################


def setup_bet():
    container_leghe = []
    # Trova il container con tutte le partite
    container_partite = driver.find_element_by_xpath('//*[@id="contentLivePage"]/div')
    time.sleep(1)

    # Apri tutte le date
    container_chiusi = container_partite.find_elements_by_class_name('accordionLeague.collapsed')
    for container_chiuso in container_chiusi:
        container_chiuso.click()
        time.sleep(0.1)

    # Trova singoli container
    container_leghe = container_partite.find_elements_by_class_name('leagueWrapperLive.ng-scope')

    return container_leghe


def find_match():
    list_matches = []
    try:
        container_leghe = setup_bet()
        for container_lega in container_leghe:

            # Trova le singole partite in una certa lega
            singole_partite = container_lega.find_elements_by_class_name(
                'container-fluid.noPadLeftRight.overflowHidden.ng-scope.rowColored')

            for singola_partita in singole_partite:

                # Trova le squadre
                tempo = singola_partita.find_element_by_class_name('minutesWatchLivePage')
                if tempo.text != '' and tempo.text != '-':
                    if int(tempo.text) >= min_minute:
                        match = singola_partita.find_element_by_class_name(
                            'heightRowMatchLive.descriptionMatchLivePage')
                        match = match.text.replace('\n', ' - ')
                        list_matches.append(match)
    except NoSuchElementException:
        pass

    return list_matches


def find_result_75():
    list_result_75 = []
    try:
        container_leghe = setup_bet()
        for container_lega in container_leghe:

            # Trova le singole partite in una certa lega
            singole_partite = container_lega.find_elements_by_class_name(
                'container-fluid.noPadLeftRight.overflowHidden.ng-scope.rowColored')

            for singola_partita in singole_partite:

                # Trova le squadre
                tempo = singola_partita.find_element_by_class_name('minutesWatchLivePage')

                if tempo.text != '' and tempo.text != '-':
                    if int(tempo.text) >= min_minute:

                        # Trova il container delle tre le quote per ogni partita
                        odds_container = singola_partita.find_element_by_class_name(
                            'betWrappper.heightRowMatchLive.displayBlock')

                        # Trova un singola quota nella partita
                        odds = odds_container.find_elements_by_class_name('oddsLive.ng-binding')

                        # Confronta il risultato per evitare i pareggi
                        risultato_casa = singola_partita.find_element_by_class_name(
                            'homeTeamScoreLivePage').text
                        risultato_trasferta = singola_partita.find_element_by_class_name(
                            'awayTeamScoreLivePage').text

                        if int(risultato_casa) != int(risultato_trasferta):
                            risultato = risultato_casa + "-" + risultato_trasferta
                            list_result_75.append(risultato)
    except NoSuchElementException:
        print("Errore")

    return list_result_75

def find_odds():
    list_odds = []
    try:
        container_leghe = setup_bet()
        for container_lega in container_leghe:

            # Trova le singole partite in una certa lega
            singole_partite = container_lega.find_elements_by_class_name(
                'container-fluid.noPadLeftRight.overflowHidden.ng-scope.rowColored')

            for singola_partita in singole_partite:

                # Trova le squadre in base alla condizione del tempo
                tempo = singola_partita.find_element_by_class_name('minutesWatchLivePage')
                if tempo.text != '' and tempo.text != '-':
                    if int(tempo.text) >= min_minute:

                        # Trova il container delle tre le quote per ogni parita
                        odds_container = singola_partita.find_element_by_class_name(
                            'betWrappper.heightRowMatchLive.displayBlock')

                        # Trova un singola quota nella partita
                        odds = odds_container.find_elements_by_class_name('oddsLive.ng-binding')

                        # Confronta il risultato per evitare i pareggi
                        risultato_casa = singola_partita.find_element_by_class_name(
                            'homeTeamScoreLivePage').text
                        risultato_trasferta = singola_partita.find_element_by_class_name(
                            'awayTeamScoreLivePage').text
                        if int(risultato_casa) != int(risultato_trasferta):

                            # Ciclo per convertire in float e trovare la quota minima (maggiore di min_odd)
                            m_list = []  # lista di appoggio per convertire in float
                            for odd in odds:
                                if odd.text != '':
                                    odd = odd.text.replace(',', '.')
                                    m_list.append(float(odd))
                                    if float(odd) >= min_odd and len(m_list) == 3:
                                        list_odds.append(min(m_list))
                                    elif float(odd) < min_odd:
                                        list_odds.append('Quota troppo bassa!')
    except NoSuchElementException:
        print("Errore")
    return list_odds
