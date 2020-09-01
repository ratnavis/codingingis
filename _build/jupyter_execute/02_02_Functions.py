# Functions

Bevor wir uns in die Simulation stürzen müssen wir noch lernen eigene *Functions* zu schreiben: Dies ist auch nicht weiter schwierig: Eine *Function* wird mit `def` eingeleitet, braucht einen Namen, einen Input und einen Output.

Wenn wir zum Beispiel eine Function erstellen wollen die uns grüsst, so geht dies folgendermassen:

def sag_hallo():
    return("Hallo!")

- Mit `def` sagen wir: "Jetzt definiere ich eine Function". 
- Danach kommt der Name der *Function*, in unserem Fall `sag_hallo` (mit diesem Namen können wir die *Function* später wieder abrufen). 
- Als drittes kommen die runden Klammern, wo wir bei Bedarf Inputvariablen (sogenannte Parameter) festlegen können. In diesem ersten Beispiel habe ich keine Parameter festgelegt
- Nach der Klammer kommt ein Doppelpunkt was bedeutet: "jetzt wird gleich definiert, was die Funktion tun soll"
- Auf einer neuen Zeile wird eingerückt festgelegt, was die Function eben tun soll. Meist sind hier ein paar Zeilen Code vorhanden
- Die letzte eingerückte Zeile (in unserem Fall ist das die einzige Zeile) gibt mit return an, was die *Function* zurück geben soll (der Output). In unserem Fall soll sie "Hallo!"  zurück geben.
- Voila, das war’s schon! Jetzt können wir diese Function schon nutzen:


sag_hallo()

Diese *Function* ohne Input ist wenig nützlich. Meist wollen wir der *Function* etwas - einen Input - übergeben können. Um eine *Function* zu erstellen die ein Argument annimmt geht man folgendermassen vor:

def sag_hallo(vorname):
    return("Hallo "+vorname+"!")

Nun können wir der Function einen Paramter übergeben, damit wir persönlich gegrüsst werden. In folgendem Beispiel ist `vorname` ein Parameter, "Charles" ist sein Argument.

sag_hallo("Charles")

Den Output können wir wie gewohnt einer neuen Variabel zuweisen:

persoenlicher_gruss = sag_hallo("Charles")
persoenlicher_gruss