%% ALL -
"""
Gegeben sei die Datei sneaker.json mit 50 Sneakern. Für jedes Produkt
ist der Name (displayName), der Preis (price) und die Farbe (color) abgelegt.

Die Produkte sollen mit Pandas ausgewertet werden. Nutzen Sie die
Onlinedokumentation zum Pandas-Modul bei allfälligen Unklarheiten
zu Methoden:
 https://pandas.pydata.org/docs/user_guide/basics.html
 https://pandas.pydata.org/docs/user_guide/visualization.html

(15 Punkte insgesamt)
"""

# -------------------------------------------------------------------------

%% ALL df
"""
Lesen Sie zuerst die Datei ein und erstellen Sie ein Pandas DataFrame
namens 'df', in welchem die Produkteigenschaften als Spalten abgelegt sind.
Nutzen Sie dafür die Modulmethode read_json.

(2 Punkte für das Einlesen)
"""

# ... Ihre Lösung hier: df = ...

# -------------------------------------------------------------------------

%% A3 df_black
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, deren Farbe schwarz (Black) ist.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_black = ...
print("-- Schwarze Schuhe --")
print(df_black)

%% A3 df_blue
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, deren Farbe blau (Blue) ist.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_blue = ...
print("-- Blaue Schuhe --")
print(df_blue)

%% A3 df_preis180
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, deren Preis 180 ist.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_preis180 = ...
print("-- Schuhe mit Preis 180 --")
print(df_preis180)

%% A3 df_preis110
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, deren Preis 110 ist.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_preis110 = ...
print("-- Schuhe mit Preis 110 --")
print(df_preis110)

%% A3 df_wander
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, die explizit als Wanderschuhe bezeichnet sind.
Hinweis: Sie müssen hierzu ".str" an die zu filternde Spalte anhängen,
um String-Methoden darauf anwenden zu können.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_wander = ...
print("-- Wanderschuhe --")
print(df_wander)

%% A3 df_lauf
"""
Geben Sie ein DataFrame auf der Konsole aus, welches nur die Produkte
enthält, die explizit als Laufschuhe bezeichnet sind.
Hinweis: Sie müssen hierzu ".str" an die zu filternde Spalte anhängen,
um String-Methoden darauf anwenden zu können.
(3 Punkte)
"""
# ... Ihre Lösung hier: df_lauf = ...
print("-- Laufschuhe --")
print(df_lauf)

%% B1 plot_plot
"""
Erstellen Sie einen Plot, in welchem der Preis für alle Produkte
aufsteigend als Linie angezeigt wird.
(4 Punkte)
"""
# ... Ihre Lösung hier (basierend auf df)
import pylab
pylab.savefig("plot_plot.png")

%% B1 plot_boxplot
"""
Erstellen Sie einen Boxplot, welcher die Verteilung aller Preise
inklusive Minimum, Maximum und Median anzeigt.
(4 Punkte)
"""
# ... Ihre Lösung hier (basierend auf df)
import pylab
pylab.savefig("plot_boxplot.png")
