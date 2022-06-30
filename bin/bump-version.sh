#!/usr/bin/env bash

current=$(poetry version -s)
poetry version ${1:-patch}
new=$(poetry version -s)

sed -i -e "s/\"${current}\"/\"${new}\"/" src/boilerplate/__init__.py
