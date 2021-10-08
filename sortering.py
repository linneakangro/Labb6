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


def quicksort(data):  # Hämtat från Canvas
    sista = len(data) - 1  # Plockar fram det högsta indexet
    qsort(data, 0, sista)  # Kallar på qsort med listan, lägsta index (default 0 första körningen), högsta index


def qsort(data, low, high):  # Hämtat från Canvas
    pivotindex = (low+high)//2  # Väljer ett pivot-index som ligger ungefärligt mitt mellan det högsta och lägsta index
    data[pivotindex], data[high] = data[high], data[pivotindex]  # Byter plats på elementet på högsta- och pivot-indexet

    pivotmid = partitionera(data, low-1, high, data[high])  # (Listan, lägsta index-1, högsta index, pivot-elementet)
    # Pivotmid blir det index-nummer som är brytpunkten mellan de högre- och lägre elementen jämfört med pivot-elementet
    # Det blir det index där det första element som är större än pivot ligger

    data[pivotmid], data[high] = data[high], data[pivotmid]  # Flyttar pivot till rätt plats i listan

    if pivotmid-low > 1:  # Om pivots index-lägsta index är större än 1 (pivot är inte näst längst till vänster)
        qsort(data, low, pivotmid-1)  # Kalla på funktionen qsort med (listan, lägsta index, nuvarande pivot-index-1)
        # en "nedkortad lista till vänster om nuvarandra pivot"

    if high-pivotmid > 1:  # Om högsta index-pivot-index är större än 1 (pivot är inte näst längst till höger)
        qsort(data, pivotmid+1, high)  # Kalla på funktionen qsort med (listan, pivot-index+1, högsta index)
        #  en "nedkortad lista till höger om nuvarande pivot"


def partitionera(data, v, h, pivot):  # Hämtat från Canvas
    while True:
        v = v + 1  # Plussar på v med 1 (flyttar index åt höger från vänster)
        while data[v] < pivot:  # Så länge den vänstra (lägsta) index-elementet är mindre än pivot-elementet
            v = v + 1  # Ta ett steg åt höger i listan

        h = h - 1  # Subtraherar 1 från h (flyttar index åt vänster från höger, pivot ligger längst till höger)
        while h != 0 and data[h] > pivot:  # Så länge högra (högsta) index-elementet är skilt från noll och är större än pivot
            h = h - 1  # Ta ett steg åt vänster i listan

        data[v], data[h] = data[h], data[v]  # När data[h] <= pivot/0 och pivot <= data[v] byter dessa plats

        if v >= h:  # Om v är större än eller lika med h (alltså att dessa har korsats eller är på samma plats
            break  # Bryt while-loopen

    data[v], data[h] = data[h], data[v]  # Byt tillbaka det senaste bytet då v>=h gör att senaste bytet var felaktigt
    return v  # Returnerar det index-nummer som v (den som vandrar från vänster till höger) har


def slowsort(songlist):  # Hämtat från Canvas
    n = len(songlist)  # Räknar ut längden av listan
    bytt = True
    while bytt:
        bytt = False
        for i in range(n-1):
            if songlist[i] > songlist[i+1]:
                songlist[i], songlist[i+1] = songlist[i+1], songlist[i]
                bytt = True


def main():
    songlist1 = read_file()
    songlist2 = read_file()
    # Gör två listor då man annars under andra sorteringen man gör skulle skicka in en redan sorterad lista

    slicing_number = 100000
    times_run = 1

    songlist1 = songlist1[:slicing_number]
    songlist2 = songlist2[:slicing_number]

    n = len(songlist1)

    print("Antal element =", n, "\n")

    #print("Påbörjar den snabba sorteringen av listan...")
    #fastsorttime = timeit.timeit(stmt=lambda: quicksort(songlist1), number=times_run)
    #print("Fastsort tog i snitt", round((fastsorttime/times_run), 4)/times_run, "sekunder\n")

    print("Påbörjar den långsamma sorteringen av listan...")
    slowsorttime = timeit.timeit(stmt=lambda: slowsort(songlist2), number=times_run)
    print("Slowsort tog i snitt", round((slowsorttime/times_run), 4), "sekunder\n")


main()

"""
Dessa tider avser en körning

Tider      n = 1 000       n = 10 000        n = 100 000       n = 1 000 000
Snabb:      0,0053s          0,074s            1,1502s              14,8892s
långsam:    0,5301s         54,0085s           
"""