"""
Learns a decision tree after being given an ARFF file as input. Does
this across random samples of various sizes, then writes a csv that
has average, min, and max accuracy for various sample sizes.

usage: python dt-learn.py train.arff test.arff m
Where m is an integer specifying the min number of training instances
that can reach a node before the node is forced to become a leaf.

Rick Wolf
"""

import sys, math
from Dataset import Dataset
from DecisionTree import DecisionTree
from DecTreeNode import DecTreeNode
import random
import copy





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
	m = 4

	if len(sys.argv) == 4:
		trainFile = sys.argv[1]
		testFile  = sys.argv[2]
		outname = sys.argv[3]
	else:
		sys.exit("Bad input: Please provide a test file, train file, and outfile name")


	# Ingest the datasets
	trainset = readFile(trainFile)
	testset = readFile(testFile)

	# test decision tree constructor
	#a = DecisionTree(trainset, m)

	
	# prep a file for graphing data
	f = open(outname, 'w+')
	f.write('samplePercentage,Accuracy,Min,Max\n')


	# train using various sample sizes
	samplePercs = [0.05, 0.1, 0.2, 0.5]
	for samplePerc in samplePercs:
		# get the number of instances I'll be using
		sampleSize = int(len(trainset.instances)*samplePerc)
		
		# populate the samples
		samples = []
		for i in range(10):
			samples.append(random.sample(trainset.instances, sampleSize))

		accuracies = []
		for sample in samples:
			# train using this sample
			tmpTrain = copy.deepcopy(trainset)
			tmpTrain.overrideInstances(sample)
			tmpTree = DecisionTree(tmpTrain, m)

			scores = []
			for instance in testset.instances:
				scores.append(1 if tmpTree.classify(instance, tmpTree.root) == instance[-1] else 0)
			accuracies.append(float(sum(scores))/len(scores))

		# write the data to a file
		avg = str((float(sum(accuracies))/len(accuracies))*100)
		mi  = str((min(accuracies))*100)
		ma  = str((max(accuracies))*100)
		#f.write(str(samplePerc*100) + ',' + avg + ',Average\n')
		#f.write(str(samplePerc*100) + ',' + mi + ',Minimum\n')
		#f.write(str(samplePerc*100) + ',' + ma + ',Maximum\n')
		f.write(str(samplePerc*100) + ',' + avg + ',' + mi + ',' + ma + '\n')

	# do one more classification accuracy using the whole training set
	scores = []
	a = DecisionTree(trainset, m)
	for instance in testset.instances:
		scores.append(1 if a.classify(instance, a.root) == instance[-1] else 0)
	avg = str((float(sum(scores))/len(scores))*100)
	#f.write('100,' + str((float(sum(scores))/len(scores))*100) + ',Average\n')
	#f.write('100,' + str((float(sum(scores))/len(scores))*100) + ',Minimum\n')
	#f.write('100,' + str((float(sum(scores))/len(scores))*100) + ',Maximum\n')
	f.write('100,' + avg + ',' + avg + ',' + avg + '\n')




if __name__ == "__main__":
	main(sys.argv[:])







