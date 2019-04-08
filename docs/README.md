# NETS 213 Final Project
### Spring 2019

Here's a list of what we'll be doing.
* (2) Data collection. We need to acquire a good set of poems to let people work with. In order to accomplish this, we'll probably harvest some short poems from the internet. For example, we might pull some Shel Silverstein poems; hopefully it's legal for us to do that for our project.
* (2) Poem keywording. We get workers to label a poem with keywords and an overall mood. We'll give the workers three textboxes, and they should put one word into each of these boxes. (This hopefully will save us the work of having to parse the separators between words). We'll also have a dropdown menu of poem moods for workers to choose from, again for the sake of making the poem mood easy to select.
* (2) Keyword aggregation. People will give us a lot of keywords for poems, but we need to compile them together to give an organized list to our writers. We'll write some type of script to filter through the keywords people gave us and pick the most commonly given keywords.
* (4) Three poetry-writing phases. We get workers to write poems. They'll get four separate textboxes, one for each line, again to try to reduce the formatting issues. If a worker is writing the second or third stanzas, they'll also see the previously written stanzas.
* (3) Quality control phases. After each poem-writing phase, get workers to verify that the poems are well written. This is to filter out any spammy submitted HITs. We'll ask workers if the written poems fit the given keywords, and if the poems make sense.
* (2) Final election. Get workers to vote on the best poems. This should be easy, although to make sure that workers aren't simply clicking through the HITs as rapidly as possible, we'll force the workers to give us a reason for why they liked or didn't like a poem.

===============

Data Format:

Compiling Poetry
(Input to Aggregation Module)
{
	title: String
	poem: String
}

Describing Poetry
(Output from Aggregation Module)
{
	title: String
	first_line: String
	keyword1: String
	keyword2: String
	keyword3: String
	mood: String
}

Writing Poetry
(Input to Quality Control Module)
{
	title: String
	first_line: String
	keyword1: String
	keyword2: String
	keyword3: String
	mood: String
	crowdsourced_poem: String
}

Writing Poetry
(Output from Quality Control Module)
{
	title: String
	first_line: String
	keyword1: String
	keyword2: String
	keyword3: String
	mood: String
	crowdsourced_poem: String
	identified_mood: String
	is_english: Boolean
	embodies_original: Boolean
}

Evaluating Crowdsourced Poetry
(Input to Aggregation Module)
{
	title: String
	original_poem: String
	crowdsourced_poem: String
}

Evaluating Crowdsourced Poetry
(Input to Quality Control Module)
{
	title: String
	vote: String
	explanation: String
}

Evaluating Crowdsourced Poetry
(Output from Quality Control/Aggregation Module)
{
	title: String
	original_votes: Number
	crowdsourced_votes: Number
}