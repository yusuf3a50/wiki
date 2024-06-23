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

