fin = open("tekst.txt")
fout = open("output.txt", "w+")
delete_list = ['się', 'oraz', 'nigdy', 'dlaczego', ' i ']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
