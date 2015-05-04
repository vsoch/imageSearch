# import the necessary packages
import numpy as np
from scipy import misc
import cv2
 
class ColorDescriptor:
	def __init__(self, bins, mask, grid_size):
		# store the number of bins for the 3D histogram
		self.bins = bins
                self.mask = mask
                self.grid_size = int(grid_size)
 
	def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []
 
                # Read in the mask image - misc handles transparency
                mask = misc.imread(self.mask)
                xblocks, yblocks = np.array(mask.shape[0:2])/self.grid_size
     
                #            
                # loop over the blocks and calculate histograms for each nonzero
                self.xblocks = []
                self.yblocks = []
                for xblock in range(0,xblocks):
                    x = xblock*self.grid_size
                    for yblock in range(0,yblocks):
                        y = yblock*self.grid_size
                        binmask = np.zeros(mask.shape[0:2],dtype="uint8")
                        binmask[x:(x+self.grid_size),y:(y+self.grid_size)] = 1
                        # This is if we want to save the mask grid images to visually check
                        #new_img = np.copy(mask)
                        #new_img[binmask==1,0] = 247
                        #new_img[binmask==1,1] = 53
                        #new_img[binmask==1,2] = 99
                        #print "%s_%s_block.png" %(xblock,yblock)
                        #misc.imsave("/home/vanessa/Desktop/img/%s_%s_block.png" %(xblock,yblock),new_img)                        
                        # Only extract if the entire roi isn't transparent
                        if not np.sum(mask[binmask==1,3]) == 0:
			    # extract a color histogram and update feature vector
			    hist = self.histogram(image, binmask)
			    features.extend(hist)
  
		# return the feature vector
		return features

	def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the
		# image, using the supplied number of bins per channel; then
		# normalize the histogram
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, 
                                    [0, 180, 0, 256, 0, 256])
		hist = cv2.normalize(hist).flatten()
 
		# return the histogram
		return hist
