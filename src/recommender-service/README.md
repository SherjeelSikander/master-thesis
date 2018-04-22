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

# If using VS code don't forget to update python.pythonPath in .vscode/settings.json to the python installed inside the env folder e.g.
{
    "python.pythonPath": "D:\\Documents\\Thesis\\master-thesis\\src\\recommender-service\\env\\Scripts\\python.exe"
}

########## FOR DEVELOPMENT - running flask API ##########

# on Windows enter the following on command line
$ env/Scripts/activate
# on Linux enter the following on command line
$ source env/venv/bin/activate

# to start the api service
$ python api.py

References:
https://developer.akamai.com/blog/2017/06/21/building-virtual-python-environment/
http://mherman.org/blog/2017/04/26/flask-for-node-developers/#.WtswQYhuZPY
https://www.python.org/dev/peps/pep-0405/#isolation-from-system-site-packages
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask