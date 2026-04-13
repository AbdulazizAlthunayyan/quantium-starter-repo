#!/bin/bash

if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found."
    exit 1
fi

python -m pytest test_app.py

if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi