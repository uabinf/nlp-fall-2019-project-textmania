#!/bin/bash

# Assume on Cheaha if we are ssh'd into something
if [ ${#SSH_CONNECTION} -gt 0 ]; then
  module load Python/3.6.3-intel-2017a
fi
# Install virtualenv
pip install virtualenv 

if [ ! -d ./venv ]; then
  virtualenv venv
fi

source ./venv/bin/activate

pip install -r requirements.txt
