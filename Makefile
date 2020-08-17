
EXT_NAME:=ulauncher-cheats
EXT_DIR:=$(shell pwd)

lint:
	@find . -iname "*.py" | xargs pylint

format:
	@autopep8 --in-place --recursive --aggressive .

link:
	@ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

unlink:
	@rm -r ~/.local/share/ulauncher/extensions/${EXT_NAME}
