import random
import time
import vocabulary as v


vokabeln = v.currentVocabs
trainingsmode = True

def toggleTrainingsmode():
    global trainingsmode
    if trainingsmode == True:
        trainingsmode = False
        print("Trainingsmode deaktiviert")
    else:
        trainingsmode = True
        print("Trainingsmode aktiviert")

def whenDone():
    text="\nGute Arbeit. " + str(counter) + " von " + str(countertried)+ " Vokabeln richtig bearbeitet."
    if (countertried - counter)==1:
        text= text +" An dieser Vokabel musst du noch arbeiten:"
    elif countertried == 0:
        text="\nMit der Einstellung wird das nichts."
    elif counter != countertried:
        text= text+ " An diesen Vokabeln musst du noch arbeiten:" 
    elif counter == countertried:
        text=text+"\nDamit hast du alles richtig! Bekommst du das nochmal hin?"
    print (text)
    for vok in wrong:
        print(vok," = ", vokabeln[vok])

def manual():
    print("Du hast folgende Optionen:")
    print("-l    Lasse ausgeben, wie viele Vokabeln bearbeitet wurden und wie viele noch anstehen")
    print("-t    toggle trainingsmode (falsche Antworten müssen erneut getippt werden)")
    print("-e    Beende das Programm")


def process(vok,w,counter,countertried,wrong):
        print(vok)    
        guess=input()
        
        if guess == w:
            print ("Richtig: "+ vok + " = "+ w)
            counter+=1
        elif guess == "-t":
            toggleTrainingsmode()
            process(vok,w,counter,countertried,wrong)
        elif guess == "-e":
            exit()
        elif guess == "-man":
            manual()
            process(vok,w,counter,countertried,wrong)
        elif guess == "-l":
            print(str(countertried) +" von "+str(len(vokabeln))+" Vokabeln bearbeitet.")
            process(vok,w,counter,countertried,wrong)
        elif guess=="":
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,counter,countertried,wrong)
        elif guess in w:
            print("Gut. Korrekt ist: "+vok+" = " + w) 
            counter+=1
        else:
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,counter,countertried,wrong)

def main():
    global counter , countertried, wrong, trainingsmode
    counter = 0
    countertried = 0
    wrong =[]
    print(str(len(vokabeln))+" Vokabeln stehen an. Gib -man für das Manual ein.")
    if trainingsmode == True:
        print("Trainingsmode ist aktiviert.")
    for vok, w in sorted(vokabeln.items(), key =lambda x: random.random()):
        process(vok, w,counter,countertried,wrong)
        countertried+=1
        time.sleep(1)
        print()
    whenDone()

try:
    main()
except KeyboardInterrupt:
    whenDone()
