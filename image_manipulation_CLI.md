#### batch rotate 90 degrees clockwise
`find . -maxdepth 1 -type f -name "*.jpg" -exec convert {} -rotate 90 {} \;`

#### batch convert JPGs to greyscale and put them into folder called 'grey'
`mkdir grey; for JPG in *.jpg; do jpegtran -grayscale "$JPG" >"grey/${JPG%.jpg}".jpg; done`

#### create pdf from a jpg
`img2pdf *.jpg --output combined.pdf`

#### reduce size of a pdf (NOT CLI!!)
Open PDf with LibreOffice Draw
File > Export > Export as PDF > JPG compression, quality: xx%