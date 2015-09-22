






class Dataset(object):
	"""
	A class representing relevant information about a dataset used for training a 
	decision tree using the ID3 algorithm
	
	Attributes:
	labels: a list of the possible class labels, probably just 0 or 1
	attributes: a list of attribute names (i.e., the x variables)
	attributeValues: a dictionary where attribute names are keys and
					values are the lists of possible values each var can take.
					When an attrib can take real number values, this simply states
					'real'.
	instances: a list of instances, where each instance is a list of attribute values

	Author: Rick Wolf
	"""

	def __init__(self, labels, attributes, attributeValues, instances):
		
		assert len(attributes) == len(instances[0])
		assert len(labels) == 2

		self.labels = labels
		self.attributes = attributes
		self.attributeValues = attributeValues
		self.instances = instances



	

