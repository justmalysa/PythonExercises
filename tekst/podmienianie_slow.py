fin = open("tekst.txt")
fout = open("output2.txt", "w+")

for line in fin:
    line = line.replace(' i ', ' i_2 ')
    line = line.replace('oraz', 'i')
    line = line.replace(' i_2 ', ' oraz ')
    line = line.replace('nigdy', 'prawie nigdy')
    line = line.replace('dlaczego', 'czemu')
    fout.write(line)
fin.close()
fout.close()
