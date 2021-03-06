import csv
import random

input_file = "raw_poem_votes.csv"
output_file = "poem_votes.csv"
letters='qwertyuiopasdfghjklzxcvbnm'
num_poems = 10
votes_per_poem = 11
length_threshold = 20
random.seed(213)

### sample votes for best poem
with open(input_file, 'w') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(['title', 'vote', 'explanation'])
	for i in range(num_poems):
		for j in range(votes_per_poem):
			comment = ''
			comment_length = random.randrange(40)
			for k in range(comment_length):
				comment += letters[random.randrange(26)]
			writer.writerow(['poem%d' % i, random.randrange(2), comment])

with open(input_file, 'r') as file:
	with open(output_file, 'w') as qc:
		reader = csv.reader(file, delimiter=',')
		writer = csv.writer(qc, delimiter=',')

		next(reader)
		writer.writerow(['title', 'vote'])
		votes = {}
		for line in reader:
			if len(line[2]) > length_threshold:
				writer.writerow([line[0], line[1]])