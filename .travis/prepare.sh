#!/bin/bash
set -e

apt-get update
apt-get -y install python3-dev libffi-dev virtualenv build-essential
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
rm -rf crm_env
virtualenv -p python3 crm_env
./crm_env/bin/pip3 install -r requirements.pip