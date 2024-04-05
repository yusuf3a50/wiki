Descend into every folder with current working directory and do something:

`for d in */; do echo "$d"; done`

or create a folder within each folder:

`for d in */; do mkdir "$d"/new_folder; done`

The / at the end tells, use directories only