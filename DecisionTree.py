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
import math


# generator function to map key-value pair
# and holds values respective to attributes
# i.e. attributes with respective example values in a dictionary
def get_examples(examples, attributes):

    for value in examples:
        yield dict(zip(attributes, value.strip().replace(" ", "").split(',')))


# get the list of Goal Predicate from the examples
# extracted from the input file
def get_goal_predicates(examples):

    return [d['Predicate'] for d in examples]


# get the total distribution of goal predicates
# for instance: total number of yes/no
def get_goal_predicate_frequency(examples, goal_predicate_list):

    # holds total number of occurrence of goal predicates
    frequency = []
    # holds the predicate,respective occurrence value in dictionary
    goal_predicate_distribution = {}

    # count the occurrence and store in the list
    for i in range(len(goal_predicate_list)):
        frequency.append(get_goal_predicates(examples).count(goal_predicate_list[i]))

    # hold the values as (key,value)
    zip_pair = zip(goal_predicate_list, frequency)

    # assign values to the dictionary
    for goal_predicate_list, frequency in zip_pair:
        goal_predicate_distribution[goal_predicate_list] = frequency

    return goal_predicate_distribution


# get the frequency of examples
# i.e. occurrence of an attribute value in an example
# get the total distribution of goal predicates
# for instance: total number of yes/no
def get_example_frequency(examples, name_of_attributes):

    # stores the unique values of an attribute in a list of lists
    unique_example = []
    # holds total number of occurrence of example of an attribute
    frequency = []
    # holds the example value of an attribute and it's frequency together
    example_frequency = {}

    # reads the attributes and its respective example values
    for i in range(len(name_of_attributes)-1):
        unique_example.append(list(set([d[name_of_attributes[i]] for d in examples])))

    # count total occurrence of unique_example in examples
    # count the occurrence and store them in the list
    for i in range(len(unique_example)):
        print 

    return 0


# using entropy to calculate the homogeneity of a sample.
# Entropy is the sum of p(x)log(p(x)) across all the different possible results
# If the sample is completely homogeneous the entropy is zero and
# if the sample is an equally divided it has entropy of one.
# it is based on the overall distribution of predicate
def get_entropy(examples, goal_predicate_list):

    # store the entropy value
    predicate_entropy = 0
    # store the sum of frequencies
    sum_of_frequencies = 0

    # store the dictionary with predicate and its frequency
    frequency_values = get_goal_predicate_frequency(examples, goal_predicate_list)

    for key in frequency_values.keys():
        sum_of_frequencies += frequency_values[key]

    for key in frequency_values.keys():
        predicate_entropy += (-frequency_values[key]/sum_of_frequencies) * math.log(frequency_values[key]/sum_of_frequencies, 2)

    return predicate_entropy


# Entropy using the frequency table of two attributes
# It is the product of Probability and Entropy value of the attribute
def get_entropy_of_two_attributes(examples, goal_predicate_list):

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
        goal_predicate_list = list(set(get_goal_predicates(examples)))

        # invoke get_entropy_of_attributes function
        get_entropy(examples, goal_predicate_list)

        get_example_frequency(examples,goal_predicate_list)
