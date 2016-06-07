#!/bin/bash

if [ ! -d .venv ]
then
    virtualenv -p /usr/bin/python3 .venv
fi

. .venv/bin/activate

pip install -r requirements.txt

python ./update-releases.py

