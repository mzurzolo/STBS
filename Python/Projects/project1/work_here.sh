#!/bin/sh

mkdir -p inputs outputs

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

echo "\nRemember to run \"deactivate\" when you're done with this project"
