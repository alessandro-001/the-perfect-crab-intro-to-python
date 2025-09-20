# Video alternative: https://vimeo.com/954334103/0aed500d39#t=0

# Congratulations! You've covered all of the key syntax, concepts, and ideas
# necessary to succeed in your assessment. You can take it now if you like,
# though you might be a little stronger if you do these extra challenges.

# Each challenge focuses on a new technique or approach. It starts with an
# example, and then leads into an exercise.

# We'll start with combining filtering, mapping, and summarising into one
# super-brilliant pipeline.

# I'll demonstrate for you a function that:
#
# * Gets rid of junk data
# * Converts negative integers to positive numbers
# * Creates a graph of how frequently each number shows up
#
# If you've not used the videos so far, you might want to do so for this one. It

# will show you how I build up the program piece by piece.

example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]


# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

def generate_frequency_graph(numbers):
	integers = get_only_integers(numbers)
	positive_integers = convert_negatives_to_positives(integers)
	number_frequency = calc_frequency_of_numbers(positive_integers)
	graph = format_graph(number_frequency)
	return graph


def get_only_integers(numbers):
	integers = [] #create empty list
	for number in numbers: #scan through numbers
		if number is not None: #check if number is not None
			integers.append(number) #if not, append to the dictionary
	return integers #return dictionary


def convert_negatives_to_positives(numbers):
	positives = [] #create empty list
	for number in numbers: #scan through numbers
		if number < 0: #if number is negative
			positive_number =  number * -1 #multiply by -1 to convert to positive
			positives.append(positive_number) #append to the dictionary
		else: #any other case, all positives
			positives.append(number) #append to the dictionary
	return positives #return dictionary


def calc_frequency_of_numbers(numbers):
	freq = {} #create empty dictionary
	for number in numbers: #scan through numbers
		if number in freq: #if number is not in the dictionary
			freq[number] = freq[number] + 1 #add one to that number
		else: #otherwise
			freq[number] = 1 #declare that number is unique (1)
	return freq #return frequency dictionary

def format_graph(freq_dict):
	graph = ""
	for number in freq_dict:
		bar = 'x' * freq_dict[number]
		line = f"{number}: {bar}"
		graph = graph + line + "\n"
	return graph

print ("Function - get_only_integers")
print (get_only_integers([0, None, -1, 1]))

print ("Function - convert_negatives_to_positives")
print (convert_negatives_to_positives([-1, 0, 1]))

print ("Function - calc_frequency_of_numbers")
print (calc_frequency_of_numbers([0, 1, 2, 3, 1, 2, 4]))

print ("Function - format_graph")
print (format_graph({0: 1, 1: 2, 2: 2, 3: 1, 4: 1}))

print ("Final graph: ")
print(generate_frequency_graph(example_numbers))
