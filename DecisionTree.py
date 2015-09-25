
import math
from Dataset import Dataset
from DecTreeNode import DecTreeNode


class DecisionTree(object):

	def __init__(self, train, m):
		"""
		train: an instance of the Dataset class that constitutes the training data
		m:     the min number of instances that may reach a node before that node is
		       forced to become a leaf node
		"""

		self.labels = train.labels
		self.attributes = train.attributes
		self.attributeValues = train.attributeValues
		self.m = m

		self.root = self.buildTree(train.instances, m)



	def buildTree(self, examples, m, attributes, parentAttrib=None, parentAttribValue=None):
		"""
		recursively builds a decision tree, returning the root node

		examples: instances from the training set (a list of lists)
		m: the number of instances at which to force a leaf
		attributes: a list of attributes that can be split on
		"""

		# get a tuple with the name of the best attribute and its info gain
		splitAndGain = self.bestAttribAndGain(examples)

		# test if this should be a leaf node
		#   are the remaining training instances homogeneous?
		if (self.isHomogeneousSet(examples)):
			return DecTreeNode(parentAttrib, parentAttribValue, True, [], examples[-1])
		#   are there fewer than m instances?
		if (len(examples) < m):
			return DecTreeNode(parentAttrib, parentAttribValue, True, [], 
				self.getMajorityLabel(examples))

		#   do all remaining features have negative information gain?

		#   are there no more remaining candidate splits?






	def determineCandidateNumericSplit(self, instances, attribute):
		"""
		returns a tuple that is the (bestSplit, infoGain)

		instances: the instances involved in deciding this split
		attribute: the string name of the attribute
		"""
		x = self.attributes.index(attribute)
		candidates = []

		# get a sorted list of unique values in the attribute
		uniqueVals = sorted(list(set(zip(*instances)[x])))
		
		# get a dict of instances sorted 
		valSets = {key:[] for key in uniqueVals}
		for instance in instances:
			valSets[instance[x]].append((instance[x],instance[-1]))
		
		# determine if midpoints between set values should 
		# be considered for splits
		for i in range(len(uniqueVals)-1):
			sLabels = set(zip(*valSets[uniqueVals[i]])[1])
			tLabels = set(zip(*valSets[uniqueVals[i+1]])[1])
			# if there exists a pair of instances with different labels between the two sets
			if (len(sLabels) == 2 or len(tLabels) == 2 or not(sLabels == tLabels)):
				candidates.append((uniqueVals[i] + uniqueVals[i+1])/float(2))

		# decide which candidate has the best info gain
		bestGain = float("-inf")
		bestCand = None
		for candidate in candidates:
			candGain = self.getEntropy(instances) - self.getCondEntropyNumeric(instances, x, candidate)
			if candGain > bestGain:
				bestGain = candGain
				bestCand = candidate
		return (candidate, candGain)




	def bestAttribAndGain(self, instances, attributes):
		"""
		returns a tuple that names the attribute with the best info gain,
		and how much info gain that is. If the attribute is numeric,
		the tuple has a 3rd field defining the split point
		"""
		best = ("none", float("-inf"))

		# loop through each attribute and get best info gain
		for attribute in attributes:
			# if the attribute is nominal
			if len(self.attributeValues[attribute] > 1):
				newGain = self.getEntropy(instances) - self.getCondEntropyNominal(instances, attribute)
				if newGain > best[1]:
					best = (attribute, newGain)
			# if the attribute is numeric
			else:
				# get a tuple with a (splitCandidate, infoGain)
				candSplitGain = self.determineCandidateNumericSplit(instances, attribute)
				if candSplitGain[1] > best[1]:
					best = (attribute, candSplitGain[1], candSplitGain[0])

		return best




	def getProbOfLabel(self, instances, label):
		count = sum([1 if instance[-1] == label else 0 for instance in instances])
		return float(count) / len(instances)

	
	def getCondEntropyNumeric(self, instances, attribute, split):
		"""
		Gets conditional entropy of a candidate numeric split
		"""
		# find instances that are less than or equal to the split
		x = self.attributes.index(attribute)
		lteInstances = [instance for instance in instances if instances[x] <= split]
		gtInstances = [instance for instance in instances if instances[x] > split]

		# calculate conditional entropy
		return ((len(lteInstances)/len(instances))*self.getEntropy(lteInstances)) + \
		((len(gtInstances)/len(instances))*self.getEntropy(gtInstances))



	def getCondEntropyNominal(self, instances, attribute):
		"""
		Gets conditional entropy of a nominal attribute
		"""
		xInd = self.attributes.index(attribute)
		valList = self.attributeValues[attribute]

		entSum = 0

		for val in valList:
			valExamples = [instance for instance in instances if instance[xInd] == val]
			entSum += (len(valExamples)/len(instances)) * self.getEntropy(instances)

		return entSum





	def getEntropy(self, instances):
		probPos = self.getProbOfLabel(instances, self.labels[1])
		probNeg = self.getProbOfLabel(instances, self.labels[0])

		if (probNeg == 0 or probPos == 0):
			return 0

		return -1* ((probNeg * math.log(probNeg,2)) + (probPos * math.log(probPos,2)))





	def isHomogeneousSet(self, instances):
		"""
		Returns true if the class label of all of the input training instances are the same
		"""
		label = instances[0][-1]

		for instance in instances:
			if not (label == instance[-1]):
				return False
		return True



	def getMajorityLabel(self, instances):
		"""
		Returns the string name of the class that the most instances in the given set have
		"""

		counts = [0,0]
		for instance in instances:
			if instance[-1] == self.labels[0]:
				counts[0] += 1
			else:
				counts[1] += 1
		return self.labels[counts.index(max(counts))]













