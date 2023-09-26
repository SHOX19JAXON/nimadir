n = input("Butun son kiriting: ")
with open("file.txt", "w") as f:
    f.write(n)

with open("file.txt", "r") as f1:
    raqam = int(f1.readline())
    kun = raqam // 86400
    raqam -= kun*86400
    soat = raqam // 3600
    raqam -= soat*3600
    minut = raqam // 60
    raqam -= minut*60
    print(f"kun: {kun} soat: {soat} minut: {minut}, sekund: {raqam}")

