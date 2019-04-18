# NETS 213 Final Project 
## Analysis

The goal of this project is to see if crowdsourced poetry can match with that written by famous poets, such as Shel Silverstein. The code and analysis to be used in this project are below.

### Code
We are using several scripts in this project.

```
aggregateKeywordsAndMood.py
```
This script reads in a .csv file containing Turker inputs on our Describing Poetry and aggregates results. The input file includes the fields 'title', 'poem', 'keyword1', 'keyword2', 'keyword3', and 'mood'. The script aggregates and finds the top 3 keywords by frequency by Turkers for each poem, and then writes results to our output file and includes an additional field of 'first_line'. Any keywords that are stopwords are filtered out.

```
qcPoemQuality.py
```
This script reads in a .csv file containing Turker inputs on our Writing Poetry HIT and does quality control to filter out bad poetry. The input file includes the fields 'title', 'is_english', 'embodies_keywords', and 'embodies_mood', where Turkers indicate if they think a poem is good quality. The script uses majority vote for each poem to determine if a poem is good quality or not, and discards a poem if it is not good quality. The output file is the same format as the input.

```
qcBestPoemVotes.py
```
This script reads in a .csv file containing Turker inputs on our Voting HIT and formats it into a cleaner .csv file. The input file includes the fields 'title', 'vote', and 'explanation', and we output a file with only 'title' and 'vote' fields. We perform quality control by filtering out Turkers who didn't provide an answer exceeding a length threshold for the 'explanation' field.

```
aggregateBestPoemVotes.py
```
This script reads in a .csv file that is the output from the qcBestPoemVotes.py script. It reads in the votes of each poem and accumulates the number of votes before sorting from highest to lowest. It then checks that poems have majority vote before outputting it as a winning opem. The script outputs a file with fields 'title' and 'winner'.


### Analysis
We plan on doing analysis at the end of posting our 4 stages of HITs (Describing Poetry, Writing Poetry, Writing Poetry QC, Evaluating Poetry), after we have consolidated the crowd's opinion on our crowdsourced poetry. Once we have aggregated the crowd's votes between original poems and the corresponding crowdsourced poems, we intend to compute what percentage of original vs crowdsourced poems were preferred. 

We also may do an extension and ask the crowd to rate original and crowdsourced poems on a 1-10 scale so that we can compute mean ratings, standard deviations, etc... and compare these metrics.