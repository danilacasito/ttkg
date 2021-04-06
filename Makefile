main: main.py /usr/local/bin/pyinstaller
	pyinstaller --onefile main.py
	mkdir binary
	cd binary && mkdir bin
	cp dist/main binary/bin/ttkg
install: binary/bin/ttkg
	mkdir /usr/apps
	mkdir /usr/apps/ttkg
	mkdir /usr/apps/ttkg/bin
	install -m 755 binary/bin/ttkg /usr/apps/ttkg/bin
	ln -sf /usr/apps/ttkg/bin/ttkg /usr/bin/ttkg
uninstall:
	rm -rf /usr/apps/ttkg
	rm -rf /usr/bin/ttkg
clean:
	rm -rf build
	rm -rf dist
	rm -rf main.spec
	rm -rf __pycache__
	rm -rf binary
readme: README.md
	vim README.md
