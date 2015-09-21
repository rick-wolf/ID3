






class Dataset(object):
	"""
	A class representing relevant information about a dataset used for training a 
	decision tree using the ID3 algorithm
	
	Attributes:
	labels: a list of the possible class labels, probably just 0 or 1
	attributes: a list of attribute names (i.e., the x variables)
	attributeValues: a dictionary where attribute names are keys and
					values are the lists of possible values each var can take
	instances: a list of instances

	Author: Rick Wolf
	"""

	def __init__(self, labels, attributes, attributeValues, instances):