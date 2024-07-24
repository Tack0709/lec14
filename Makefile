
.PHONY: clean test coverage

test:
	python -m unittest testRecurusive.py

coverage:
	coverage run testRecurusive.py
	coverage report
	coverage html
	coverage xml

clean:
	rm -rf *.pyc __pycache__/
	rm -rf htmlcov/ coverage.xml .coverage
