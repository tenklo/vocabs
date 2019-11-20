import random
import time
import vocabulary as v


vokabeln = v.currentVocabs


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
    print("Du hast folgende Optionen:\n-l    Lasse ausgeben, wie viele Vokabeln bearbeitet wurden und wie viele noch anstehen\n-e    Beende das Programm")

def process(vok,w,counter,countertried,wrong):
        print(vok)    
        guess=input()
        
        if guess == w:
            print ("Richtig: "+ vok + " = "+ w)
            counter+=1
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
        elif guess in w:
            print("Gut. Korrekt ist: "+vok+" = " + w) 
            counter+=1
        else:
            print("Falsch. Korrekt ist: "+vok+" = " + w) 
            wrong.append(vok)

def main():
    print(str(len(vokabeln))+" Vokabeln stehen an. Gib -man für das Manual ein.")
    global counter , countertried, wrong
    counter = 0
    countertried = 0
    wrong =[]
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
