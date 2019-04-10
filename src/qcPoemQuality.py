import csv
import random

input_file = "raw_poem_quality_data.csv"
output_file = "qc_poem_quality_data.csv"
num_poems = 10
votes_per_poem = 11
random.seed(213)

### sample results from QC HIT
with open(le_file, 'w') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(['title', 'is_english', 'embodies_keywords'])
	for i in range(num_poems):
		for j in range(votes_per_poem):
			writer.writerow(['poem%d' % i, random.randrange(2), random.randrange(2)])

with open(le_file, 'r') as file:
	with open(la_file, 'w') as qc:
		reader = csv.reader(file, delimiter=',')
		writer = csv.writer(qc, delimiter=',')

		next(reader)
		writer.writerow(['title', 'is_english', 'embodies_keywords'])
		votes = {}
		for line in reader:
			title = line[0]
			is_english = int(line[1])
			embodies_keywords = int(line[2])
			if title in votes:
				votes[title] = (is_english + votes[title][0], embodies_keywords + votes[title][1])
			else:
				votes[title] = (is_english, embodies_keywords)
		for title in votes:
			is_english = 1 if votes[title][0] > votes_per_poem / 2 else 0
			embodies_keywords = 1 if votes[title][1] > votes_per_poem / 2 else 0
			writer.writerow([title, is_english, embodies_keywords])
