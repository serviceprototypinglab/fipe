"""
Das nachfolgende Skript führt eine mathematische Berechnung gemäss einer
spezifischen Formel durch. Die Formel muss nicht weiter verstanden werden.
Vervollständigen Sie das Skript an den kommentierten Stellen, so dass
es lauffähig wird und schliesslich das Resultat ausgibt.
Etwas 'Tüfteln' und aufmerksames Lesen von Python-Fehlermeldungen
ist dabei hilfreich.

(20 Punkte - je 2 Punkte pro korrekter Vervollständigung)
"""

import math
# Vervollständigung V1: Modul für numerisches Rechnen importieren (2P)

fixpoint_array = [
    1.0036784723520398,
    1.0046843389945894,
    1.0042146074100489,
    0.9976506126739353,
    1.004628260985105,
    0.99796357703{VARY:448}79,
    1.0043510357919885,
    0.9951575774279858,
    1.0026486757629631,
    1.0011646109142465
]

# Vervollständigung V2: Schlüsselwort für Klassen (2P)
ConvergenceCalculation:
    # Vervollständigung V3: Parameter für Konstruktormethode (2P)
    def __init__:
        self.const_a = 1.492582
        self.const_b = 2994.13952094
        self.const_c = 999324.24942325669
        self.const_d = math.e + math.sin(self.const_a) - 0.23599352

    # Vervollständigung V4: Methodendefinition siehe Aufrufe unten (2P)
    def :
        self.array = np.array(fixpoint_array)

    def calculate(self):
        x = self.const_a * self.const_b + self.const_b
        y = self.const_a * self.const_d + self.const_b
        # Vervollständigung V5: Ergebnisattribut (2P)
        self. = (x + y) * np.mean(self.array)

    def validate(self):
        # Vervollständigungen V6/V7: mit Assertions prüfen, ob Ergebnis im gültigen Bereich liegt (2 x 2P)
        self.result > 10000
        self.result < 11000

    def output(self):
        # Vervollständigung V8: Ergebnis auf Standardausgabe schreiben (2P)
        (round(self.result))

if __name__ == "__main__":
    # Vervollständigung V9: Objekt instanziieren (2P)
    c = ()
    c.precalculate()
    c.calculate()
    c.validate()
    # Vervollständigung V10: Ergebnisausgabe (2P)
