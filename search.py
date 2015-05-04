# import the necessary packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
ap.add_argument("-m", "--mask", required = True,
	help = "Path to image mask (same size as images) to break into a grid")
ap.add_argument("-g", "--gridsize", required = True,
	help = "Dimension for a single width/height for the square grid mask")
args = vars(ap.parse_args())
 
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3),args["mask"],args["gridsize"])

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)
 
# perform the search
searcher = Searcher(args["index"])
scores,image_names = searcher.search(features)
 
# display the query
cv2.imshow("Query", query)
 
# loop over the results
for x in range(0,len(scores)):
        resultID = image_names[x]
        print "Similar image %s is %s, score: %s" %(x,resultID,scores[x])
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
