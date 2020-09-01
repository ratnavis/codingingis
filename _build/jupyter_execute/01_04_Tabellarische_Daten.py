# Tabellarische Daten

Schauen wir uns nochmals die *Dictionary* `people` an. Diese ist ein Spezialfall einer Dictionary: Jeder Eintrag besteht aus einer Liste von gleich vielen Werten. Diese Dictionary schreit förmlich danach, tabellarisch dargestellt zu werden. Dies wollen wir gewähren und brauchen dafür das Modul `pandas`. Importiere das Modul mit dem Alias `pd`.

!! ACHTUNG: HIER FEHLT NOCH DIE EINFÜHRUNG INSTALLATION VON MODULEN !!

## Übung 1: von einer *Dictionary* zu einer *DataFrame*

Wandle die Dictionary `people` in eine DataFrame um: Dazu musst du `people` als Argument der Funktion `DataFrame` übergeben: `pd.DataFrame(people)`. Weise den Output der Variable `people_df` zu. 

**Für R Nutzer**: Auch in R gibt es *Dataframes*, diese sind aber in Base R integriert (brauchen deswegen keine Erweiterung wie `pandas`)

people = {"vornamen": ["Christopher", "Henning", "Severin"], "nachnamen": ["Annen","May", "Kantereit"], "groessen": [174, 182, 162]}

! Ab hier wird pandas benötigt !

import pandas as pd

people_df = pd.DataFrame(people)

## Übung 2: *DataFrame* in csv umwandeln

In der Praxis kommen Tabellarische Daten meist als «csv» Dateien daher. Wir können aus unserer eben erstellten DataFrame sehr einfach eine csv Datei erstellen. Führe das mit folgendem Code aus:

people_df.to_csv("people.csv")

## Übung 3: CSV als *DataFrame* importieren

Genau so einfach ist es eine csv zu importieren. Lade dazu die Datei "zeckenstiche.csv" von Moodle herunter und speichere es im aktuellen Arbeitsverzeichnis ab. Importiere mit folgendem Code die Datei "zeckenstiche.csv". Schau dir `zeckenstiche` nach dem importieren an.

zeckenstiche = pd.read_csv("zeckenstiche.csv")

**Hinweis**: Dieser Code funktioniert nur, wenn "zeckenstiche.csv" im aktuellen Arbeitsverzeichnis (*Current Working Directory*) abgespeichert wird. Wenn du nicht sicher bist, wo dein aktuelles Arbeitsverzeichnis liegt, kannst du das Modul `os` laden und dies mit der Funktion `os.getcwd()` (get **c**urrent**w**orking**d**irectory) herausfinden.

import os

os.getcwd()

## Übung 4: Koordinaten räumlich darstellen

Die *DataFrame* `zeckenstiche` beinhaltet x und y Koordinaten für jeden Unfall in den gleichnamigen Spalten. Wir können die Stiche mit einem Scatterplot räumlich visualisieren. Führe dazu folgenden Code aus:


! Ab hier wird matplotlib benötigt !

zeckenstiche.plot.scatter("x","y")

## Übung 5: Einzelne Spalte selektieren

Um eine einzelne Spalte zu selektieren (z.B. die Spalte "ID") kann man gleich vorgehen wie bei der Selektion eines Eintrage in einer *Dictionary*. Probiere es aus.

zeckenstiche["ID"]

## Übung 6: Neue Spalte erstellen

Auch das Erstellen einer neuen Spalte ist identisch mit der Erstellung eines neuen *Dictionary* Eintrags. Folgende Zeile erstellt eine neue Spalte "Stichtyp" mit dem gleichen Wert in allen Zeilen ("Zecke"). Erstelle ebenfalls eine solche Spalte.


zeckenstiche["Stichtyp"] = "Zecke"

zeckenstiche