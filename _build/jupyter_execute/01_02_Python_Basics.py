# Python Basics

## Übung 1: Variablen erstellen

Wir beginnen damit, einfache Datentypen wie Zahlen, Text, boolsche Variabeln (siehe Vorlesungsfolien) sogenannten Variablen zu zuweisen. Führe die folgenden Schritte aus und schau dir nach jedem Schritt die erstellten Variablen jeweils im im Variable explorer von Spyder an

1. Erstelle eine Variabel vorname mit deinem Vornamen
2. Erstelle eine zweite Variabel nachname mit deinem Nachnamen
3. Was sind vorname und nachname für Datentypen?
4. Klebe die beiden Variabeln zusammen, ohne den Output zu speichern
5. Erstelle eine Variabel groesse mit deiner Körpergrösse in Zentimeter auf Zentimeter genau. Was ist das für ein Datentyp?
6. Ermittle deine Grösse in Meter auf der Basis von groesse. Was ist das für ein Datentyp?
7. Erstelle eine boolsche Variable blond und setzte sie auf True wenn diese Eigenschaft auf dich zutrifft und False falls nicht. 


**Für R Nutzer**:
- In R gibt es die gleichen Primitiven Datentypen wie in Python: Boolean, String, Integer, Float. Die Bezeichnung ist jedoch leicht anders (Logical, Character, Integer, Numeric, Double)
- In R können Variablen genau gleich zugewiesen werden wie in Python (mit dem `=` Symbol). In R gibt es zudem noch die Möglichkeit, Variablen mit `<-` zu zuweisen, in Python jedoch nicht 


## Übung 2: Lists

1. Erstelle eine Variable `vornamen` bestehend aus einer *List* mit 3 Vornamen
2. Erstelle eine zweite Variable `nachnamen` bestehend aus einer *List* mit 3 Nachnamen
3. Erstelle eine Variable `groessen` bestehend aus einer *List* mit 3 Grössenangaben in Zentimeter.

**Für R Nutzer**: Eine Python List entspricht eines R Vectors 

vornamen = ["Christopher", "Henning", "Severin"]
nachnamen = ["Annen","May", "Kantereit"]

groessen = [174, 182, 162]

## Übung 3: Elemente aus Liste ansprechen

Wie erhältst du den ersten Eintrag in der Variable `vornamen`? Wie erhältst du den letzten Eintrag? Tipp: nutze dazu `[` und `]` sowie eine Zahl.

**Für R Nutzer**: In R werden Elemente aus Vectors auf die gleiche Weise extrahiert. Nur ist in R das erste Element die Nummer 1, Python beginnt bei 0 

## Übung 4: Liste ergänzen

Listen können durch der Method `append` ergänzt werden.


vornamen.append("Malte")

Ergänze in die Listen `vornamen`, `nachnamen` und `groessen` durch je einen Eintrag.

nachnamen.append("Huck")

groessen.append(177)

## Input: Dictionary (Teil I)

Ähnlich wie eine List, ist eine Dictionary ein Behälter wo mehrere Elemente abgespeichert werden können. Wie bei einem Wörterbuch bekommt jedes Element ein "Schlüsselwort", mit dem man den Eintrag finden kann. 
Unter dem Eintrag "trump" findet man im Langenscheidt Wörterbuch (1977) die Erklärung "erdichten, schwindeln, sich aus den Fingern saugen".  

![](trump.jpg)

In Python würde man diese *Dictionary* folgendermassen erstellen:

langenscheidt = {"trump":"erdichten- schwindeln- sich aus den Fingern saugen"}

Schlüssel (von nun an mit *Key* bezeichnet) des Eintrages lautet "trump" und der dazugehörige Wert (*Value*) "erdichten- schwindeln- aus den Fingern saugen". Beachte die geschweiften Klammern (`{` und `}`) bei der Erstellung einer Dictionary.

Eine *Dictionary* besteht aber meistens nicht aus einem, sondern aus mehreren Einträgen: Diese werden Kommagetrennt aufgeführt. 

langenscheidt = {"trump":"erdichten- schwindeln- sich aus den Fingern saugen", "trumpery":"Plunder- Ramsch- Schund"}

Der Clou der *Dictionary* ist, dass man nun einen Eintrag mittels dem *Key* aufrufen kann. Wenn wir also nun wissen wollen was "trump" heisst, ermitteln wir dies mit der nachstehenden Codezeile:  

langenscheidt["trump"]

**Für R Nutzer**: Eine Python *Dictionary* entspricht einer R *List*. Diese werden in R nicht gleich erstellt, dafür aber auf die gleiche weise abgefragt wie *Dictionaries* in Python

## Übung 5: Dictionary

Erstelle eine *Dictionary* mit folgenden Einträgen: Vorname und Nachname von (d)einer Person. Weise diese Dictionary der Variable `me` zu.

me = {"vorname": "Charles", "nachname": "Darwin"}

## Übung 6: Elemente aus Dictionary ansprechen

Rufe verschiedene Elemente aus der Dictionary via dem *Key* ab.

me["vorname"]

me["nachname"]

## Übung 7: Key ergänzen

Um einer *Dictionary* mit einem weiteren Eintrag zu ergänzen, geht man sehr ähnlich vor wie beim Abrufen von Einträgen. 

langenscheidt["trumpet"] = "trompete" 

Ergänze gemäss nachstehendem Beispiel die Variable `me` durch den Eintrag `groesse`. 

**Für R Nutzer**: Python *Dictionaries* werden nicht nur gleich abgerufen wie R *Lists*, sonder auch gleich ergänzt.

me["groesse"] = 181

## Input: Dictionary (Teil II)

Ein *Key* kann auch mehrere Einträge enthalten. An unserem Langenscheidts Beispiel: Das Wort "trump" ist zwar eindeutig, doch "trumpery" hat vier verschiedene Bedeutungen. In so einem Fall können wir einem Eintrag auch eine *List* von Werten zuweisen. Beachte die Eckigen Klammern und die Kommas, welche die Listeneinträge voneinander trennt.

langenscheidt["trumpery"] = ["Plunder- Ramsch- Schund", "Gewäsch- Quatsch", "Schund- Kitsch", "billig- nichtssagend"]    
langenscheidt["trumpery"]

## Übung 8: Dictionary mit List

Erstelle eine neue Dictionary mit den gleichen Keys wie `me`, aber diesmal mit mehreren Einträgen pro *Key* (also mehreren Vornamen, Nachnamen usw.). Beachte, dass nun jeder Eintrag eine *List* sein muss. Weise diese Dictionary der Variabel `people` zu.

people = {"vornamen": ["Christopher", "Henning", "Severin"], "nachnamen": ["Annen","May", "Kantereit"], "groessen": [174, 182, 162]}

## Übung 9: Functions

Bisher haben wir Objekte erstellt. Richtig interessant wird programmieren aber erst, wenn wir mit Objekte durch Funktionen (*Functions*) verändern. *Functions* führen bestimmte Tasks aus. Wende die Functions `len()` und `sum()` an den Listen `groessen` und `vornamen` an. 

len(groessen)

sum(groessen)

len(vornamen)

# sum(vornamen)