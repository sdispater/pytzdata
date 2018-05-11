RELEASE := $$(sed -n -E "s/^VERSION = '(.+)'/\1/p" pytzdata/version.py)

list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

release:
	@poetry build

publish:
	@poetry publish --no-build

# test your application (tests in the tests/ directory)
test:
	@poetry run pytest tests/ -sq

# run tests against all supported python versions
tox:
	@tox

# Build tzdata
data:
	@python -m pytzdata.commands.app make
	@autopep8 pytzdata/_timezones.py -i

# Dump timezones
zones:
	@python -m pytzdata.commands.app zones:dump
	@autopep8 pytzdata/_timezones.py -i
