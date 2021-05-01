from setup import *
import csv


class Write:

    def __init__(self, path):
        # crea il file se non esiste e lo apre inizializzando i campi
        with open(path + "\data.csv", 'w', newline='') as file:

            header = ["ID", "Partita", "Quota", "Punteggio al 75'", "Punteggio Finale"]
            writer = csv.writer(file, delimiter=',')
            writer.writerow(header)

            # usa per scrivere riga, come parametri prende i dettagli della scommessa
            # writer.writerow()

