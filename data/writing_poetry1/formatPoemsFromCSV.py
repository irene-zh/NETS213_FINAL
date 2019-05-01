import sys
import csv

if len(sys.argv) < 3:
    print('Usage: python3 formatPoemsFromCSV.py <HIT_output.csv> <output.txt>')
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, 'w') as ofile:
    with open(input_file, 'r') as file:
        # skip the first line of headers
        file.readline()
        reader = csv.reader(file)

        for fields in reader:
            title = fields[27]
            line1 = fields[28]
            line2 = fields[33]
            line3 = fields[34]
            line4 = fields[35]

            ofile.write(title + '\n')
            ofile.write(line1 + '\n')
            ofile.write(line2 + '\n')
            ofile.write(line3 + '\n')
            ofile.write(line4 + '\n\n')