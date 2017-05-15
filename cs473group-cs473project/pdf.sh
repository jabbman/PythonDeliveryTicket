cd LatexTicketTemplate
cd temp
rm *.pdf #remove other existing pdf files to prevent directory congestion from pdf files
cd ..
pdflatex -output-directory temp $1
#open $2
cd temp
rm *.png
rm *.tex
rm *.log
rm *.aux

