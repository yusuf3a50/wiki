#### create pdf from a jpg
`img2pdf *.jpg --output combined.pdf`


#### create png(s) from a pdf
```
sudo apt install poppler-utils
pdftoppm -png filename.pdf output
```
The output file name will be output-1.png, output-2.png, output-3.png etc..


#### reduce size of a pdf (NOT CLI!!)
Open PDf with LibreOffice Draw
File > Export > Export as PDF > JPG compression, quality: xx%


#### Remove the first page: 
```
sudo apt-get install qpdf
qpdf input.pdf --pages . 2-z -- output.pdf
```

This command specifies to include pages from the second to the last in the output PDF.