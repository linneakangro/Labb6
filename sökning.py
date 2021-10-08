# Linnea Kangro HT21

import timeit


class Song:  # En klass för alla sånger med deras olika attribut
    def __init__(self, trackid, songid, artistnamn, title):
        self.trackid = trackid
        self.songid = songid
        self.artistnamn = artistnamn
        self.title = title

    def __str__(self):  # Visar hur objekten ska skrivas ut
        return self.artistnamn + " med låten " + self.title

    def __lt__(self, other):  # Sorterar objekten med avseende på artistnamn (a -> ö)
        return self.artistnamn < other.artistnamn


def read_file():  # Läser in alla rader i filen, skapar objekt och lagrar dem i en lista som returneras.
    songlist = []
    with open("unique_tracks.txt", "r", encoding="utf8") as infile:  # Öppnar filen och stänger den sedan när det körts klart
        read = infile.readlines()  # Läser in alla rader i filen

        for line in read:
            line = line.strip("\n")
            line = line.split("<SEP>")  # splittar vid <SEP>
            song = Song(line[0], line[1], line[2], line[3])  # Skapar klassobjekt Song
            songlist.append(song)  # Lägger in i listan songlist

    return songlist


def lin_search(songlist, key):  # Linjär sökning i listan
    for song in songlist:  # Går igenom listan från första objektet till det sista
        if song.artistnamn == key or song.title == key:  # Om key stämmer överens
            # print(song)
            return song  # Returnerar objektet som stämmer överens med key
        else:
            pass  # Om objektet inte stämmer överens med key hoppar vi över objektet
    print("lin failed")
    return None  # Om inget av objekten stämde överens med key när hela listan har gåtts igenom


def bin_search(songlist, key):  # Hämtat från Canvas med mindre modifikationer
    low = 0  # Index 0 för första körningen, aka från första elementet i listan
    high = len(songlist)-1  # High är antal element i listan -1 (pga mängden element = index för elementen + 1)

    while low <= high:  # Så länge det minsta indexet är mindre än det högsta indexet
        middle = (low + high)//2  # Räknar ut mittpunkten mellan högsta och lägsta index med heltalsdivision
        if songlist[middle].artistnamn == key:  # Kollar om mitten är det vi letar efter (stämmer överens med nyckeln)
            # print(songlist[middle])
            return songlist[middle]  # Returnerar elementet på det indexet som stämmer överens med nyckeln
        else:
            if key < songlist[middle].artistnamn:  # Om nyckeln är mindre än objektet på indexet
                high = middle - 1  # Ändras high-indexet till det till vänster (mindre) om det vi redan jämfört med key
            else:
                low = middle + 1  # Om key är större än objektet, ändras low till höger om det testade elementet

    print("Bin failed!")
    return None  # Om hela listan har gåtts igenom och inget har hittats körs detta


def hash_search(songdic, key):  # Hämtat från Canvas med mindre modifikationer
    try:  # Kommer försöka köra koden
        # print(key, "med låten", songdic[key])
        return songdic[key]  # Om key hittas i dictionaryt kommer objektet att returneras
    except KeyError:  # Om koden i try-satsen inte gick att köra
        print(key, "hittades inte")
        return None  # Returneras None, alltså finns inte key i songdic


def main():
    songlist = read_file()  # Läser in filen och lägger den i en lista
    song_dic = {}  # Skapar en tom dictionary

    songlist = songlist[:1000000]  # Slicear listan

    for song in songlist:  # Lägger in objekten från listan i dictionaryn
        song_dic[song.artistnamn] = song.title  # Lägger in objektens artistnamn som key och titeln som värde

    n = len(songlist)  # Beräknar listans längd
    print("Antal element =", n, "\n")  # Skriver ut antal element som finns i listan

    sista = songlist[n-1]  # Väljer det sista elementet i listan
    key = sista.artistnamn  # Väljer en key som är sista elementets artistnamn
    print(key)

    lintime = timeit.timeit(stmt=lambda: lin_search(songlist, key), number=10000)  # Tar tiden för funktionen att köras
    print("Linjärsökningen tog", round(lintime, 4), "sekunder\n")

    print("Påbörjar sorteringen av listan...")  # Skriver bara ut vad som sker i körningen
    songlist.sort()  # Sorterar listan med avseende på artistnamn
    print("Sorteringen klar!\n")

    bintime = timeit.timeit(stmt=lambda: bin_search(songlist, key), number=10000)  # Tar tiden för funktionen att köras
    print("Binärsökningen tog", round(bintime, 4), "sekunder\n")

    hashtime = timeit.timeit(stmt=lambda: hash_search(song_dic, key), number=10000)  # Tar tiden för funktionen att köras
    print("Sökning i hashtabell tog", round(hashtime, 4), "sekunder\n")


main()

"""
Detta med sista elementets artist som nyckel och number = 10 000
                         n = 250 000         n = 500 000        n = 1 000 000
Linjär sökning            100,3216s            5,5544s          0,9102s
Binär sökning               0,0709s            0,0661s          0,0603s
Sökning i hashtabell        0,0024s            0,0023s          0,0022s

Tidskomplexitet (i teorin):
Linjär söknig   O(n)
Binär sökning   O(log(n))
Hashtabell      O(1)

Jag skulle inte påstå att mina resultat helt sstämmer överens med teorin gällande den linjära eller den binära
sökningen. Den binära sökniingen stämmer mer överens med den teoretiska tidskomplexiteten dock och kan ha påverkats
av hur elementen låg i listan och datorns kapacitet att köra programmet, det sist nämnde påverkar även de andra
sökfunktionerna.
Den linjära sökningen har tydligt påverkats av hur elementen låg i listan då det vid 250 000 element tog längre tid
att söka i listan än vid 1 000 000 element. Rimligtvis skulle sökningen i den längsta listan ta längst tid med
linjärsökningen. Dock förekommer artister (vilket i denna kod är söknyckeln) flera gånger fast med olika låtar så vid
den kortare listan kan en artist som först förekommer långt bak i listan vara vår söknyckel medan en artist som blir vår
söknyckel vid de längre listorna förekommer tidigare i listan och dörför hitta ssnabbare.
Sökningen i hashtabellen stämmer relativt bra överens med teorin då den tar ungefär lika lång tid vid varje sökning,
detta då man endast gör en jämförelse mellan två nycklar.

Den linjära söknignen kommer att ta längst tid då man i värsta fall kommer att gå igenom alla värden i listan i tur och
ordning för att leta efter ett element som matchar nyckel. Alltså kommer det att i värsta fall behöva genomföras N antal
jämförelser. Detta ger O(n) vid stora tal n.

Den binära sökningen kommer att ta näst längst tid då den för varje jämförelse den gör i en sorterad lista kommer att
halvera antalet element i listan som eventuellt kommer behöva jämföras med nyckeln. Detta gör att tidskomplexiteten för
binärsökningen kommer att bli O(log(n)) (i bas 2) för stora tal n.

Sökningen i hashtabell kommer att vara den snabbaste söknings-funktionen då man endast gör en jämförelse mellan sin
nyckel och om det finns en nyckel som stämmer överens med den i hashtabellen. Detta gör att tidskomplexiteten blir O(1).
"""