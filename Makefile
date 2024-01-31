install:
	@poetry install
format:
	@isort .
	@blue .
lint:
	@blue . --check
	@isort . --check
	@prospect --with-tool pep257 --doc-warning
test:
	@pytest -v
sec:
	@pip-audit
