import random

class KartaKredytowa:
    def __init__ (self):
        poczatek_numeru = "400000"
        srodek_numeru = str(random.randint(000000000,999999999)).zfill(9)
        pre_luhn = poczatek_numeru + srodek_numeru
        luhn = [int(x) for x in pre_luhn]
        luhn_sum = 0
        suma_kontrolna = ""

        for i in range(len(luhn)):
            if(i % 2 == 0):
                luhn[i] *= 2

        for i in range(len(luhn)):
            if(luhn[i] > 9):
                luhn[i] -= 9

        for i in range(len(luhn)):
            luhn_sum += luhn[i]

        reszta = luhn_sum % 10

        if(reszta != 0):
            suma_kontrolna = str(10 - reszta)
        else: 
            suma_kontrolna = "0"

        self.numer_karty = poczatek_numeru + srodek_numeru + suma_kontrolna
        self.pin = str(random.randint(0000,9999)).zfill(4)
        self.saldo = 0

    def informacje_karty(self):
        print("Your card number:")
        print(self.numer_karty)
        print("Your card PIN:")
        print(self.pin)

    def sprawdzenie_pinu(self, pin):
        return self.pin == pin

class SystemBankowy:

    STANY = ['ogolny', 'zalogowany', 'zamkniety']

    stan = STANY[0]
    tablica_kart = []
    karta = None

    def wiadomosc_ogolny(self):
        print("1. Create an account") #
        print("2. Log into account")    #
        print("0. Exit") #
    
    def wiadomosc_zalogowany(self):
        print("1. Balance")
        print("2. Log out")
        print("0. Exit") #

    def wyswietlanie_wiadomosci(self):
        if self.stan == self.STANY[0]:
            self.wiadomosc_ogolny()
        elif self.stan == self.STANY[1]:
            self.wiadomosc_zalogowany()

    def utworzenie_konta(self):
        karta = KartaKredytowa()
        self.karta = karta
        self.tablica_kart.append(karta)
        print("Your card has been created")
        karta.informacje_karty()

    def logowanie(self):
        print("Enter your card number:")
        log_numer = input()
        print("Enter your PIN:")
        log_pin = input()

        poprawne_logowanie = self.czy_poprawny_numer(log_numer, log_pin)

        if poprawne_logowanie:
            print("You have successfully logged in!")
            self.stan = self.STANY[1]
        else:
            print("Wrong card number or PIN!")

    def czy_poprawny_numer(self, podany_numer, podany_pin):
        for k in self.tablica_kart:
            if podany_numer == k.numer_karty:
                if podany_pin == k.pin:
                    return True
                else: 
                    return False
            else:
                return False

    def wyjscie(self):
        self.stan = self.STANY[2]
        print("Bye!")

    def uruchomiony_system(self):
        return self.stan != self.STANY[2]

    def wyswietl_saldo(self):
        print("Balance: " + str(self.karta.saldo))

    def wylogowanie(self):
        self.stan = self.STANY[0]

    def akcje(self, numer_akcji):
        if self.stan == self.STANY[0]:
            if numer_akcji == 1:
                self.utworzenie_konta()
            elif numer_akcji == 2:
                self.logowanie()
            elif numer_akcji == 0:
                self.wyjscie()
        elif self.stan == self.STANY[1]:
            if numer_akcji == 1:
                self.wyswietl_saldo()
            elif numer_akcji == 2:
                self.wylogowanie()
            elif numer_akcji == 0:
                self.wyjscie()

system = SystemBankowy()


while system.uruchomiony_system():
    system.wyswietlanie_wiadomosci()
    wybor = int(input())
    print()
    system.akcje(wybor)
    print()