import sys
import csv

if len(sys.argv) < 3:
    print('Usage: python3 consolidateQC.py <HIT_QC_output.csv> <output.csv>')
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

poem_dict = {}

with open(output_file, 'w') as ofile:
    ofile = csv.writer(ofile, delimiter=',')
    ofile.writerow(['title', 'stanza', 'is_english', 'encompass_mood', 'encompass_keywords', 'rhymes', 'good_poem'])
    with open(input_file, 'r') as file:
        # skip the first line of headers
        file.readline()
        reader = csv.reader(file)

        for fields in reader:
            title = fields[0]
            line1 = fields[1]
            line2 = fields[6]
            line3 = fields[7]
            line4 = fields[8]
            is_english = fields[10] == "TRUE"
            has_mood = fields[14] == "TRUE"
            has_kw1 = fields[17] == "TRUE"
            has_kw2 = fields[18] == "TRUE"
            has_kw3 = fields[19] == "TRUE"
            rhymes = fields[16] == "TRUE"
            good_poem = fields[12] == "TRUE"

            poem = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            
            if poem not in poem_dict:
                poem_dict[poem] = {}
                poem_dict[poem]['title'] = title
                poem_dict[poem]['is_english'] = 0
                poem_dict[poem]['encompasses_mood'] = 0
                poem_dict[poem]['encompasses_keywords'] = 0
                poem_dict[poem]['rhymes'] = 0
                poem_dict[poem]['good_poem'] = 0

            poem_dict[poem]['is_english'] += 1 if is_english else 0
            poem_dict[poem]['encompasses_mood'] += 1 if has_mood else 0
            poem_dict[poem]['encompasses_keywords'] += 1 if (has_kw1 and has_kw2) or (has_kw1 and has_kw3) or (has_kw2 and has_kw3) else 0
            poem_dict[poem]['rhymes'] += 1 if rhymes else 0
            poem_dict[poem]['good_poem'] += 1 if good_poem else 0
        
        for stanza in poem_dict:
            ofile.writerow([poem_dict[stanza]['title'], stanza, poem_dict[stanza]['is_english'], poem_dict[stanza]['encompasses_mood'], poem_dict[stanza]['encompasses_keywords'], poem_dict[stanza]['rhymes'], poem_dict[stanza]['good_poem']])

            


            
            

            