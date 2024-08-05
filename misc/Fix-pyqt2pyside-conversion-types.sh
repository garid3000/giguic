#!/bin/sh
# sed -i 's///g' "$1"

sed -i 's/from PyQt6/from PySide6/g' "$1"
sed -i 's/import PyQt6/import PySide6/g' "$1"

