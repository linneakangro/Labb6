# Linnea Kangro HT21


def binary_search(the_list, key):  # Hämtat från Canvas med små modifikationer
    low = 0  # Index 0 för första körningen, aka från första elementet i listan
    high = len(the_list)-1  # High är antal element i listan -1 (pga mängden element = index för elementen + 1)

    while low <= high:  # Så länge det minsta indexet är mindre än det högsta indexet
        middle = (low + high)//2  # Räknar ut mittpunkten mellan högsta och lägsta index med heltalsdivision
        if the_list[middle] == key:  # Kollar om mitten är det vi letar efter (stämmer överens med nyckeln)
            return the_list[middle]  # Returnerar elementet på det indexet som stämmer överens med nyckeln
        else:
            if key < the_list[middle]:  # Om nyckeln är mindre än objektet på indexet
                high = middle - 1  # Ändras high-indexet till det till vänster (mindre) om det vi redan jämfört med key
            else:
                low = middle + 1  # Om key är större än objektet, ändras low till höger om det testade elementet
    return None  # Om hela listan har gåtts igenom och inget har hittats körs detta


def main():  # Hämtat från Canvas
    # Läs in listan
    indata = input().strip()  # Läser in input, tar bort mellanslag i slutet av textsträngen
    the_list = indata.split()  # Splittar inputen vid mellanslag och lägger det i en lista
    # Läs in nycklar att söka efter
    key = input().strip()  # Läser in nyckeln som vi söker efter, tar bort mellanslag i slutet av strängen
    while key != "#":  # Så länge input av nyckeln är skilt från "#"
        print(binary_search(the_list, key))  # Anropar och skriver ut vad den binära sökfunktionen returnerar
        key = input().strip()  # Frågar efter en ny nyckel


main()
