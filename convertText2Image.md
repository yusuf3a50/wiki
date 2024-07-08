`convert -size 250x25 xc:white -font "FreeMono" -pointsize 14 -fill black -annotate +15+15 "some text here" email.png && display email.png`


To create a canvas that fits the size of the text, you can use ImageMagick's label: format

`convert -background white -fill black -pointsize 80 label:"Some text here" output.png && display output.png`

#### You need to have the following installed to run this command:

`sudo apt install imagemagick`