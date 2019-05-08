import sys
import csv

if len(sys.argv) < 3:
    print('Usage: python3 getCrowdPoems.py <HIT_output.csv> <crowd_poems.txt>')
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, 'w') as ofile:
    with open(input_file, 'r') as file:
        # skip the first line of headers
        file.readline()
        reader = csv.reader(file)

        for fields in reader:
            title = fields[28]
            rating1 = fields[40]
            rating2 = fields[41]
            line1 = fields[30]
            line2 = fields[31]
            line3 = fields[32]
            line4 = fields[33]
            line5 = fields[34]
            line6 = fields[35]
            line7 = fields[36]
            line8 = fields[37]
            
            poem = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7 + '\n' + line8
            
            if int(rating2) >= int(rating1):
                ofile.write(title + '\n')
                ofile.write('Rating: ' + rating2 + '\n\n')
                ofile.write(poem + '\n\n')
            


            
            

            