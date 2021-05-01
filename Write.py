from setup import *
import csv


class Write:

    path = ""

    def __init__(self, path):
        # crea il file se non esiste e lo apre inizializzando i campi
        self.path = path
        with open(self.path + "\data.csv", 'w', newline='') as file:

            header = ["ID", "Partita", "Quota", "Punteggio al 75'", "Punteggio Finale"]
            writer = csv.writer(file, delimiter=',')
            writer.writerow(header)

            # usa per scrivere riga, come parametri prende i dettagli della scommessa
            # writer.writerow()

    # metodo che scrive i dettagli della scommessa su file. Prende in input l'istanza della classe Bet
    def write(self, Bet):
        pass
