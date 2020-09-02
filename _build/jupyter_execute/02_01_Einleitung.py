# Einleitung zu diesem Block

Letzte Woche habt ihr einen weiten Bogen gespannt: Von einfachen (primitiven) Datentypen bis hin zu Geodaten und deren Visualisierung. In dieser und der nächsten Übung (Coding in GIS II und III) wollen wir uns weiter mit den Zeckenstichdaten befassen. Wir werden im Wesentlichen ein Teil der Übung aus «Datenqualität und Unsicherheit» in Python rekonstruieren. 
In der Übung geht es um folgendes: Wir wissen das die Lagegenauigkeit der Zeckenstichmeldungen mit einer gewissen Unsicherheit behaftet sind. Um die Frage "Welcher Anteil der der Zeckenstiche befinden sich im Wald?" unter Berücksichtigung dieser Unsicherheit beantworten zu können, führen wir eine (Monte Carlo) Simulation durch.
In dieser Simulation verändern wir die Position der Zeckenstichmeldungen zufällig und berechnen den Anteil der Zeckenstiche im Wald. Das zufällige Verschieben und berechnen wiederholen wir beliebig lange und bekommen für jede Wiederholung einen leicht unterschiedlichen Prozentwert. Die Verteilung dieser Prozentwerte ist die Antwort auf die ursprüngliche Frage ("Welcher Anteil...") unter Berücksichtigung der Unsicherheit.

Um eine solche, etwas komplexere Aufgabe lösen zu können müssen wir sie in einfachere Einzelschritte aufteilen. Diese bearbeiten wir in dieser und der kommenden Woche:

- Schritt 1: Einen Einzelpunkt zufällig verschieben
- Schritt 2: Alle Punkte einer GeoDataFrame zufällig verschieben (1 «Run»)
- Schritt 3: Alle Punkte einer GeoDataFrame mehrfach zufällig verschieben (z.B. 50 «Runs»)
- Schritt 4: Anteil der Punkte im Wald pro «Run» ermitteln
- Schritt 5: Verteilung dieser Mittelwerte visualisieren 



```{admonition} Übungsziele
:class: attention
- Functions kennenlernen und beherrschen
- Einfache Geometrien manipulieren lernen
- Eigene Python-Scripts importieren können
- Function auf eine ganze Spalte einer (Geo-) DataFrame anwenden können.
```