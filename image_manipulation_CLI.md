#### batch rotate 90 degrees clockwise
`find . -maxdepth 1 -type f -name "*.jpg" -exec convert {} -rotate 90 {} \;`

#### batch convert JPGs to greyscale and put them into folder called 'grey'
`mkdir grey; for JPG in *.jpg; do jpegtran -grayscale "$JPG" >"grey/${JPG%.jpg}".jpg; done`

##### or for a single image:
`jpegtran -grayscale foo.jpg > foo_greyScale.jpg`

#### create pdf from a jpg
`img2pdf *.jpg --output combined.pdf`

#### reduce size of a pdf (NOT CLI!!)
Open PDf with LibreOffice Draw
File > Export > Export as PDF > JPG compression, quality: xx%

#### Compressing Image to a fixed size using jpegoptim
We can compress the image to a fixed size which we want, for that we have to use the –size option with jpegoptim command and mention the size of the image that we want after compressing. Let’s compress the same gfg.jpg file to 200k using jpegoptim with –size option.

`jpegoptim --size=200k gfg.jpg`
or
`mkdir reducedSize; for JPG in *.jpg; do jpegoptim --stdout --size=200k "$JPG" > "reducedSize/${JPG%.jpg}".jpg; done`