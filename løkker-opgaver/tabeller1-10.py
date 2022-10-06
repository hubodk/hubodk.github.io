#Lav et program, der udskriver 2-tabellen, 3-tabellen, .. op til 10-tabellen.
for tabel in range(11):
    print(f"{tabel}-tabellen")
    for i in range(1,11):
        print(str(tabel) + " x " + str(i) + " = " + str(tabel*i))