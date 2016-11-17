#Using Python to clean up CMS-generated EPUB
Hello! I am developing a Python script to clean up files that have been exported from a specific CMS. I encountered a problem wherein the metadata feed for this CMS was not up-to-date for this particular series of books, so I would have to manually place the cover into the EPUB in addition to adding metadata (ISBNs, author name) and various forms of navigation (landmarks and changes to the OPF spine). Emmet in Sublime Text 3 helped to some extent, but I wanted a more automated solution. This solution is very specific to the files I am creating, but perhaps you will find something helpful in it. At any rate, this is my first Python script, so I also took it as a learning opportunity. 

##Folder Structure
CMS export to EPUB creates a file called **not_named.epub** (if you do not have assigned metadata, which these series of titles do not). In this new workflow, I will create a folder named after the title of the book (as I already do), in this case **GenericTitle**. In this folder will be the exported EPUB, the cover jpeg which is helpfully named for the ISBN (in this case **9780000000000.jpg**), and the script itself, **romance.py**.

##Process
This script first prompts the user to enter the author's name[1], then takes the contents of the EPUB file, edits them using regular expressions, replaces the placeholder cover with the proper one, renames the EPUB file after the ISBN and parent folder (so we get **9780000000000_GenericTitle.epub**), zips it back up, and deletes the folder and original CMS EPUB export. This creates a valid EPUB3 file.

##Goals

- Replace content in the OPF spine using regex
- Replace landmarks in the OPF spine using regex
- Replace content in the OPF metadata field and the NCX with content pulled from other files (namely ISBNs, which are helpfully named in the cover jpegs I am provided)
- Unzip, rename by ISBN, and rezip EPUB file

##Sandbox
The folders demonstrate before and afters for running the script. The main version of the python script is at the top.

====
[1]: I was unable to automate the author name input because of the variations in possible author names (first, middle, last; first, middle initial, last; mononyms; juniors and seniors; double-barrelled last names, whether Spanish, Portuguese, hyphenated, etc.) and because the OPF must list author names as both in full and last name first. Instead I settled for a manual input in the terminal. You are prompted enter in the first and last names of the author, which is then put into the appropriate metadata fields in the OPF.
