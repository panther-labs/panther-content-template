cur_dir   := $(shell basename $(CURDIR))
mount_dir := $(PWD)

# Targets for local development
init::    git_reset
shell::   docker_shell
install:: utl_activate ci_install
fmt::     ci_fmt
lint::    fmt ci_lint
test::    fmt ci_lint ci_test
clean::   venv_rm

# Targets for CI
ci_install::
	python -m pip install --upgrade pip
	pip3 install -qr requirements.txt

ci_fmt::
	black panther_content tests

ci_lint::
	mypy --config-file mypy.ini panther_content tests

ci_test::
	nosetests -v --with-coverage --cover-package=panther_content

# Other targets
venv:
	python3.9 -m venv venv

utl_activate: venv
	. venv/bin/activate

venv_rm:
	rm -rf venv

docker_shell:
	docker run --rm -it -v "$(mount_dir):/$(cur_dir)" --workdir "/$(cur_dir)" python:3.9 /bin/bash

git_reset:
	rm -rf .git
	rm .github/CODEOWNERS
	git init