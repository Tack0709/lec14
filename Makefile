
.PHONY: clean test coverage

test:
	python -m unittest testRecursive.py

coverage:
	coverage run testRecursive.py
	coverage report
	coverage html
	coverage xml

clean:
	rm -rf *.pyc __pycache__/
	rm -rf htmlcov/ coverage.xml .coverage
