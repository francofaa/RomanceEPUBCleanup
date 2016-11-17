import zipfile
import os
import shutil
# import re
# from datetime import datetime

# set our directory to the current one where the python script lives
weekFolder = os.getcwd()

# our cover file should also be in this directory (Crimson Week number directory)
# this finds the cover file, which should contain the ISBN and puts it in a var called ISBN that removes the jpg extension
for file in os.listdir(weekFolder):
	if file.endswith('.jpg'):
		ISBN = os.path.splitext(file)[0]

# this creates the directory where we'll place our epub content from the file called not_named.epub, as automatically titled by the CMS
os.mkdir(ISBN)
zip_ref = zipfile.ZipFile('not_named.epub', 'r')
zip_ref.extractall(ISBN)
zip_ref.close()

# this var will place us in the correct folder for the next edits
epubFolder = os.path.join(weekFolder + '/' + ISBN + '/OEBPS')
print epubFolder


# this will rename our cover image to cover.jpg  and set up a variable so that we can move coverImg
os.rename(ISBN + '.jpg', 'cover.jpg')

for file in os.listdir(weekFolder):
	if file.endswith('.jpg'):
		coverImg = file

# this copies over our old image
shutil.copy(coverImg, epubFolder + '/images')



# regex = str('')



# print(os.path.splitext('/tmp/test.txt'))


# curDirList = os.rename(curDirList[7], 'ReadMe2.md')

# shows you when the file was modified last 
# mod_time = os.stat('README.md').st_mtime

# print(datetime.fromtimestamp(mod_time))

# generates a directory path -- traverses from top down -- thre value tuple

# for dirpath, dirnames, filenames in os.walk(curDir):
#	print('Current Path:', dirpath)
#	print('Directories:', dirnames)
#	print('Files:', filenames)
#	print(' ')


# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# this pulls out the extension! 
# print(os.path.splitext('/tmp/test.txt'))