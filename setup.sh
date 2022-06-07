#!/bin/bash

echo Creating virtual environment...
python3 -m venv venv

echo Installing requirenments...
source venv/bin/activate
pip3 install -r requirements.txt
