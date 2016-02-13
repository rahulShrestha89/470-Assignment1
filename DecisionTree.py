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


class DecisionTree:

    # generator function to map key-value pair
    # and holds values respective to attributes
    # i.e. attributes with respective example values
    # in a dictionary
    def get_examples(examples, attributes):
        for value in examples:
            yield dict(zip(attributes, value.strip().replace(" ", "").split(',')))

    # filters the repeated examples
    # and returns a non redundant list of dictionary of examples
    def get_non_redundant_examples(all_redundant_examples):
        for value in all_redundant_examples:
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
                all_redundant_examples = file.readlines()

            # holds all the examples as a list of dictionary
            # for instance: dic=[{'name_attributes': respective_example_value_from_the_file},...{}]
            all_redundant_examples = get_examples(all_redundant_examples, name_of_attributes)

            # stores the non redundant examples
            examples = get_non_redundant_examples(all_redundant_examples)
