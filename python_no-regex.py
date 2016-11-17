##### Pieces of this exist in the main python script (post_CMS_cleanUp.py) but I made this so that I did not run a regex every time I wanted to test these functions

import re
import zipfile
import os
import shutil
# set our directory to the current one where the python script lives
weekFolder = os.getcwd()

# our cover file should also be in this directory (Crimson Week number directory)
# this finds the cover file, which should contain the ISBN and puts it in a var called ISBN that removes the jpg extension
for file in os.listdir(weekFolder):
	if file.endswith('.jpg'):
		ISBN = os.path.splitext(file)[0]

# this creates the directory named ISBN where we'll place our epub content extracted from the file called not_named.epub, as automatically titled by the CMS
os.mkdir(ISBN)
zip_ref = zipfile.ZipFile('not_named.epub', 'r')
zip_ref.extractall(ISBN)
zip_ref.close()

# this var will place us in the correct folder for the next edits
epubFolder = os.path.join(weekFolder + '/' + ISBN + '/OEBPS')

# this will rename our cover image to cover.jpg  and set up a variable so that we can copy coverImg over the blank placeholder cover image
# !! I am sure there is a better way to do this ; for some reason simply renaming the ISBN.jpg file does not create a path for it ; I simply copied from line 10 
os.rename(ISBN + '.jpg', 'cover.jpg')

for file in os.listdir(weekFolder):
	if file.endswith('.jpg'):
		coverImg = file

# this copies over our placeholder image
shutil.copy(coverImg, epubFolder + '/images')
