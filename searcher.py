#/usr/bin/python

# import the necessary packages
import numpy as np
import pandas
 
class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
 
	def search(self, queryFeatures, limit = 10):

                # Read in the image matrix with pandas
                database = pandas.read_csv(self.indexPath,header=None,index_col=0)

                # Apply the function to the rows
                results = database.apply(self.chi2_distance,axis=1, args = [queryFeatures])
                results.sort()
                 
		# return our (limited) results
                return results.tolist()[0:limit],results.index[0:limit].tolist()
	
	def chi2_distance(self, histA, histB, eps = 1e-10):
                histA = list(histA)
                histB = list(histB)
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
 
		# return the chi-squared distance
		return d
