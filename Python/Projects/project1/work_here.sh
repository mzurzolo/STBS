#!/bin/sh

mkdir -p inputs outputs

if [ ! -f ./inputs/data.csv ] ; then
  cp ../data.csv ./inputs/data.csv

if [ ! -d ./py3 ] ; then
  python3 -m venv py3
  source py3/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

if [ ! -f ./project1.py ] ; then
  cp ./project1.backup.py ./project1.py
fi

source py3/bin/activate

printf "\nRemember to run \"deactivate\" when you're done with this project\n\n"
