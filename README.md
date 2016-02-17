
Usage:
My program is compatible with Python 3.x. There will be some issues running it on 2.x versions. 

Decision Tree - Classification

Decision tree builds classification or regression models in the form of a tree structure. It breaks down a dataset into smaller 
and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with 
decision nodes and leaf nodes. A decision node (e.g., Outlook) has two or more branches (e.g., Sunny, Overcast and Rainy). 
Leaf node (e.g., Play) represents a classification or decision. The topmost decision node in a tree which corresponds to the best 
predictor called root node. Decision trees can handle both categorical and numerical data.

Algorithm

The core algorithm for building decision trees called ID3 by J. R. Quinlan which employs a top-down, greedy search through the 
space of possible branches with no backtracking. ID3 uses Entropy and Information Gain to construct a decision tree.
