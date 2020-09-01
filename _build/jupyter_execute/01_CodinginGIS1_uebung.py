# Einleitung

Noch ein kurzer Hinweis zur Typografie dieses Dokumentes:

- Wenn sich im Fliesstext (Python oder ) Code befindet, wird `dieser Festschriftart` mit grauem Hintergrund dargestellt
- Alleinstehende Codezeilen werden  !! HIER NOCH BESCHREIBEN!!!
- Englische Fachbegriffe, deren Übersetzung eher verwirrend als nützlich sein würde, werden *kursiv* hervorgehoben
- Für R-Nutzer stelle ich den Vergleich zur R-Programmiersprache her. Wer wenig Erfahrung in R hat kann diese Teile ignorieren


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

## Übung 3: Elemente aus Liste ansprechen

Wie erhältst du den ersten Eintrag in der Variable `vornamen`? Wie erhältst du den letzten Eintrag? Tipp: nutze dazu `[` und `]` sowie eine Zahl.

**Für R Nutzer**: In R werden Elemente aus Vectors auf die gleiche Weise extrahiert. Nur ist in R das erste Element die Nummer 1, Python beginnt bei 0 

## Übung 4: Liste ergänzen

Listen können durch der Method `append` ergänzt werden.


```
vornamen.append("Frank")
```

Ergänze in die Listen `vornamen`, `nachnamen` und `groessen` durch je einen Eintrag.

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

## Übung 6: Elemente aus Dictionary ansprechen

Rufe verschiedene Elemente aus der Dictionary via dem *Key* ab.

## Übung 7: Key ergänzen

Um einer *Dictionary* mit einem weiteren Eintrag zu ergänzen, geht man sehr ähnlich vor wie beim Abrufen von Einträgen. Ergänze gemäss nachstehendem Beispiel die Variable `me` durch den Eintrag `groesse`.

langenscheidt["trumpet"] = "trompete" 

**Für R Nutzer**: Python *Dictionaries* werden nicht nur gleich abgerufen wie R *Lists*, sonder auch gleich ergänzt.

## Input: Dictionary (Teil II)

Ein *Key* kann auch mehrere Einträge enthalten. An unserem Langenscheidts Beispiel: Das Wort "trump" ist zwar eindeutig, doch "trumpery" hat vier verschiedene Bedeutungen. In so einem Fall können wir einem Eintrag auch eine *List* von Werten zuweisen. Beachte die Eckigen Klammern und die Kommas, welche die Listeneinträge voneinander trennt.

langenscheidt["trumpery"] = ["Plunder- Ramsch- Schund", "Gewäsch- Quatsch", "Schund- Kitsch", "billig- nichtssagend"]    
langenscheidt["trumpery"]

## Übung 8: Dictionary mit List

Erstelle eine neue Dictionary mit den gleichen Keys wie `me`, aber diesmal mit mehreren Einträgen pro *Key* (also mehreren Vornamen, Nachnamen usw.). Beachte, dass nun jeder Eintrag eine *List* sein muss. Weise diese Dictionary der Variabel `people` zu.

## Übung 9: Functions

Bisher haben wir Objekte erstellt. Richtig interessant wird programmieren aber erst, wenn wir mit Objekte durch Funktionen (*Functions*) verändern. *Functions* führen bestimmte Tasks aus. Wende die Functions `list()`, `len()` und `sum()` an den Listen groesse und vornamen an. 

# Python Modules

Ähnlich wie R basiert Python auf Erweiterungen: Diese Erweiterungen heissen in R *Libraries* / *Packages*, in Python werden sie *Modules* genannt. Sie sind dazu da, gewisse Teilbereiche unseres Arbeitsprozesses zu vereinfachen. Eine Analogie dazu: Um ein Haus zu bauen sind wir auf verschiedene Spezialisten / Spezialistinnen angewiesen: Wir brauchen zum Beispiel eine Malerin oder einen Maler. Im Telfonbuch sind seitenweise Maler\*innen aufgelistet, und jede\*r arbeitet etwas anders. Um eine spezifische Malerin anzuheuern müssen wir zuerst den Kontakt herstellen und die Vertragsmodalitäten vereinbaren. Erst dann können wir sie in unseren Arbeitsprozess (Haus bauen) einbinden.

Um diese Analogie auf unser Projekt zu übertragen: Das "Haus bauen" ist unser Forschungsprojekt (z.B. eine Bachelorarbeit). Ein "Telefonbuch", wo die Spezialisten erfasst sind nennt ein *Reposoritory*. Den Erstkontakt mit der Malerin zu erstellen und die Vertragsmodalitäten zu vereinbaren bedeutet, die Erweiterung zu installieren. In R wird eine Erweiterung folgendermassen installiert:

```
install.packages("malerinMina")
```
In diesem Beispiel heisst die Erweiterung `malerinMina`. Das *Reposoritory* geben wir in R oft nicht an, weil in RStudio typischerweise schon eine Adresse hinterlegt ist. Wie wir in Python ein Modul installieren lernen wir später. Nehmen wir an dieser Stelle an, wir haben die Erweiterung `malerinMina` in Python installiert. Treiben wir an dieser Stelle die Analogie etwas weiter: Der Erstkontakt mit der Kleptnerin ist also erstellt und alle Vertragsmodalitäten sind vereinbart. Nun wollen wir an einem bestimmten Tag mit ihr arbeiten. Dafür müssen wir sie zuerst auf die Baustelle bestellen. Übersetzt auf programmieren bedeutet dies, wir müssen die Erweiterung in unsere Session laden. In R sieht der Befehl so aus:

```
library(malerinMina)
```

In Python lautet der entsprechende Befehl:

```
import malerinMina
```

Erst jetzt können wir mit der Erweiterung arbeiten und die Fachexpertise unserer Malerin nutzen. Eine Expertise unserer Malerin ist es, Wände zu bemalen. Dafür gibt es eine *Function* `wand_bemalen()`. In R kann ich diese *Function* "einfach so" aufrufen:

```
wand_bemalen()
```

In Python hingegen muss ich die Erweiterung, in der die *Function* enthalten ist, der *Function* mit einem Punkt voranstellen. Das sieht also folgendermassen aus:

```
malerinMina.wand_bemalen()
```

Das ist zwar umständlicher, aber dafür weniger Fehleranfällig. Angenommen, unser Maurer kann ebenfalls Wände bemalen und hat die entsprechende *Function* `wand_bemalen()` ebenfalls. Dann ist in R nicht klar, welche Erweiterung gemeint ist und das kann zu Missverständnissen führen (vielleicht bemalt der Mauerer die Wände etwas anders als die Malerin). In Python ist im obigen Beispiel unmissverständlich, dass ich `wand_bemalen()` aus dem Modul `malerinMina` meine.

**Das wichtigste in Kürze**
- Erweiterungen heissen in Python *Modules*
- Vor der erstmaligen Nutzung muss ein *Module* installiert werden
- Vor der Verwendung in einer Session muss ein *Module* "geladen" werden. Dies muss für jede Session wiederholt werden!
- Ein *Module* wird in Python mit `import modulename` geladen
- Eine *Function* aus einem *Module* wird folgendermassen aufgerufen: `modulname.function()`

## Modul mit Alias importieren

Wenn es uns zu Umständlich ist jedesmal `malerinMina.wand_bemalen()` voll auszuschreiben können wir beim Importieren dem Modul auch einen "Alias" vergeben. Dies kann beispielsweise folgendermassen aussehen:

```
import malerinMina as mm
mm.wand_bemalen()
```

Dies ist deshalb wichtig, weil sich für viele Module haben sich bestimmte Aliasse eingebürgert haben. Ihr macht sich das Leben leichter, wenn ihr euch an diese Konventionen (welche ihr noch kennenlernen werdet) hält.

## Einzelne *Function* importieren

Was man auch noch machen kann, ist eine explizite *Function* aus einem Modul zu laden. Wenn man dies macht, kann man die Funktion ohne vorangestelltes Modul nutzen (genau wie in R). Dies sieht folgendermassen aus:

```
from malerinMina import wand_bemalen()
wand_bemalen()
```



```{toctree}
:hidden:
:titlesonly:


Untitled
```
