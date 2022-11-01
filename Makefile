cur_dir   := $(shell basename $(CURDIR))
mount_dir := $(PWD)

# Targets for local development
init::    git_reset
shell::   pipenv shell
install:: ci_install 
fmt::     ci_fmt
lint::    fmt ci_lint
test::    fmt ci_lint ci_test

.SILENT: git_reset

# Targets for CI
ci_fmt::
	pipenv run black panther_content tests

ci_lint::
	pipenv run mypy --config-file mypy.ini panther_content tests

ci_test::
	pipenv run nosetests -v --with-coverage --cover-package=panther_content

ci_install:
	pipenv install --dev

docker_shell:
	docker run --rm -it -v "$(mount_dir):/$(cur_dir)" --workdir "/$(cur_dir)" python:3.9 /bin/bash

# Other targets
git_reset:
	printf "%s " "This will reset the repository git history. Press ENTER to continue"
	read ans
	rm -rf .git
	rm .github/CODEOWNERS
	git init
	echo "done!"