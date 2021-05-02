from setup import *
import time


class Bet:
    id = 0
    match = ''
    odd = 0.0
    score_75 = ''
    final_score = ''

    def __init__(self):
        pass

    def bet_setup(self):

        singole_partite = []

        # Trova il container con tutte le partite
        container_partite = driver.find_element_by_xpath('//*[@id="contentLivePage"]/div')
        time.sleep(1)

        # Apri tutte le date
        container_chiusi = container_partite.find_elements_by_class_name('accordionLeague.collapsed')
        for container_chiuso in container_chiusi:
            time.sleep(0.2)
            container_chiuso.click()

        container_leghe = container_partite.find_elements_by_class_name('leagueWrapperLive.ng-scope')
        for container_lega in container_leghe:
            # Trova le singole partite in una certa lega
            singole_partite = container_lega.find_elements_by_class_name(
                'container-fluid.noPadLeftRight.overflowHidden.ng-scope.rowColored')

        return singole_partite

    def find_matches(self):

        singole_partite = self.bet_setup()

        # Trova singole partite nel container
        for singola_partita in singole_partite:
            # Trova le squadre
            self.match = singola_partita.find_element_by_class_name('heightRowMatchLive.descriptionMatchLivePage')

    def find_score_75(self):

        singole_partite = self.bet_setup()

        for singola_partita in singole_partite:
            tempo = singola_partita.find_element_by_class_name('minutesWatchLivePage')

            # Scommetti se tempo maggiore di 70
            if tempo.text != '' and tempo.text != '-':
                if int(tempo.text) > 75:
                    # Trova punteggio squadra in casa
                    punteggio_casa = singola_partita.find_element_by_class_name('homeTeamScoreLivePage')

                    # Trova il punteggio della squadra in trasferta
                    punteggio_trasferta = singola_partita.find_element_by_class_name('awayTeamScoreLivePage')

                    self.score_75 = punteggio_casa + " - " + punteggio_trasferta

    def find_odd(self):

        singole_partite = self.bet_setup()

        for singola_partita in singole_partite:
            odd_casa = singola_partita.find_element_by_class_name('oddsWrapper.heightRowMatchLive.ng-scope').text
            odd_trasferta = singola_partita.find_element_by_class_name('oddsWrapper.heightRowMatchLive.ng-scope')








