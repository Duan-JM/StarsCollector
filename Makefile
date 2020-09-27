.PHONY: build
build:
	pip3 install -r requirements.txt

.PHONY: uninstall
uninstall:
	pip3 uninstall stars_collecter

.PHONY: install
install:
	python3 setup.py install

.PHONY: clean
clean:
	rm -rf *.egg-info
	rm -rf build dist
