#!/bin/sh

mkdir -p inputs outputs

if [ ! -f ./inputs/data.csv ] ; then
  cp ../data.csv ./inputs/data.csv
fi

if [ ! -d ./py3 ] ; then
  python3 -m venv py3
  source py3/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

if [ ! -f ./project2.py ] ; then
  cp ./project2.backup.py ./project2.py
fi

source py3/bin/activate

jupyter lab
