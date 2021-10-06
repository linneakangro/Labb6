# Linnea Kangro HT21

import timeit


class Song:
    def __init__(self, trackid, songid, artistnamn, title):
        self.trackid = trackid
        self.songid = songid
        self.artistnamn = artistnamn
        self.title = title

    def __str__(self):
        return self.artistnamn + " med låten " + self.title

    def __lt__(self, other):
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


def lin_search(songlist, key):
    for song in songlist:
        if song.artistnamn == key or song.title == key:
            # print(song)
            return song
        else:
            pass
    # print("lin failed")
    return None


def bin_search(songlist, key):
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

    # print("Bin failed!")
    return None  # Om hela listan har gåtts igenom och inget har hittats körs detta


def hash_search(songdic, key):
    try:
        # print(key, "med låten", songdic[key])
        return songdic[key]
    except KeyError:
        # print(key, "hittades inte")
        return None


def main():
    songlist = read_file()
    song_dic = {}

    for song in songlist:
        song_dic[song.artistnamn] = song.title

    n = len(songlist)
    print("Antal element =", n, "\n")

    sista = songlist[n-1]
    key = sista.artistnamn

    lintime = timeit.timeit(stmt=lambda: lin_search(songlist, key), number=10000)
    print("Linjärsökningen tog", round(lintime, 4), "sekunder\n")

    print("Påbörjar sorteringen av listan...")
    songlist.sort()
    print("Sorteringen klar!\n")

    bintime = timeit.timeit(stmt=lambda: bin_search(songlist, key), number=10000)
    print("Binärsökningen tog", round(bintime, 4), "sekunder\n")

    hashtime = timeit.timeit(stmt=lambda: hash_search(song_dic, key), number=10000)
    print("Sökning i hashtabell tog", round(hashtime, 4), "sekunder\n")


main()
