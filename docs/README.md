# NETS 213 Final Project 
### Overview

Here's a condensed list of what we'll be doing
* (2) **Data collection**. We need to acquire a good set of poems to let people work with. In order to accomplish this, we'll probably harvest some short poems from the internet. For example, we might pull some Shel Silverstein poems; hopefully it's legal for us to do that for our project.
* (2) **Poem keywording**. We get workers to label a poem with keywords and an overall mood. We'll give the workers three textboxes, and they should put one word into each of these boxes. (This hopefully will save us the work of having to parse the separators between words). We'll also have a dropdown menu of poem moods for workers to choose from, again for the sake of making the poem mood easy to select.
* (2) **Keyword aggregation**. People will give us a lot of keywords for poems, but we need to compile them together to give an organized list to our writers. We'll write some type of script to filter through the keywords people gave us and pick the most commonly given keywords.
* (4) **Three poetry-writing phases**. We get workers to write poems. They'll get four separate textboxes, one for each line, again to try to reduce the formatting issues. If a worker is writing the second or third stanzas, they'll also see the previously written stanzas.
* (3) **Quality control phases**. After each poem-writing phase, get workers to verify that the poems are well written. This is to filter out any spammy submitted HITs. We'll ask workers if the written poems fit the given keywords, and if the poems make sense.
* (2) **Final election**. Get workers to vote on the best poems. This should be easy, although to make sure that workers aren't simply clicking through the HITs as rapidly as possible, we'll force the workers to give us a reason for why they liked or didn't like a poem.



### Data Format:

All the data is located in the [data](../data) directory. The data we start with is a collection of 46 short poems written by Shel Silverstein. They are in [poems.txt](../data/poems.txt) if you are interested. The other data we will gather in this project will be `.csv`s that will serve as inputs and outputs to our various HITs. All the data related to each step of the process is detailed below.

#### Step 1: Gather the poems. 
The poems have been gathered. Find them [here](../data/poems.txt)! We attribute them to this lovely [website](http://thewhynot100.blogspot.com/2014/05/46-short-and-sweet-shel-silverstein.html). 

#### Step 2: Describe the poems.
We will post HITs (#1 in HIT designs) that will ask the crowd to come up with 3 keywords and a mood for each poem. The results of the HIT will be inputted into our aggregation module. A sample file that could represent these results is [here](../data/sample/describe_poem_HIT_results.csv). It will have the following columns 
```	
title: String
poem: String
keyword1: String
keyword2: String
keyword3: String
mood: String
```
Our aggregation module for this step will take the top three most frequent keywords and top mood for each poem and output that into a file that would look like [this](../data/sample/describe_poem_agg_output.csv), with the following columns:
```	
title: String
first_line: String
keyword1: String
keyword2: String
keyword3: String
mood: String
```

#### Step 3: Write the poems.
The crowd will write the poems iteratively (one stanza at a time), and for each iteration, we will have HITs (#3 in HIT designs) to filter out trashy poems as a way to control quality. A sample input file to this HIT is [here](../data/sample/writing_poetry_qc_input_sample.csv). Each HIT will decide whether a crowdsourced poem is English (not random words), embodies the 3 keywords, and embodies the mood. The result file would have many columns and look like [this](../data/sample/writing_poetry_qc_output_sample.csv), but we only really care about a few columns. We still have to put in work to condense this file, but a condensed sample result file would look like [this](../data/sample/write_poem_qc_HIT_results.csv). It has the columns:
```
title: String
is_english: Boolean
embodies_keywords: Boolean
embodies_mood: Boolean
```
The quality control HIT results will be fed into our own quality control module that will just take the majority vote on all categories. It will output a `csv` with the same columns as the input. An example output file is [here](../data/sample/write_poem_qc_results.csv). 

#### Step 4: Evaluate the poems.
When the poems are completed, we compare them to the original Shel Silverstein through another HIT (#4 in HIT designs) by asking the crowd to vote. Each original poem will be matched with a crowdsourced poem, so the input to this HIT would look like [this](../data/sample/evaluating_poetry_agg_input_sample.csv). Sample results of this HIT can be found [here](../data/sample/raw_poem_votes.csv). It has the columns:
```
title: String
vote: Integer
explanation: String
```
where the integer vote would represent which poem they chose. We can enforce that 0 is always original and 1 is always crowdsourced, and just randomize how they'd appear on the HIT.
After quality control, the results would be a csv that looks like [this](../data/sample/poem_votes.csv). 
```
title: String
vote: Integer
````

### Source Code

We have a few quality control and aggregation modules as python files in our [src folder](../src). So what are they?

[src/aggregateKeywordsAndMood.py](../src/aggregateKeywordsAndMood.py) aggregates 3 keywords and 1 mood for each poem.

[src/qcPoemQuality.py](../src/qcPoemQuality.py) is quality control for the poem quality intermediately.

[src/qcBestPoemVotes.py](../src/qcBestPoemVotes.py) is quality control where we filter out all submissions with an invalid answer for "why"?

[src/aggregateBestPoemVotes.py](../src/aggregateBestPoemVotes.py) is our aggregation module for getting the best poems by taking a majority.



