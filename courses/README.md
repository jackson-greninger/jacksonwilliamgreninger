The Theory Course Page Formatting Guide
===

This is a quick guide to writing your own course pages in the style as the ones you find here. Each course is in its own folder, which you should give an alphanumeric name. For eg., the Theory of Computation course pages are in the folder `csci341/`. A course folder in this format consists of the  subfolders `assignments/`, `compiled/`, `imgs/`, and `pageconstruction/`, and two html files, `footer.html` and `header.html`. These last two html files should be customized for each course. Knowing the purpose each of the folders has is crucial for understanding how the automated generation of pages works in this format (later).

The most important thing to note: **never touch the `compiled/` folder**. Don't even look at it. It is entirely written over by the `make.sh` shell script.

## Page Construction and Compiled Pages

The `pageconstruction/` folder is where all of the course pages are constructed. In here, you will write an html document (with MathJax if you need it!) for each page. No header or footer is necessary for these files, simply start each page with `<h1>Title of Page</h1>`. 

### Root pages

You will want to include an `assignments.html`, `contents.html`, `index.html`, and `resources.html` in this folder. You can change the names of these files, but if you do, you will want to also change the `header.html` file as well. The use of `contents.html` in particular is of some importance, because that is how you will link students to the Notes pages.

**Note.** If you are going to link to a course page, do not link it to a page in the `pageconstruction/` folder. That folder is only for designing pages. Link it to the corresponding page name in the `compiled/` folder (which you should not touch). These files will have page names of the form `coursename_..._pagename.html`. If you are not sure what the page will be called, make a file for it in the `pageconstruction/` folder and try running `make.sh` (see instructions below).

### Notes pages

Notes pages are a special type of page that are different than the Root pages. They are all tied together with "next topic" and "previous topic" buttons that allow students to skip through the rest of the notes pages in alphabetical order (more on this in a second). In order for the page script to recognize an html document as a Notes page is by its file name: **every Notes page is a string of the form**
```
notes_#_##_name_of_topic.html
```
The first `#` is intended to be a "chapter" number and the proceeding `##` is intended to be a "section" number. The "next topic" and "previous topic" buttons are built by the `./make.sh` script automatically and the buttons themselves are labelled as `name of topic`, as it is scraped from the name of the html file. See [this csci341 page](./csci341/compiled/csci341_notes_1_03_language_acceptance.html) for an example.

## Assignments

This is a standard kind of folder for course design. It consists of documents written in LaTeX and the PDFs that they generate. The `make.sh` will try to compile these LaTeX documents with `pdflatex` as it is running. If you are worried about a bunch of useless log files making their way into this folder, don't fret---the page generator will annihilate them! These files you need to link to manually from the `pageconstruction/` folder.

# Automated Page Generation

Once you have set up the `header.html`, `footer.html`, Root and Notes pages in `pageconstruction/`, it's time to build the website. This is where the `./make.sh` script comes in: you simply navigate to the `courses/` folder in your shell/terminal and run the command 
```
./make.sh coursename
```
If you get a permission error, you may need to run 
```
chmod +x ./make.sh
```
first. 

The `make.sh` script scrapes the `pageconstruction/` folder for "bodies", and then runs a python script called `compilepages.py` that straps the `header.html` to the beginning and the `footer.html` to the end of each page, and creates "next topic" and "previous topic" buttons for all the Notes pages, and piles everything into the `compiled/` folder. 

Also, because I hate aux files, `make.sh` will attempt to obliterate anything in the `assignments/` folder that is a log file, an aux file, or any other auto-generated file that `pdflatex` produces (other than `.bbl` of course).

You should now be able to preview your web pages by opening the html files in the `compiled` folder in your browser.

### Optional: Running `pdflatex` with the `make.sh` script
If you add an additional argument to the `make.sh` script, it will also look for a LaTeX file of that name in the `assignments/` folder, run `pdflatex` on it, and clean up the whole  `assignments/` folder for you to remove log files and the like.
```
./make.sh coursename assignment1
```
This actually runs the following script: 
```
pdflatex -interaction=batchmode $2.tex
biber -q $2
pdflatex -interaction=batchmode $2.tex
```
with a call to biber in the middle. Currently there is no support for bibtex, but I felt that was overkill for this application.

### Optional: `make_and_push.sh`

For the ultra-lazy, there is also a script called `make_and_push.sh`, which takes two parameters:
```
./make_and_push.sh coursename "Commit message for git"
```
It's exactly how it sounds: it basically runs 
```
./make.sh coursename
git add *
git commit -m "Commit message for git"
git push
``` 
Not secure at all, but I use it all the time :D