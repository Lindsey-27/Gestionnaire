import random
import string
import datetime

matricule_existant = []
def matricule_auto():
    while True:
        matricule = "".join(random.sample(string.hexdigits, k=10))
        if matricule not in matricule_existant:
            matricule_existant.append(matricule)
            return matricule
#for _ in range(5): ## C'est juste pour tester si ca fonctionne
matricule_auto()

def date_enregistrement():
    while True:
        date = datetime.datetime.now()
        date_actuelle = date.strftime("%d-%m-%Y %H:%M:%S")
        return date_actuelle
print(date_enregistrement())


