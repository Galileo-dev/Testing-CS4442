#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# run firebase emulator
firebase emulators:start --only auth,firestore

# run pytest
pytest

