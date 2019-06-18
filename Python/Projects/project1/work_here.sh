#!/bin/sh

mkdir -p inputs outputs

if [ ! -d ./py3 ] ; then
python3 -m venv py3
source py3/bin/activate
python3 -m pip install -r requirements.txt
fi

source py3/bin/activate
