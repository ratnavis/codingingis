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
