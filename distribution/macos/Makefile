MAKEFLAGS += --warn-undefined-variables

SHELL := bash

.DEFAULT_GOAL := CellProfiler.dmg

.DELETE_ON_ERROR:

.SHELLFLAGS := -eu -o pipefail -c

.SUFFIXES:

#identity = "Developer ID Application: Allen Goodman (MERWFR65Q3)"

CellProfiler:
	git clone https://github.com/glencoesoftware/CellProfiler $@

	cd $@ && git checkout compat-3-0

.PHONY: dependencies
dependencies: CellProfiler
	pip install --no-cache-dir --upgrade cython
	pip install --no-cache-dir --upgrade numpy==1.13.1
	pip install --no-cache-dir --upgrade scipy==1.0.1
	pip install --no-cache-dir --upgrade centrosome==1.0.9
	pip install --no-cache-dir --upgrade javabridge==1.0.14

	git clone git@github.com:emilroz/python-javabridge.git
	cd python-javabridge && git checkout tags/1.0.14 -b 1.0.14-build && python setup.py bdist_wheel
	cd python-javabridge/dist && pip install --no-cache-dir javabridge*

	pip install --editable "CellProfiler[build, test]" --upgrade

dist/CellProfiler.app: CellProfiler dependencies Info.plist
	pyinstaller --noconfirm --log-level=DEBUG --windowed --clean -F CellProfiler.spec

	cp $(word 3, $^) $@/Contents

	# codesign --deep -s $(identity) $@

	# xattr -lr $@
	# xattr -cr $@

CellProfiler.dmg: dist/CellProfiler.app
	hdiutil create                  		\
		-format UDRW                		\
		-fs HFS+                    		\
		-fsargs "-c c=64,a=16,e=16" 		\
		-size 450000k               		\
		-srcfolder dist/CellProfiler.app 	\
		-volname CellProfiler      			\
		CellProfiler.dmg

	#codesign --force --verify --verbose --deep -s $(identity) $@

.PHONY: clean
clean:
	if [ -d build ]; then rm -rf build; fi
	
	if [ -d dist ]; then rm -rf build; fi

	if [ CellProfiler.dmg ]; then rm -rf CellProfiler.dmg; fi

	if [ -d python-javabridge ]; then rm -rf python-javabridge; fi
