moduleOneA = {
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
    "to swap": "tauschen",
}

amazonSheet ={
    "high-rise": "Hochhaus",
    "to range": "reichen, sich bewegen zwischen",
    "reportedly": "angeblich, wie gemeldet",
    "recent": "neu, letzte",
    "to promote": "verbreiten",
    "discriminatory practice": "diskriminierende Praxis",
    "retail": "Einzelhandel",
    "to debit": "abbuchen",
    "receipt": "Beleg, Quittung",
    "to dive into": "eintauchen",
    "mock": "Probe- / Schein-",
    "bottleneck": "Nadelöhr, Flaschenhals",
    "to defeat": "zerschlagen, besiegen",
    "intention": "Absicht",
    "line": "(Warte-)Schlange",
    "to tinker": "tüfteln",
    "counter": "Theke",
    "holdup": "Verzögerung",
    "to shrink": "schrumpfen",
    "bullish": "stur",
    "to fall short of": "hinter etwas zurückbleiben",
    "attempt": "Versuch",
    "grocery": "Lebensmittel",
    "according to": "laut",
    "permit": "Zulassung",
    "to abandon": "verlassen",
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


def fuseDicts(listOfDicts):
    output={}
    for dictio in listOfDicts:
       for key, val in dictio.items():
            if key not in output:
                output[key]=val
            else:
                output[key]=output[key]+", "+val

    return output


ersterVokabeltest= fuseDicts([moduleOneA , amazonSheet])
#put the vocabs you actually want to practice here:
currentVocabs=ersterVokabeltest
