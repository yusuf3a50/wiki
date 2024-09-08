#### Descend into every folder with current working directory and do something:

`for d in */; do echo "$d"; done`

or create a folder within each folder:

`for d in */; do mkdir "$d"/new_folder; done`

The / at the end tells, use directories only

##### Copy a document into each folder that exists in the current working directory whilst naming each copy the document to contain the name of the containing folder
```
for d in */; do
    d="${d%/}"  # Remove trailing slash
    cp DocumentName.docx "$d"/DocumentName_"$d".docx
done
```

#### Find and delete
**Use the following with CAUTION!**
```
find . -name folderName -exec rm -r {} \;
find . -name __pycache__ -exec rm -r {} \;
```

#### Make multiple copies of a file, filenames relative to each newLine in a fileName.txt file:
there is a file named as follows:
filename(TEMPLATE).xlsx
there is another file as follows:
studentsList.txt

in bash, make many copies of filename(TEMPLATE).xlsx, one for each student as listed in studentsList.txt (new line separated text file) naming each copied file with the name of the student for example:

filename(AliceSmith).xlsx
filename(BobSmith).xlsx
etc etc

```
#!/bin/bash

# Define the template file
template_file="filename(TEMPLATE).xlsx"

# Read each line from studentsList.txt
while IFS= read -r student; do
    # Create a new filename based on the student's name
    new_filename="filename(${student}).xlsx"
    
    # Copy the template file to the new filename
    cp "$template_file" "$new_filename"
done < studentsList.txt
```

#### convert a spreadsheet into a text file with specific format
1. save the spreadsheet of two columns and multiple rows as a CSV file. 
2. convert the CSV file into a text file where the two columns are concatenated and each new row is a new line. also add underscores between first and second row and also any additional whitespaces
```
awk -F, '{gsub(/ /, "_", $1); gsub(/ /, "_", $2); print $1 "_" $2}' data.csv > output.txt
```