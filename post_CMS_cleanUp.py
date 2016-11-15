import re
import os

# OPF

opf = open('content.opf')
opf_contents = opf.read()

# Get rid of new lines

opf_contents = opf_contents.replace('\n', '')
opf_contents = opf_contents.replace('>  <', '><')
opf = open('content.opf', 'w')

# Spine regex

spine_regex = r'<spine toc="ncx" page-progression-direction="ltr"><itemref idref="toc" /><itemref idref="(.*?)" /><itemref idref="(.*?)" />'
spine_subst = r'<spine toc="ncx" page-progression-direction="ltr"><itemref idref="cover" linear="yes" /><itemref idref="\1" /><itemref idref="\2" /><itemref idref="newsletter" /><itemref idref="toc" />'
opf_contents = re.sub(spine_regex, spine_subst, opf_contents)

# Metadata regex

metadata_regex = r'</dc:identifier><dc:date>(.*?)</dc:date><dc:rights></dc:rights><meta name="cover" content="I" />'
metadata_subst = r'''
<dc:date>\1</dc:date>
<dc:identifier id="bookid">ISBN</dc:identifier>
<dc:creator id="mainauthor1">FirstName LastName</dc:creator>
<meta refines="#mainauthor1" property="role" scheme="marc:relators">aut</meta>
<meta refines="#mainauthor1" property="file-as">LastName, FirstName</meta>
<meta refines="#mainauthor1" property="display-seq">1</meta>
<dc:publisher>Adams Media</dc:publisher>
<dc:rights>WORLD</dc:rights>
<meta name="cover" content="Icover.jpg" />
'''
opf_contents = re.sub(metadata_regex, metadata_subst, opf_contents)


# Re-expand contents
opf_contents = opf_contents.replace('><', '>\n<')
opf_contents = opf_contents.replace('> <', '>\n<')

opf.write(opf_contents)
opf.close()

# NAV.XHTML

nav = open('nav.xhtml')
nav_contents = nav.read()
nav = open('nav.xhtml', 'w')

nav_regex = r'<ol class="epub_landmarks" epub:type="list">'
nav_subst = r'<ol class="epub_landmarks" epub:type="list">\n<li><a epub:type="cover" href="cover\.xhtml">Cover</a></li>'

nav.write(nav_contents)
nav.close()

