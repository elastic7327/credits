#!/bin/sh

pytest -s -v src/tests/test_luhn.py
pytest -s -v src/tests/test_models.py
pytest -s -v src/tests/test_securitys.py

# pylint src/

# flake8 --filename=*.py src/
# flake8 --filename=*.py src/
