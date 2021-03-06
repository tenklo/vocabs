import random
import time
import vocabulary as v


vokabeln = v.currentVocabs
trainingsmode = True
mode = 2   # choose number from 0-2, depending on which mode you want (see manual)
_mode=0    #not to mess with, shouldnt matter if you do tho

def toggleTrainingsmode():
    global trainingsmode
    if trainingsmode == True:
        trainingsmode = False
        print("Trainingsmodus deaktiviert")
    else:
        trainingsmode = True
        print("Trainingsmodus aktiviert")

def whenDone():
    global counter
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
    print("-t    toggle Trainingsmodus (falsche Antworten müssen erneut getippt werden)")
    print("-d 0/1/2    Wechsel zwischen 0: englisch - deutsch, 1: deutsch - englisch, 2: zufällig")
    print("-e    Beende das Programm")


def process(vok,w,countertried,wrong,firstRun=True):
    global counter, mode, _mode
    if mode == 0:
        _mode = 0
    elif mode == 1:
        _mode = 1
    elif mode == 2 and firstRun==True:
        _mode = random.randrange(0,2)

    if _mode == 0:    
        print("englisch: "+vok)    
        guess=input()
        if guess == w:
            print ("Richtig: "+ vok + " = "+ w)
            if firstRun:
                counter+=1
        elif guess == "-t":
            toggleTrainingsmode()
            process(vok,w,countertried,wrong)
        elif guess == "-d 0":
            mode = 0
            print("englisch - deutsch aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-d 1":
            mode = 1
            print("deutsch - englisch aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-d 2":
            mode = 2
            print("Zufallsmodus aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-e":
            exit()
        elif guess == "-man":
            manual()
            process(vok,w,countertried,wrong)
        elif guess == "-l":
            print(str(countertried) +" von "+str(len(vokabeln))+" Vokabeln bearbeitet.")
            process(vok,w,countertried,wrong)
        elif guess=="":
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            if not vok in wrong:
                wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,countertried,wrong, False)
        elif guess in w:
            print("Gut. Korrekt ist: "+vok+" = " + w) 
            if firstRun:
                counter+=1
        else:
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            if not vok in wrong:
                wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,countertried,wrong,False)

    if _mode == 1:    
        print("deutsch: "+w)    
        guess=input()
        if guess == vok:
            print ("Richtig: "+ vok + " = "+ w)
            if firstRun:
                counter+=1
        elif guess == "-t":
            toggleTrainingsmode()
            process(vok,w,countertried,wrong)
        elif guess == "-d 0":
            mode = 0
            print("englisch - deutsch aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-d 1":
            mode = 1
            print("deutsch - englisch aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-d 2":
            mode = 2
            print("Zufallsmodus aktiviert")
            process(vok,w,countertried,wrong)
        elif guess == "-e":
            exit()
        elif guess == "-man":
            manual()
            process(vok,w,countertried,wrong)
        elif guess == "-l":
            print(str(countertried) +" von "+str(len(vokabeln))+" Vokabeln bearbeitet.")
            process(vok,w,countertried,wrong)
        elif guess=="":
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,countertried,wrong, False)
        elif guess in vok:
            print("Gut. Korrekt ist: "+vok+" = " + w) 
            if firstRun:
                counter+=1
        else:
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)
            if trainingsmode == True:
                time.sleep(1)
                process(vok,w,countertried,wrong,False)

def main():
    global counter , countertried, wrong, trainingsmode
    counter = 0
    countertried = 0
    wrong =[]
    print("\n\n")
    print(str(len(vokabeln))+" Vokabeln stehen an. Gib -man für das Manual ein.")
    if mode == 0:
        print("englisch - deutsch aktiviert.")
    elif mode == 1:
        print("deutsch - englisch aktiviert.")
    elif mode == 2:
        print("Zufallsmodus aktiviert.")
    if trainingsmode == True:
        print("Trainingsmodus ist aktiviert.")
    print("\n\n")
    for vok, w in sorted(vokabeln.items(), key =lambda x: random.random()):
        process(vok, w,countertried,wrong)
        countertried+=1
        time.sleep(1)
        print()

try:
    main()
except UnicodeError:
    print("ascii/Sonderzeichen/utf-8 Problem. Das Programm mit PYTHONIOENCODING=utf-8 aufzurufen ist ein fix")
except KeyboardInterrupt:
    pass
finally:
    whenDone()
