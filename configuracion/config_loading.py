porcentajes = []
scale = 1

f = open("configuracion/config.txt")
for line in f.readlines():
    if "#" not in line:
        if "@" in line:
            ecuation = line.split(" = ")
            for n in range(round(int(ecuation[1])/10)):
                porcentajes.append(ecuation[0][1:len(ecuation[0])])
        if "Multiplicador de escala" in line:
            scale = float(line.split(" = ")[1])
f.close()

