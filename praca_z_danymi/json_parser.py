import json
import os

file_name = 'data.json'
file_new = False

if not os.path.isfile(file_name):
    file = open(file_name, 'w+')
    file.close()
    file_new = True

file = open(file_name, 'r+')

if file_new:
    data = {}
    data["movies"] = []
else:
    data = json.load(file)

run = True
while run:
    print("List of operations:\n"
          "1 - add movie\n"
          "2 - delete movie\n"
          "3 - print movies\n"
          "4 - save and exit\n")

    operation = int(input())

    if operation == 1:
        title = input("Give a title of the movie\n")
        year = input("Give a year of the movie production\n")
        movie = {"title": title, "year": year}
        data["movies"].append(movie)
    elif operation == 2:
        title_to_delete = input("Give a title of the movie\n")
        index = -1
        for i in range (len(data["movies"])):
            movie = data["movies"][i]
            if movie["title"] == title_to_delete:
                index = i
                break
        if index != -1:
            del data["movies"][index]
        else:
            print("Movie not found")
    elif operation == 3:
        print(json.dumps(data, sort_keys=True, indent=4))
    elif operation == 4:
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        file.close()
        run = False

