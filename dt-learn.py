"""
Learns a decision tree after being given an ARFF file as input.

usage: python dt-learn.py train.arff test.arff m
Where m is an integer specifying the min number of training instances
that can reach a node before the node is forced to become a leaf.

Rick Wolf
"""

import sys, math, dataset



def main(argv):

	# Handle User input
	trainFile = ''
	testFile  = ''
	m = 0

	if len(sys.argv) == 4:
		trainFile = sys.argv[1]
		testFile  = sys.argv[2]
		m = sys.argv[3]
	else:
		sys.exit("Bad input: Please provide a test file, train file, and value for m")


	# Parse the





if __name__ == "__main__":
	main()
