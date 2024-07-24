
.PHONY: clean test coverage

test:
	python -m unittest test_compute.py

coverage:
	coverage run test_compute.py
	coverage report
	coverage html
	coverage xml

clean:
	rm -rf *.pyc __pycache__/
	rm -rf htmlcov/ coverage.xml .coverage

