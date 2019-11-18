import random
import time


ersterVokabeltest = {
    "to apply": "anwenden",
    "to design": "entwerfen, konstruieren",
    "website": "Website, Internetseite",
    "to integrate": "integrieren",
    "database": "Datenbank",
    "focus": "Schwerpunkt",
    "design": "Gestaltung, Design",
    "to advise": "beraten",
    "functionality": "Funktionalität",
    "option": "Alternative, Möglichkeit",
    "benefit": "Leistung, Nutzen",
    "overall": "gesamt",
    "suggestion": "Vorschlag",
    "impact": "Wirkung, Einfluss",
    "performance": "Ergebnis, Erfolg",
    "thorough": "gründlich",
    "analytical": "analytisch",
    "verbal": "mündlich",
    "graphic": "graphisch",
    "to troubleshoot": "Fehler beheben",
    "maintenance": "Wartung",
    "LAN (local area network)": "lokales Netzwerk",
    "WAN (wide area network)": "Weitverkehrsnetzwerk",
    "implementation": "Einführung, Umsetzung, Implementierung",
    "to recommend": "empfehlen",
    "to schedule": "anberaumen",
    "to handle": "umgehen mit",
    "confidential": "vertraulich",
    "broad": "breit angelegt",
    "several": "mehrere",
    "to recognize": "erkennen, anerkennen",
    "career": "Beruf, Laufbahn, Karriere",
    "to outline": "umreißen, skizzieren",
    "systems analyst": "Systemberater",
    "findings": "Ergebnisse",
    "job title": "Berufsbezeichnung",
    "to swap": "tauschen"
}

vokabeln = ersterVokabeltest


def whenDone():
    text="\nGute Arbeit. " + str(counter) + " von " + str(countertried)+ " Vokabeln richtig bearbeitet."
    if counter != countertried:
        text= text+ " An diesen Vokabeln musst du noch arbeiten:" 
    elif counter == countertried:
        print("Alles richtig! Bekommst du das nochmal hin?")
    print (text)
    for vok in wrong:
        print(vok," = ", vokabeln[vok])

def main():
    global counter , countertried, wrong
    counter = 0
    countertried = 0
    wrong =[]
    for vok, w in sorted(vokabeln.items(), key =lambda x: random.random()):
        print(vok)    
        guess=input()
        
        if guess == w:
            print ("Richtig: "+ vok + " = "+ w)
            counter+=1
        elif guess in w:
            print("Gut. Korrekt ist: "+vok+" = " + w) 
            counter+=1
        else:
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
        countertried+=1
        time.sleep(1)
        print()
    whenDone()

try:
    main()
except KeyboardInterrupt:
    whenDone()
