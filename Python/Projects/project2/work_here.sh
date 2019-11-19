#!/bin/sh

# work_here.sh is a shell script (it's not python).
# shell scripts are just another way to tell your computer what to do.
# you could perform all of the actions
# in this script manually (on a command line), but these steps should not be
# the focus of the lesson. I put the shell script here so you could ignore
# the details of project setup for now. I'll write a translation/explanation
# of what's happening right above each line.

# "Make two directories (folders), named 'inputs' and 'outputs'"
# The p flag (-p) means that it's ok if the folders exist already.
# see note 1 below for more details.
mkdir -p inputs outputs

# "If there is not a file called data.csv in a folder called inputs, then
# copy data.csv from the folder one level up (just outside the project folder)
# and put the copy in the inputs folder"
# I copy the data.csv file this way so I only have one original to keep track
# of, and I copy it into whatever project I'm using it for.
if [ ! -f ./inputs/data.csv ] ; then
  cp ../data.csv ./inputs/data.csv
fi

git pull

read -p "Reset python environment? (y/n)" result
case "$result" in
  y|Y ) rm -fR py3 ;;
  n|N ) true ;;
esac

# "If there is not a directory called py3, then do the following things:
#    1. create a virtual environment here called py3
#    2. activate that environment so all python commands run inside the new
#        environment
#    3. upgrade python's package installer (pip)
#    4. install all the packages listed in requirements.txt"
if [ ! -d ./py3 ] ; then
  python3 -m venv py3
  source py3/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

# "If there is not a file called project2.py, then
# copy the file project2.backup.py and call the project2.py"
# I copy projects this way so the project's "starting point" is saved,
# and you can make changes to project2.py without worrying about losing the
# original. It also allows you to get updated projects (with git pull) without
# those updates overwriting your current work.
if [ ! -f ./project2.py ] ; then
  cp ./project2.backup.py ./project2.py
fi

# "activate the virtual environment"
# This makes sure the virtual environment gets activated even if it already
# exists.
source py3/bin/activate

# This starts jupyter lab in your browser. Starting jupyter lab from the script
# Makes sure that when you stop jupyter lab, you don't need to deactivate your
# environment
jupyter lab

# Note 1: The p flag also creates parent directories as needed, but that's not
# a relevant detail for how I'm using it here. Parent directories are folders
# that hold other folders. The command "mkdir -p parent1/child1/inputs" will
# create: a folder parent1 (if it doesn't exist),
#         a folder child1 inside of parent1 (if it doesn't exist),
#         and a folder inputs inside of child1 (if it doesn't exist).
# The command "mkdir parent1/child1/inputs" will only create the last folder
# (inputs) and it will only do that if the other two folders already exist.
# If they don't, or if the inputs folder already exists,
# "mkdir parent1/child1/inputs" will produce an error message.
