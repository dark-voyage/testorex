#!/bin/bash
# shellcheck disable=SC2164
cd "$(dirname "$0")"

# Let's install the applications first
printf "======= INSTALLATION ======="
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

printf "======= RUNNING APP  ========"
python main.py