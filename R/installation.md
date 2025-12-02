# Installation

`sudo apt install r-base libxml2-dev`

Note: libxml2-dev is a dependency for the R languageServer

These packages are required for the tidyverse library:
``` bash
sudo apt install libcurl4-openssl-dev libssl-dev libfontconfig1-dev libfreetype6-dev
```

## (R in Visual Studio Code)[code.visualstudio.com/docs/languages/r]

First install languageServer in R:
Go to the R command prompt by running `R`
Then run:
``` R
install.packages("languageserver", dependencies=TRUE)
```

You will likely hit a permissions error on where to install the lanaguageServer. The simplest solution is to install it in your home directory by specifying `yes`


install.packages("libxml2-dev")




plugin: `REditorSupport.r`

Then state where the R executable is located by running:
```
which R
```
Then in VScode going to `@ext:REditorSupport.r rpath`
Then copy paste the R executable in the field: R > Rpath: Linux




sudo apt install libcurl4-openssl-dev libssl-dev libfontconfig1-dev libfreetype6-dev








Shortcuts:
You can run an R selection by highlighting or leaving your cursor on the line and then hitting `Ctrl + Enter`