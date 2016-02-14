# Main Class
# Rahul Shrestha
# CMPS 470-Spring 2016
# Dr. John W. Burris

# This program implements the DECISION_TREE_LEARNING algorithm.

# Input Description:
#       First	line:	(N)	Number of	examples
#       Second	line:	(X)	Number	of	attributes	(Not	including	goal	predicate)
#       Third	line:	The	name	of	each	of	the	X	attributes on	a	single	line,	separated	by	comma.
#       Following	N	lines	contain	X+1	values	containing	the	data	set,	separated	by	comma.

import os


# generator function to map key-value pair
# and holds values respective to attributes
# i.e. attributes with respective example values in a dictionary
def get_examples(examples, attributes):
    for value in examples:
        yield dict(zip(attributes, value.strip().replace(" ", "").split(',')))


# get the list of Goal Predicate from the examples
# extracted from the input file
def get_all_predicates(examples):
    return [d['Predicate'] for d in examples]


# using entropy to calculate the homogeneity of a sample.
# If the sample is completely homogeneous the entropy is zero and
# if the sample is an equally divided it has entropy of one.
# it is based on the overall distribution of predicate
def get_entropy_of_attributes(examples, predicate_list):
    get_all_predicates(examples).count(predicate_list[0])
    return 0

# get the file name from the user
file_name = input("Enter the input file name: ")

# look for file in the directory
try:
    fo = open(file_name, "r")
except IOError:
    print("Error: can\'t find file or read data.")
else:
    print("File found.")

    # check if the file is empty
    if os.stat(file_name).st_size <= 0:
        print("Not enough data in the input file.")
    else:
        # read and stores the number of examples, attributes.
        # as well as the name of attributes, and all examples
        with open(file_name, 'r') as file:

            number_of_examples = int(file.readline())
            number_of_attributes = int(file.readline())

            # replace the spaces and use , as delimiter
            name_of_attributes = [n for n in (file.readline().strip().replace(" ", "")).split(",")]
            name_of_attributes.append("Predicate")

            # store all the unfiltered examples as list
            all_examples = file.readlines()

        # holds all the examples as a list of dictionary
        # for instance: dic=[{'name_attributes': respective_example_value_from_the_file},...{}]
        examples = list(get_examples(all_examples, name_of_attributes))

        # get the values of Predicate from the examples
        # set - unordered collection of unique elements
        predicate_list = list(set(get_all_predicates(examples)))

        # invoke get_entropy_of_attributes function
        get_entropy_of_attributes(examples, predicate_list)



