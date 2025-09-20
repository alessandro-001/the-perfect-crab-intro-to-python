# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295
from textwrap import shorten

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
	#filter out words that are 10 letters long
	long_words = extract_long_words(words)

	#filter out words containing a hyphen
	words_no_hyphens = reject_hyphen_words(long_words)

	#map the ones that are 15+ letter long
	shorten_if_longer = shorten_very_long_words(words_no_hyphens)

	#summarise to a string report
	return format_long_word(shorten_if_longer)

#-----------------------------------------------------------------------------#
def extract_long_words(words):
	long_words = [] #empty list
	for word in words: #scan through the words
		if len(word) > 10: #check length more than 10 chars
			long_words.append(word) #append that word if is longer
	return long_words #return the list

print ("Function - extract_long_words:")
print(extract_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

#-----------------------------------------------------------------------------#
def reject_hyphen_words(words):
	non_hyphenated_words = [] #empty list
	for word in words:
		if "-" not in word:
			non_hyphenated_words.append(word)
	return non_hyphenated_words

print ("Function - reject_hyphen_words:")
print(reject_hyphen_words(['hello',
    'non-biological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism']))

#-----------------------------------------------------------------------------#
def shorten_very_long_words(words):
	processed_words = []
	for word in words:
		if len(word) > 15:
			shortened_word = word[0:15] + "..."
			processed_words.append(shortened_word)
		else:
			processed_words.append(word)
	return processed_words

print ("Function - shorten_very_long_words:")
print(shorten_very_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

#-----------------------------------------------------------------------------#
def format_long_word(long_words):
	report = "These words are quite long: "
	if len(long_words) == 0:
		return report
	for word in long_words:
		report += word + ", "
	return report[0:-2]

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
