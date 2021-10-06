n = len(songlist)
bytt = True
while bytt:
    bytt = False
    for i in range(n-1):
        if songlist[i] > songlist[i+1]:
            songlist[i], songlist[i+1] = songlist[i+1], songlist[i]
            bytt = True


n = len(songlist)
for i in range(n):
    minst = i
    for j in range(i+1, n):
        if songlist[j] < songlist[minst]:
            minst = j
    songlist[minst], songlist[i] = songlist[i], songlist[minst]