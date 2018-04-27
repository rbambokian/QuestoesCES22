read = open("intext.txt", "r")
write = open("outtext.txt", "w")
lines_list = []

while True:
    line = read.readline()
    lines_list.append(line)
    if len(line) == 0:
        break

for i in reversed(lines_list):
    write.write(i)

read.close()
write.close()
