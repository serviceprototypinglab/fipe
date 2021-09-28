"""
Dieses objektorientierte Programm simuliert die Fussballbegegnung Finnland
gegen Belgien vom 21. Juni 2021. Leider hat der Programmierer bei aller
Euphorie vergessen, die beiden Klassen 'Spieler' und 'Ball' sowie in
der Klasse 'Game' die Methode 'setup' fertigzustellen.
Vervollständigen Sie die beiden Klassen und die Methode, um eine
lauffähige Simulation zu erhalten. Das Programm läuft dann erfolgreich
in einer Endlossimulation.
Hinweis: Führen Sie das Programm mehrfach auch und ziehen Sie Rückschlüsse
von den Fehlermeldungen auf fehlende Attribute. Die Klassen Spieler/Ball
enthalten jeweils nur die Konstruktormethode mit Attributzuweisungen.
%MAGIC%
(20 Punkte - 5 für Spieler, 6 für Ball, und 9 für setup)
"""

import time
import random
import itertools

class Spieler:
    """
    Spieler haben einen Namen, eine x/y-Position auf dem Feld
    und eine Zugehörigkeit zu einer Mannschaft.
    """

class Ball:
    """
    Der Ball hat eine x/y-Position auf dem Feld,
    einen x/y-Schussvektor (initial 0/0) und einen Verweis
    auf die ballbesitzende Mannschaft (initial keine).
    """

class Game:
    def __init__(self):
        # UEFA-Richtlinienmasse - beachten für die Positionierung von Ball/Spieler
        self.feld = (105, 68)
        # Mannschaften - beachten für die Spieleraufstellung
        self.begegnung = ("Finnland", "Belgien")
        # Spielerliste und Ball - diese Attribute werden in der setup-Methode gesetzt
        self.spieler = []
        self.ball = None

        # interne Attribute und Methoden, nicht relevant für die Aufgabenstellung
        self.stats = {}
        self.names = {}
        self.setup()
        self.check()
        self.aufstellung()

    def setup(self):
        """
        Setzt den Ball und alle Spieler auf das Spielfeld.
        Hinweis: Spielernamen können durch self.generiere_name
        automatisch erzeugt werden.
        """

        # 1. Ball setzen (self.ball, Objekt der Klasse Ball, Position zufällig im Feld)

        # 2. Spieler setzen (self.spieler, Liste mit Objekten der Klasse Spieler, Positionen zufällig im Feld)

    def check(self):
        assert len(self.spieler) == 22
        assert len(self.names) == 22
        for mannschaft in self.begegnung:
            assert len([s for s in self.spieler if s.mannschaft == mannschaft]) == 11
        for spieler in self.spieler:
            assert 0 <= spieler.x < self.feld[0]
            assert 0 <= spieler.y < self.feld[1]
        assert 0 <= self.ball.x < self.feld[0]
        assert 0 <= self.ball.y < self.feld[1]

    def aufstellung(self):
        print("Aufstellung:")
        for mannschaft in self.begegnung:
            print(f"== {mannschaft} ==")
            for spieler in self.spieler:
                if spieler.mannschaft == mannschaft:
                    print(f" {spieler.name:12} @ {spieler.x}, {spieler.y}")
        print(f"Ball @ {self.ball.x}, {self.ball.y}")

    def generiere_name(self, mannschaft):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        maxlen = 5
        if mannschaft == "Finnland":
            vowels += "öööäää"
            maxlen += 2
        elif mannschaft == "Belgien":
            vowels += "ééé"
        n = ""
        for i in range(random.randrange(2, maxlen)):
            n += random.choice(consonants)
            n += random.choice(vowels)
        n = n[0].upper() + n[1:]
        self.names[n] = True
        return n

    def run_internal(self):
        for i in itertools.count():
            print(f"------- {i}")
            self.round()
            time.sleep(0.5)

    def run(self):
        try:
            self.run_internal()
        except Exception as e:
            print("== Game over! ==", e)
            print("Ballbesitz:")
            for k in self.stats:
                pct = round(100 * self.stats[k] / sum(self.stats.values()), 1)
                print(f"- {k}: {pct}%")

    def round(self):
        # Ball bewegt sich
        self.ball.x += self.ball.shoot_x
        self.ball.y += self.ball.shoot_y
        print(f"Ball @ {self.ball.x}, {self.ball.y}")
        self.stats[self.ball.mannschaft] = self.stats.get(self.ball.mannschaft, 0) + 1
        # Spielunterbrechungen
        if self.ball.x < 0:
            print("Einwurf!")
            self.ball.x = 0
            self.ball.shoot_x = 0
        elif self.ball.x >= self.feld[0]:
            print("Einwurf!")
            self.ball.x = self.feld[0] - 1
            self.ball.shoot_x = 0
        if self.ball.y < 0:
            print("Einwurf!")
            self.ball.y = 0
            self.ball.shoot_y = 0
        elif self.ball.y >= self.feld[1]:
            print("Einwurf!")
            self.ball.y = self.feld[1] - 1
            self.ball.shoot_y = 0
        # Alle Spieler rennen zum Ball oder zufällig
        for spieler in self.spieler:
            if random.randrange(2) == 0:
                delta_x = self.speed(self.ball.x - spieler.x, 3)
                delta_y = self.speed(self.ball.y - spieler.y, 3)
            else:
                delta_x = random.randrange(7) - 3
                delta_y = random.randrange(7) - 3
            spieler.x += delta_x
            spieler.y += delta_y
            # Spieler trifft den Ball
            if spieler.x == self.ball.x and spieler.y == self.ball.y:
                if self.ball.mannschaft is not None and self.ball.mannschaft != spieler.mannschaft:
                    print(f"Ballverlust für {self.ball.mannschaft}!")
                self.ball.mannschaft = spieler.mannschaft
                # ... und gibt an irgendeinen Mitspieler ab
                rspieler = self.spieler[:]
                random.shuffle(rspieler)
                for spieler2 in rspieler:
                    if spieler2.name != spieler.name and spieler2.mannschaft == spieler.mannschaft:
                        print(f"Kick {spieler.name} zu {spieler2.name} @ {spieler2.x}, {spieler2.y}")
                        self.ball.shoot_x = self.speed(spieler2.x - self.ball.x, 6)
                        self.ball.shoot_y = self.speed(spieler2.y - self.ball.y, 6)
                        break

    def speed(self, distance, limit):
        if distance > 0 and distance > limit:
            distance = limit
        if distance < 0 and distance < limit:
            distance = -limit
        return distance

g = Game()
g.run()
