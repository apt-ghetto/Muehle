from abc import ABC, abstractmethod
import os


class SpielStrategie(ABC):

    @abstractmethod
    def getFreiePosition(self, positionen, linien):
        pass

    @abstractmethod
    def takeStein(self, linien, spieler):
        pass


class StrategieSimple(SpielStrategie):

    def getFreiePosition(self, positionen, linien):
        for punkt in positionen:
            if not punkt.isBesetzt():
                return punkt

    def takeStein(self, linien, spieler):
        raise NotImplementedError("StrategieSimple: Nicht implementiert")


class StrategieMittel(SpielStrategie):

    def getFreiePosition(self, positionen, linien):
        raise NotImplementedError("StrategieMittel: Nicht implementiert")

    def takeStein(self, linien, spieler):
        raise NotImplementedError("StrategieMittel: Nicht implementiert")


class Eckpunkt:

    def __init__(self, position):
        self.position = position
        self.besitzer = None

    def getNummer(self):
        return self.position if self.besitzer is None else self.besitzer.wert

    def setBesitzer(self, besitzer):
        self.besitzer = besitzer

    def isBesetzt(self):
        return self.besitzer is not None


class Spieler:

    def __init__(self, wert):
        self.wert = wert
        self.anzahlSteine = 9
        self.punktZahl = 0

    def decrementStein(self):
        self.anzahlSteine -= 1

    def addPunkt(self):
        self.punktZahl += 1

    def getWert(self):
        return self.wert

    def hasSteine(self):
        return self.anzahlSteine > 0


class Linie:

    def __init__(self, pos1, pos2, pos3):
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.muehle = False

    def isMuehle(self):
        return self.muehle

    def checkIsMuehle(self):
        if (self.pos1.getNummer() == self.pos2.getNummer() and
                self.pos1.getNummer() == self.pos3.getNummer()):
            self.muehle = True

        return self.muehle


class Muehlebrett:

    def __init__(self):
        self.positionen = []
        for index in range(0, 24):
            self.positionen.append(Eckpunkt(index))
        self.fuelleLinien()

    def checkMuehle(self, spieler):
        liste = [x for x in self.linien if not x.isMuehle()]
        for linie in liste:
            if (linie.checkIsMuehle()):
                spieler.addPunkt()

    def getFreiePosition(self):
        return self.strategie.getFreiePosition(self.positionen, self.linien)

    def fuelleLinien(self):
        self.linien = []
        self.linien.append(Linie(self.positionen[0],
                                 self.positionen[1],
                                 self.positionen[2]))
        self.linien.append(Linie(self.positionen[3],
                                 self.positionen[4],
                                 self.positionen[5]))
        self.linien.append(Linie(self.positionen[6],
                                 self.positionen[7],
                                 self.positionen[8]))
        self.linien.append(Linie(self.positionen[9],
                                 self.positionen[10],
                                 self.positionen[11]))
        self.linien.append(Linie(self.positionen[12],
                                 self.positionen[13],
                                 self.positionen[14]))
        self.linien.append(Linie(self.positionen[15],
                                 self.positionen[16],
                                 self.positionen[17]))
        self.linien.append(Linie(self.positionen[18],
                                 self.positionen[19],
                                 self.positionen[20]))
        self.linien.append(Linie(self.positionen[21],
                                 self.positionen[22],
                                 self.positionen[23]))
        self.linien.append(Linie(self.positionen[0],
                                 self.positionen[9],
                                 self.positionen[21]))
        self.linien.append(Linie(self.positionen[3],
                                 self.positionen[10],
                                 self.positionen[18]))
        self.linien.append(Linie(self.positionen[6],
                                 self.positionen[11],
                                 self.positionen[15]))
        self.linien.append(Linie(self.positionen[1],
                                 self.positionen[4],
                                 self.positionen[7]))
        self.linien.append(Linie(self.positionen[16],
                                 self.positionen[19],
                                 self.positionen[22]))
        self.linien.append(Linie(self.positionen[8],
                                 self.positionen[12],
                                 self.positionen[17]))
        self.linien.append(Linie(self.positionen[5],
                                 self.positionen[13],
                                 self.positionen[20]))
        self.linien.append(Linie(self.positionen[2],
                                 self.positionen[14],
                                 self.positionen[23]))


muehle = Muehlebrett()
gegner = Spieler(77)
spieler = Spieler(88)


def druckeEndstand():
    print()
    print()
    print("Spiel ist beendet")
    print()
    print("Deine Punkte : {}".format(spieler.punktZahl))
    print("Punkte Gegner: {}".format(gegner.punktZahl))
    print()
    if (spieler.punktZahl > gegner.punktZahl):
        print("Du bist der Gewinner!")
    elif (spieler.punktZahl < gegner.punktZahl):
        print("Du hast leider verloren!")
    else:
        print("Unentschieden!")


def druckeInfos():
    print("Deine Steine: {}".format(spieler.wert))
    print("Gegn. Steine: {}".format(gegner.wert))


def druckeSpielfeld(positionen):
    print("{:2d}________{:2d}________{:2d}".format(
        positionen[0].getNummer(),
        positionen[1].getNummer(),
        positionen[2].getNummer()))
    print("|         |          |")
    print("|  {:2d}_____{:2d}_____{:2d}  |".format(
        positionen[3].getNummer(),
        positionen[4].getNummer(),
        positionen[5].getNummer()))
    print("|  |      |       |  |")
    print("|  |  {:2d}__{:2d}__{:2d}  |  |".format(
        positionen[6].getNummer(),
        positionen[7].getNummer(),
        positionen[8].getNummer()))
    print("|  |  |        |  |  |")
    print("{:2d}_{:d}_{:d}      {:d}_{:d}_{:d}".format(
        positionen[9].getNummer(),
        positionen[10].getNummer(),
        positionen[11].getNummer(),
        positionen[12].getNummer(),
        positionen[13].getNummer(),
        positionen[14].getNummer()))
    print("|  |  |        |  |  |")
    print("|  |  {}__{}__{}  |  |".format(
        positionen[15].getNummer(),
        positionen[16].getNummer(),
        positionen[17].getNummer()))
    print("|  |      |       |  |")
    print("|  {}_____{}_____{}  |".format(
        positionen[18].getNummer(),
        positionen[19].getNummer(),
        positionen[20].getNummer()))
    print("|         |          |")
    print("{}________{}________{}".format(
        positionen[21].getNummer(),
        positionen[22].getNummer(),
        positionen[23].getNummer()))
    druckeInfos()


def setzeStrategie():
    while True:
        print("Mögliche Strategien:")
        print("1) Simpel")
        print("2) Mittel")
        print()
        try:
            eingabe = int(input("Deine Wahl: "))
        except ValueError:
            print("Das war keine Zahl")
            continue

        if (1 == eingabe):
            muehle.strategie = StrategieSimple()
            break
        elif (2 == eingabe):
            muehle.strategie = StrategieMittel()
            break
        else:
            print("Ungültige Eingabe")


print("Herzlich willkommen zum Mühlespiel")
print()
print()
setzeStrategie()

while(spieler.hasSteine()):
    os.system('clear')
    druckeSpielfeld(muehle.positionen)
    eingabe = 99
    while eingabe > 23:
        try:
            eingabe = int(input("Welche Position: "))
        except ValueError:
            print("Ungültige Eingabe")

        if (eingabe < 24 and muehle.positionen[eingabe].isBesetzt()):
            print("Eckpunkt bereits besetzt!")
            eingabe = 99
    muehle.positionen[eingabe].setBesitzer(spieler)
    muehle.checkMuehle(spieler)
    spieler.decrementStein()
    gegnerPosition = muehle.getFreiePosition()
    muehle.positionen[gegnerPosition.position].setBesitzer(gegner)
    muehle.checkMuehle(gegner)
    gegner.decrementStein()

os.system('clear')
druckeSpielfeld(muehle.positionen)
druckeEndstand()
