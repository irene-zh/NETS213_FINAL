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
	writer.writerow(['title', 'vote'])
	for i in range(num_poems):
		for j in range(votes_per_poem):
			writer.writerow(['poem%d' % i, random.randrange(2)])

with open(le_file, 'r') as file:
	with open(la_file, 'w') as aggregate:
		reader = csv.reader(file, delimiter=',')
		writer = csv.writer(aggregate, delimiter=',')

		next(reader)
		writer.writerow(['title', 'winner'])
		votes = {}
		for line in reader:
			poem_id = line[0]
			vote = int(line[1])
			if poem_id in votes:
				votes[poem_id] += vote 
			else:
				votes[poem_id] = vote
		for poem in sorted(votes):
			winner = 1 if votes[poem] > votes_per_poem / 2 else 0
			writer.writerow([poem, winner])