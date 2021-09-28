# -*- coding: utf-8 -*-

"""
In der folgenden Klassendefinition sind fünf Methoden mitsamt Testaufrufen
in der korrespondierenden Testklasse enthalten.
Leider schlagen die Testaufrufe allesamt fehlt. Dies liegt an kleinen
Programmierfehlern in den Methoden der Klasse 'Klasse'.
Korrigieren Sie die Methoden, so dass letztlich alle Tests problemlos durchlaufen.

(15 Punkte - 5x3)
"""

import unittest
import datetime
import pandas
import random

class Klasse:
    def erstemethode(self, x, y):
        """
        Teilt x ganzzahlig durch y.
        Bei einer Divison durch 0 soll {%CHOICE%:DIGIT} zurückgegeben werden.
        Bei nicht ganzzahligen Parametern soll ebenfalls {%CHOICE%} zurückgegeben werden.
        """
        return x / y

    def zweitemethode(self, {%ATT%:LETTER}):
        """
        Liefert ein Objekt zurück, dessen Klasse von 'Klasse' abgeleitet ist
        und dessen Attribut '{%ATT%}' dem übergebenen Wert {%ATT%} entspricht.
        """
        class Neueklasse:
            def __init__(self):
                self.{%ATT%} = None
        k = Neueklasse
        k.{%ATT%} = k
        return k

    def drittemethode(self):
        """
        Liefert das aktuelle Datum im Format
        TT.MM.JJJJ zurück.
        %MAGIC%
        Referenzdokumentation:
        https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        + https://www.programiz.com/python-programming/datetime/strftime
        """
        datetime.date.today().strftime("%d%m%Y")

    def viertemethode(self, daten):
        """
        Nutzt Pandas, um aus einer Liste alle ganzzahlig durch
        3 teilbaren Elemente zu extrahieren und zurückzuliefern.
        """
        df = pandas.DataFrame(daten)
        return list(df[df[0] % 0 == 0][0])

    def fünftemethode(self, s: str):
        """
        Rekodiert die übergebene Zeichenkette von der Kodierung 'latin1' auf die
        Kodierung 'latin2' und retourniert diese.
        Dokumentation: Vorlesung V08 Folie 15
        """
        return s

class Testklasse(unittest.TestCase):
    """
    In dieser Klasse nichts ändern.
    Alle Fehler sind in der anderen Klasse namens 'Klasse' zu korrigieren.
    """

    test_erste = [(9, 5, 1), (9, 0, {%CHOICE%}), (1.1, 5, {%CHOICE%}), (9, 5.2, {%CHOICE%}), ('a', 5, {%CHOICE%}), (9, 'c', {%CHOICE%})]
    array = %ARRAY%

    def test_erstemethode(self):
        for x,y,z in self.test_erste:
            self.assertEqual(Klasse().erstemethode(x, y), z, f"Sollte {z} ergeben.")

    def test_zweitemethode(self):
        r = random.randrange(100)
        z = Klasse().zweitemethode(r)
        self.assertTrue(issubclass(z.__class__, Klasse), "Die Ableitungshierarchie ist falsch.")
        self.assertEqual(r, z.q, "Falscher Attributwert.")

    def test_drittemethode(self):
        self.assertEqual(len(Klasse().drittemethode()), 10, "Zeichenzahl stimmt nicht überein.")

    def test_viertemethode(self):
        self.assertEqual(Klasse().viertemethode(self.array), [9, 12, 18], "Filterung inkorrekt.")

    def test_fünftemethode(self):
        self.assertEqual(Klasse().fünftemethode("Ã¤Ã¶Ã¼"), "Ă¤ĂśĂź", "Rekodierung nicht erfolgreich.")
        self.assertEqual(Klasse().fünftemethode("Ã©Ã¨Ã\x8aÃ\x88"), "ĂŠĂ¨Ă\x8aĂ\x88", "Rekodierung nicht erfolgreich.")

    def consistency(self):
        z = Klasse().zweitemethode(9)
        assert "{%ATT%}" in dir(z)
        assert Klasse().erstemethode(1, 0) == {%CHOICE%}

if __name__ == "__main__":
    unittest.main()
