import random
import time
import vocabulary as v


vokabeln = v.ersterVokabeltest


def whenDone():
    text="\nGute Arbeit. " + str(counter) + " von " + str(countertried)+ " Vokabeln richtig bearbeitet."
    if (countertried - counter)==1:
        text= text +" An dieser Vokabel musst du noch arbeiten:"
    elif countertried == 0:
        text="\nMit der Einstellung wird das nichts."
    elif counter != countertried:
        text= text+ " An diesen Vokabeln musst du noch arbeiten:" 
    elif counter == countertried:
        text=("\nAlles richtig! Bekommst du das nochmal hin?")
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
        elif guess == "e":
            whenDone()
            break
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
