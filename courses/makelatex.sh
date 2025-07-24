file $2
cd "$1/assignments"
echo ls
pdflatex $2
rm *.aux
rm *.bcf
rm *.fdb_latexmk
rm *.fls
rm *.idx
rm *.ilg
rm *.ind
rm *.log
rm *.out
rm *.xml
rm *.gz
cd ../../
python3 compilepages.py $1
