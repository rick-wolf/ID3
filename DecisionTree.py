
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



	def buildTree(self, examples, m, parentAttrib=None, parentAttribValue=None):
		"""
		recursively builds a decision tree, returning the root node

		examples: instances from the training set (a list of lists)
		m: the number of instances at which to force a leaf
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






	def determineCandidateNumericSplits(self, instances, x):
		"""
		instances: the instances involved in deciding this split
		x: the index of the name of this feature in 
		"""



	def bestAttribAndGain(self, instances):
		"""
		returns a tuple that names the attribute with the best info gain,
		and how much info gain that is.
		"""
		best = ("none", float("-inf"))


	def getProbOfLabel(self, instances, label):
		count = sum([1 if instance[-1] == label else 0 for instance in instances])
		return float(count) / len(instances)


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













