#!/bin/sh

pytest -s -v

flake8 src/
