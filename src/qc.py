import csv
import random

le_file = "hallo.csv"
la_file = "goodbai.csv"
num_poems = 10
votes_per_poem = 11
random.seed(213)









### sample votes for best poem
with open(le_file, 'w') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow([''] + [('vote%d' % i) for i in range(votes_per_poem)])
	for i in range(num_poems):
		writer.writerow(['poem%d' % i] + [random.randrange(2) for i in range(votes_per_poem)])

with open(le_file, 'r') as file:
	with open(la_file, 'w') as qc_file:
		reader = csv.reader(file, delimiter=',')
		writer = csv.writer(qc_file, delimiter=',')

		next(reader)
		writer.writerow(['', 'approve?'])
		for line in reader:
			poem_id = line[0]
			votes_for = sum(map(int, line[1:]))
			if votes_for > votes_per_poem / 2:
				writer.writerow([poem_id, '1'])
			else:
				writer.writerow([poem_id, '0'])
