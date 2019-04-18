import csv

input_file = "HIT_QC_input.csv"
output_file = "HIT_QC_input2.csv"

with open(input_file, 'r') as file:
	with open(output_file, 'w') as qc:
		reader = csv.reader(file, delimiter=',')
		writer = csv.writer(qc, delimiter=',')

		next(reader)
		writer.writerow(['title', 'first_line', 'keyword1', 'keyword2', 'keyword3', 'mood', 'crowdsourced_poem'])
		for line in reader:
			crowdsourced_poem = line[6] + '<br>' + line[7] + '<br>' + line[8]
			writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], crowdsourced_poem])