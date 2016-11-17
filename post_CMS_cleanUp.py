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

# REGEXES #

# OPF

opf = open(epubFolder + '/content.opf')
opf_contents = opf.read()

# Get rid of new lines

opf_contents = opf_contents.replace('\n', '')
opf_contents = opf_contents.replace('>  <', '><')
opf = open(epubFolder + '/content.opf', 'w')

# Spine regexes

spine_regex = r'<spine toc="ncx" page-progression-direction="ltr"><itemref idref="toc" /><itemref idref="(.*?)" /><itemref idref="(.*?)" />'
spine_subst = r'<spine toc="ncx" page-progression-direction="ltr"><itemref idref="cover" linear="yes" /><itemref idref="\1" /><itemref idref="\2" /><itemref idref="newsletter" /><itemref idref="toc" />'
opf_contents = re.sub(spine_regex, spine_subst, opf_contents)

# Metadata 

## NOTE: Here's the thing, I wanted to find a way to open up the title page, grab the first and last names of the author and place them in the metadata, but since there are so many variations on how this can go down, I thought an input might be better
firstName = raw_input('Author\'s first name: ')
print(firstName)
lastName = raw_input('Author\'s last name: ')
print(lastName)

## regex 

metadata_regex = r'</dc:identifier><dc:date>(.*?)</dc:date><dc:rights></dc:rights><meta name="cover" content="I" />'
metadata_subst = r'<dc:date>\1</dc:date>\n<dc:identifier id="bookid">' + str(ISBN) + r'</dc:identifier>\n<dc:creator id="mainauthor1">' + str(firstName) + ' ' + str(lastName) + r'</dc:creator>\n<meta refines="#mainauthor1" property="role" scheme="marc:relators">aut</meta>\n<meta refines="#mainauthor1" property="file-as">' + str(lastName) + r', ' + str(firstName) + r'</meta>\n<meta refines="#mainauthor1" property="display-seq">1</meta>\n<dc:publisher>Adams Media</dc:publisher>\n<dc:rights>WORLD</dc:rights>\n<meta name="cover" content="Icover.jpg" />'
opf_contents = re.sub(metadata_regex, metadata_subst, opf_contents)


# Re-expand contents
opf_contents = opf_contents.replace('><', '>\n<')
opf_contents = opf_contents.replace('> <', '>\n<')

opf.write(opf_contents)
opf.close()

# NAV.XHTML

nav = open(epubFolder + '/nav.xhtml')
nav_contents = nav.read()
nav = open(epubFolder + '/nav.xhtml', 'w')

nav_regex = r'<ol class="epub_landmarks" epub:type="list">'
nav_subst = r'<ol class="epub_landmarks" epub:type="list">\n<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
nav_contents = re.sub(nav_regex, nav_subst, nav_contents)

nav.write(nav_contents)
nav.close()

# NCX 
ncx = open(epubFolder + '/toc.ncx')
ncx_contents = ncx.read()
ncx = open(epubFolder + '/toc.ncx', 'w')

ncx_regex = r'<meta name="dtb:uid" content="" />'
ncx_subst = r'<meta name="dtb:uid" content="' + str(ISBN) + r'" />'
ncx_contents = re.sub(ncx_regex, ncx_subst, ncx_contents)

ncx.write(ncx_contents)
ncx.close()

# zip it up and zip it out!

