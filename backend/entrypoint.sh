#!/bin/bash
set -e  # Exit on error

echo "Running tests..."
python -m unittest discover -s tests -vvv

echo "Tests passed! Starting the app..."
exec python run.py 
