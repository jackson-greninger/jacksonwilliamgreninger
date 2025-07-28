cd "$1/assignments"
echo ls
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

if [ ${2:+1} ]; then
    pdflatex $2
fi
