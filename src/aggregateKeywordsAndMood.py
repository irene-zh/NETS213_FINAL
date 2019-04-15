'''
Usage: python3 aggregateKeywordsAndMood.py <describe_poem_HIT_results.csv> <output.csv>
Given a csv output from the Describe the Poem HIT, aggregate and output three keywords and one mood for each poem in an output csv.
The input will have the following columns (and a lot more):
   title
   poem
   keyword1
   keyword2
   keyword3
   mood
The output will only have the following columns:
   title
   first line
   keyword1
   keyword2
   keyword3
   mood
'''

import sys
import csv
import operator

if len(sys.argv) < 3:
    print('Usage: python3 aggregateKeywordsAndMood.py <poem_analysis_results.csv> <output.csv>')
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
poems_dict = {}

with open(input_file, 'r') as file:
    # skip the first line of headers
    file.readline()
    reader = csv.reader(file)

    stopwords = ['a', 'the', 'of', 'he', 'she', 'me']

    for fields in reader:
        title = fields[27]
        poem = fields[28]
        keyword1 = fields[29].lower()
        keyword2 = fields[30].lower()
        keyword3 = fields[31].lower()
        mood = fields[32]

        if title not in poems_dict:
            poems_dict[title] = {}
            poems_dict[title]['keywords'] = {}
            poems_dict[title]['mood'] = {}
            poems_dict[title]['first line'] = poem[:poem.index('<br>')]
        
        if keyword1.find(' ') == -1 and keyword1 not in stopwords:
            if keyword1 not in poems_dict[title]['keywords']:
                poems_dict[title]['keywords'][keyword1] = 0
            poems_dict[title]['keywords'][keyword1] += 1

        if keyword2.find(' ') == -1 and keyword2 not in stopwords:
            if keyword2 not in poems_dict[title]['keywords']:
                poems_dict[title]['keywords'][keyword2] = 0
            poems_dict[title]['keywords'][keyword2] += 1

        if keyword3.find(' ') == -1 and keyword3 not in stopwords:
            if keyword3 not in poems_dict[title]['keywords']:
                poems_dict[title]['keywords'][keyword3] = 0
            poems_dict[title]['keywords'][keyword3] += 1

        if mood not in poems_dict[title]['mood']:
            poems_dict[title]['mood'][mood] = 0

        poems_dict[title]['mood'][mood] += 1

with open(output_file, 'w') as file:
    file = csv.writer(file, delimiter=',')
    file.writerow(['title', 'first_line', 'keyword1', 'keyword2', 'keyword3', 'mood'])
    for poem_title in poems_dict:
        keywords = sorted(poems_dict[poem_title]['keywords'].items(), key=operator.itemgetter(1), reverse=True)
        mood = sorted(poems_dict[poem_title]['mood'].items(), key=operator.itemgetter(1), reverse=True)

        kw1, count1 = keywords[0]
        kw2, count2 = keywords[1]
        kw3, count3 = keywords[2]
        mood, count = mood[0]
        first_line = poems_dict[poem_title]['first line']

        file.writerow([poem_title, first_line, kw1, kw2, kw3, mood])