### Python virtual environments:

This is basically node_modules, python style

`sudo apt install python3-venv`

`python3 -m venv .venv`

`bash .venv/bin/activate`

Once virtual environment is activated, project dependecies can be installed from requirements.txt with command:

`pip3 install -r requirements.txt`

### Upgrade python to version 3.12:

```
sudo add-apt-repository ppa:deadsnakes/ppa
 sudo apt update
 gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys 0xBA6932366A755776
 gpg --export --armor BA6932366A755776 | sudo apt-key add -
 sudo apt update
 sudo apt install python3.12 python3.12-venv
```

Then to set up a virtual environment in python3.12 youd then need:
```
python3.12 -m venv --upgrade .venv 
python3.12 -m venv .venv
source .venv/bin/activate   #this changes the terminal to python version 3.12
pip3 --version              #check whether pip will work for your python3.12
pip3 install -r requirements.txt
```