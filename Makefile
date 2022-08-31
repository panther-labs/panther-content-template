# Targets for local development
install:: utl_activate ci_install
fmt::     install ci_fmt
lint::    fmt ci_lint
test::    fmt ci_lint ci_test

# Targets for CI
ci_install::
	pip3 install -qr requirements.txt

ci_fmt::
	black panther_content tests

ci_lint::
	mypy --config-file mypy.ini panther_content tests

ci_test::
	nosetests -v --with-coverage --cover-package=panther_content

# Utility targets
venv:
	python3 -m venv venv

utl_activate: venv
	. venv/bin/activate
