first = True

for line in open("student.txt"):
    if first:
        first = False
    else:
        data = line.strip(" ").split(",")
        id = data[0]
        name = data[1]
        age = data[2]
        score = int(data[3])
        if score < 80:
            print(id, name, age, score)