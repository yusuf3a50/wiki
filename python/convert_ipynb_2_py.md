# Convert between jupyter notebook files and python files

`nbconvert` converts `.ipynb` to `.py`

### Install with: 

``` bash
pip install nbconvert
```

### Then run:
``` bash
jupyter nbconvert --to script notebook.ipynb
```
#### Outputs `notebook.py`


## Converts the other way round:

``` bash
jupyter nbconvert --to notebook your_script.py
```

### Use a Git pre-commit hook with nbconvert. Steps:

Install nbconvert: `pip install nbconvert`

Create .git/hooks/pre-commit in your repo with:

``` bash
#!/bin/bash
for ipynb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    jupyter nbconvert --to script "$ipynb"
    py_file="${ipynb%.ipynb}.py"
    git add "$py_file"
done
```

Make executable: `chmod +x .git/hooks/pre-commit`

On each git commit, this converts staged .ipynb files to .py, overwrites existing .py files, and stages them for commit.