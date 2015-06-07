all_lines = open('distance.txt', "r").readlines()

output = '['
idx = 1
label = ''

for line in all_lines:
    output = output + '[' + line.rstrip('\n') + '],' + "\n"
    label = label + '\"' + str(idx) + '\",'
    idx = idx + 1

output = output + ']'

outfile = open('distance.out', "w")
outfile.write(output)

label = '\n' + label
outfile.write(label)

outfile.close()
