#!/usr/bin/env bash
# Runs the unit tests for this project in both the
# interactive and non-interactive modes
python3 -m unittest discover tests
echo "python3 -m unittest discover tests" | bash
