


class DecTreeNode(object):

	def __init__(self, attribute, parentAttribVal, terminal, children=[], label=None, split=None, numNeg=0,
		numPos=0):
		"""
		attribute:       the name of the attribute being split at this node
		parentAttribVal: the value of the attribute split at the parent node
		terminal:        boolean whether or not this node is a leaf
		children:        a list of the decision tree nodes stemming from here
		label:           if a leaf, whether the decision is positive or negative
		split:           if attribute is numeric, the split for the attribute
		"""

		self.attribute = attribute
		self.parentAttribVal = parentAttribVal
		self.terminal = terminal
		self.children = children
		self.label = label
		self.split = split
		self.numNeg = numNeg
		self.numPos = numPos



	def addChild(self, child):
		"""
		add a child node to the list
		"""

		self.children.append(child)


	def setSplit(self, split):
		self.split = split