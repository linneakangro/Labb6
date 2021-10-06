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


def quicksort(data):  # Hämtat från Canvas (även de tillhörande funktionerna)
    sista = len(data) - 1
    qsort(data, 0, sista)


def qsort(data, low, high):  # Hämtat från Canvas
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)


def partitionera(data, v, h, pivot):  # Hämtat från Canvas
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


def slowsort(songlist):
    n = len(songlist)
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

    songlist = songlist1[:100000]
    n = len(songlist1)

    print("Antal element =", n, "\n")

    times_run = 2

    print("Påbörjar den snabba sorteringen av listan...")
    fastsorttime = timeit.timeit(stmt=lambda: quicksort(songlist1), number=times_run)
    print("Fastsort tog i snitt", round((fastsorttime/times_run), 4)/times_run, "sekunder\n")

    print("Påbörjar den långsamma sorteringen av listan...")
    slowsorttime = timeit.timeit(stmt=lambda: slowsort(songlist2), number=times_run)
    print("Slowsort tog i snitt", round((slowsorttime/times_run), 4), "sekunder\n")


main()
