#!/usr/bin/env bash

python -m venv venv
source venv/Scripts/activate
pip install pip --upgrade
pip install --upgrade -r requirements.txt