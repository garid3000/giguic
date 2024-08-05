pull_sub_module:
	git submodule update --init --recursive


convert_pyside6:
	find UI -name "*.ui" | cut -d/ -f2 | cut -d. -f1 | xargs -I {} pyside6-uic "UI/{}.ui" -o "Custom_UIs/{}.py"

convert_pyqt6: 
	find UI -name "*.ui" | cut -d/ -f2 | cut -d. -f1 | xargs -I {} pyuic6 "UI/{}.ui" -o "Custom_UIs/{}.py"

convert_fix:
	find Custom_UIs -name "*.py" | xargs -I {} misc/Fix-pyside-conversion-types.sh {}

convert_black:
	find Custom_UIs -name "*.py" | xargs -I {} black {}

convert_removal_imports:
	find Custom_UIs -name "*.py" | xargs -I {} autoflake --in-place --remove-all-unused-imports {}

convert_all:
	make clean_convert
	make convert_pyside6
	make convert_fix
	make convert_black
	make convert_removal_imports


convert_all_from_pyqt6:
	make clean_convert
	make convert_pyqt6
	make convert_fix
	find Custom_UIs -name "*.py" | xargs -I {} misc/Fix-pyqt2pyside-conversion-types.sh {}
	make convert_black
	make convert_removal_imports

clean_convert:
	find Custom_UIs ! -name '__init__.py' -type f -exec rm -f {} +

release:
	pyinstaller -F main.py


run:
	python3 main.py

run_from_nix:
	nixGL python3 main.py
