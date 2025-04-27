Automated Page Generation
===

The Python script `compilepages.py` exists so that I don't need to edit the generic parts of every page.
It's kind of here because you can't run PHP in GitHub Pages...

## What `compilepages.py` does
Each course gets its own folder, usually just the course numbering in the Bucknell course catalog. 
Within each folder, there are two html files and three folders:
    - The first folder is the `pageconstruction/` folder, and this contains all of the main bodies of the course pages. 
    - The html files are `header.html` and `footer.html`. These are the bits of html that the `compilepages.py` script will tag onto the beginning and end of each course page.
    - The second folder is the `compiled/` folder. This is the user-facing content.
    - The third folder is the `imgs/` folder. This is where the html pages will be sourcing its images from.

The script `compilepages.py` stitches the pages in `pageconstruction` together with the header and footer and then dumps the result into the `compiled` folder.

<div style="color:red"><b>Do not edit the files inside `compiled/` directly. They will be overwritten by `compilepages.py`.</b></div>

## Running `compilepages.py`
To run the `compilepages.py` script so that it gives the correct result, *the course folders must be set up correctly.* Refer to the next section for details.

To run the script, navigate to the `courses/` folder and run 
```
python compilepages.py coursename
```
with `coursename` the name of the *folder* where the course pages have been set up.

## Course Setup
To make proper use of the course structure and the `compilepages.py` script, you should follow these guidelines:
1. Provide `index.html`, `syllabus.html`, `resources.html`, and `notes.html` files.
    - `index.html` is a short page. It contains simple logistical information, the course description, and a schedule.
    - `syllabus.html` is a long page. It contains all logistical information, the guidelines and rules, pointers to campus resources, etc.
    - `resources.html` contains links to any code, videos, external lecture videos, documentation, etc. that the students might be interested in, that might not fit into the notes neatly. For example, final project ideas might fit here.
    - `notes.html` contains the table of contents for the course notes.
2. Style your course notes like in the following example: 
    ```
    coursenotes
        ↳ 1_introduction.html
        ↳ 2_decisionproblems.html
        ↳ 3_automata.html
    ```
    This style of numbering will help keep things in order.
    **However**, you will need to update the `notes.html` links yourself if you change the sequencing of the pages. 

If you would like to minimize the amount of junk in your `compiled/` folder, it is good practice to clear it out before compiling each time.