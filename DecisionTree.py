
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

		#self.root = buildTree



	@staticmethod
	def buildTree(examples, attributes, parentAttribValue, m):
		"""
		recursively builds a decision tree

		examples: instances from the training set (a list of lists)
		attributes: a list of possible attributes to split on
		parentAttribValue: the value of the attribute split at the parent node
		"""

		# test if this should be a leaf node
		#   are the remaining training instances homogeneous?

		#   are there fewer than m instances?

		#   do all remaining features have negative information gain?

		#   are there no more remaining candidate splits?