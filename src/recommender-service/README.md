########## FOR REFERENCE - Creating isolated environment and the dependencies in requirements.txt ##########

Steps for creating a virtual environment:

$ pip install virtualenv

# cd to src/recommender-service folder

$ virtualenv env
# env can be any name. The above command will create a folder called 'env' which will contain the virtual environment.

# on Windows enter the following on command line
$ env/Scripts/activate
# on Linux enter the following on command line
$ source env/venv/bin/activate

#       PS D:\.... will change to 
# (env) PS D:\....

$ pip install Flask==0.12.2

$ pip freeze > requirements.txt

########## FOR DEVELOPMENT - how to run isolated environment and install dependencies ##########
$ pip install virtualenv

# On Windows
$ virtualenv env 
$ env/Scripts/activate

# On Linux
$ virtualenv env source myproject/venv/bin/activate 

$ git clone
$ (venv) user@machine $ cd [to where the project is]
$ pip -r requirements.txt

# If using VS code don't forget to update python.pythonPath in .vscode/settings.json to the python installed inside the env folder

########## FOR DEVELOPMENT - running flask API ##########

# on Windows enter the following on command line
$ env/Scripts/activate
# on Linux enter the following on command line
$ source env/venv/bin/activate

$ python api.py