#!/usr/bin/env bash
# Requirements
# pip install pycodestyle==2.7.0
# pip install pep8==1.7.0

## Code tests
# Runs the unit tests for this project in both the
# interactive and non-interactive modes
echo -e "\e[104m Running Unit Tests \e[0m\e[33m"
python3 -m unittest discover tests
echo "python3 -m unittest discover tests" | bash
[ "$(echo -n $?)" == "0" ] && echo -ne "\e[100m\e[32m PASSED "
echo -e "\e[0m"

## Python code style checks
echo -e "\e[104m Running Style Checks \e[0m\e[31m"
Src_Files="$(find . -type f -regex '.*.py' | tr '\n' ' ')"
# shellcheck disable=SC2086
pycodestyle $Src_Files
if [[ "$(($? + 0))" == "0" ]]; then
    # shellcheck disable=SC2086
    ~/.local/bin/pep8 $Src_Files
    [ "$(echo -n $?)" == "0" ] && echo -ne "\e[100m\e[32m PASSED "
fi
echo -ne "\n\e[0m"
