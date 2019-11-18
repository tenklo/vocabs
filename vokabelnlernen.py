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

mehrVokabeln={
    "apprenticeship": "Lehre, Ausbildung",
    "tutor": "Klassenlehrer, Betreuer",
    "organigram": "Organigramm",
    "curious": "neugierig",
    "major": "Haupt-, bedeutend",
    "separate": "einzeln, gesondert",
    "sheet": "Blatt",
    "corporate": "Firmen-, Unternehmens-",
    "enterprise": "Unternehmen",
    "actually": "eigentlich, tatsächlich",
    "workshop": "Werkstatt",
    "faulty": "fehlerhaft, mangelhaft",
    "to join": "beitreten, mitmachen, sich jemandem anschließen, mitkommen",
    "premises": "Firmengelände",
    "to refer sb. to sb./sth.": "jemanden an jemanden/ auf etwas verweisen",
    "to implement": "ausführen, verwirklichen, realisieren",
    "Human Resources": "Personalabteilung",
    "accounting": "Buchhaltung",
    "stockkeeping": "Lagerhaltung",
    "reminder": "Erinnerung, Mahnung",
    "to match": "zuordnen",
    "purchase": "Kauf, Erwerb",
    "to assess": "bewerten, einschätzen, abschätzen",
    "faulty": "defekt",
    "customer field service": "Kundendienst",
    "enquiry": "Anfrage",
    "order": "Bestellung, Auftrag",
    "offer": "Angebot",
    "description": "Beschreibung",
    "stay": "Aufenthalt",
    "organisation chart (org chart)": "Organigramm, OrganisationsschemOrganigramm, Organisationsschema"
}



vokabeln = ersterVokabeltest


def whenDone():
    text="\nGute Arbeit. " + str(counter) + " von " + str(countertried)+ " Vokabeln richtig bearbeitet."
    if (countertried - counter)==1:
        text= text +" An dieser Vokabel musst du noch arbeiten:"
    elif counter != countertried:
        text= text+ " An diesen Vokabeln musst du noch arbeiten:" 
    elif counter == countertried:
        text=("Alles richtig! Bekommst du das nochmal hin?")
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
        elif guess=="":
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
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
