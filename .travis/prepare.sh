#!/bin/bash
set -e

sudo apt-get update
sudo apt-get -y install python3-dev libffi-dev virtualenv build-essential
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
pip install --user -r requirements.pip