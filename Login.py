import time

from setup import *


class Login:
    name = ""
    password = ""

    def __init__(self):
        # apre il form di login
        driver.find_element_by_id('accedi-button').click()
        time.sleep(1)

        self.name = input("Inserisci nome: ")
        driver.find_element_by_id('edit-name').send_keys(self.name)

        self.password = input("Inserisci password: ")
        driver.find_element_by_id('edit-pass').send_keys(self.password)

        driver.find_element_by_id('edit-submit--2').click()
        time.sleep(1)

        # gestisce in caso di errore di autenticazione
        isError = False
        while not isError:
            errore = driver.find_elements_by_id('messages')
            if errore:
                print('Credenziali errate!')
                self.name = input("Inserisci nome: ")
                self.password = input("Inserisci password: ")
                driver.find_element_by_id('edit-name').send_keys(self.name)
                driver.find_element_by_id('edit-pass').send_keys(self.password)
                driver.find_element_by_id('edit-submit').click()

            else:
                print('Credenziali corrette!')
                isError = True
