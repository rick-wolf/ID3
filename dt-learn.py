"""
Learns a decision tree after being given an ARFF file as input.

usage: python dt-learn.py train.arff test.arff m
Where m is an integer specifying the min number of training instances
that can reach a node before the node is forced to become a leaf.

Rick Wolf
"""

import sys, math
from Dataset import Dataset
from DecisionTree import DecisionTree
from DecTreeNode import DecTreeNode





def readFile(fname):
		"""
		Takes a filename of an ARFF file from the current directory and returns
		a Dataset object
		"""

		attributes = [] # an ordered list of the attribute names
		attributeValues = {} # a dictionary with attrib name as keys
		instances = []
		labels = []

		lines = open(fname, 'r')
		for line in lines:
			if not (line.startswith("%")):
				line = line.strip("\n")
				if (line.startswith("@attribute")):
					# line is now a list of words
					line = [word.lstrip("{ '\t").rstrip("} ',\t") for word in line.split() if word != '{']
					if (line[1] == "class"):
						labels = line[2:]
					else:
						attributes.append(line[1]) # the name will always be the second item
						attributeValues[line[1]] = line[2:] #the third to end of the list is the values
				elif  not (line.startswith("@")):
					line = line.split(',')
					newline = []
					for i in range(len(attributes)):
						if len(attributeValues[attributes[i]]) == 1:
							newline.append(float(line[i]))
						else:
							newline.append(line[i])
					newline.append(line[-1])
					instances.append(newline[:])
					


		return Dataset(labels, attributes, attributeValues, instances)



def main(argv):

	# Handle User input
	trainFile = ''
	testFile  = ''
	m = 0

	if len(sys.argv) == 4:
		trainFile = sys.argv[1]
		testFile  = sys.argv[2]
		m = float(sys.argv[3])
	else:
		sys.exit("Bad input: Please provide a test file, train file, and value for m")


	# Ingest the datasets
	trainset = readFile(trainFile)
	testset = readFile(testFile)


	# test decision tree constructor
	print m
	a = DecisionTree(trainset, m)

	
	#print(a.attributes)
	#print(a.attributeValues)
	#print(a.m)
	print(a.root.children)








if __name__ == "__main__":
	main(sys.argv[:])
