.PHONY: help install update run clean shell test format lint

help:
	@echo "OkCupidBot - Available Commands (Poetry):"
	@echo ""
	@echo "  make install     - Install all dependencies with Poetry (first time setup)"
	@echo "  make update      - Update dependencies to latest versions"
	@echo "  make run         - Run the bot"
	@echo "  make shell       - Open Poetry shell (activated virtual environment)"
	@echo "  make test        - Run tests with pytest"
	@echo "  make format      - Format code with black"
	@echo "  make lint        - Lint code with flake8"
	@echo "  make clean       - Remove virtual environment and cache"
	@echo "  make help        - Show this help message"
	@echo ""
	@echo "Note: Make sure Poetry is installed: https://python-poetry.org/docs/#installation"
	@echo ""

install:
	@echo "Installing dependencies with Poetry..."
	poetry install
	@echo ""
	@echo "Setup complete! Run 'make run' to start the bot."

update:
	@echo "Updating dependencies..."
	poetry update

run:
	@echo "Starting OkCupidBot..."
	poetry run python main.py

shell:
	@echo "Opening Poetry shell..."
	poetry shell

test:
	@echo "Running tests..."
	poetry run pytest

format:
	@echo "Formatting code with black..."
	poetry run black .

lint:
	@echo "Linting code with flake8..."
	poetry run flake8 .

clean:
	@echo "Removing virtual environment and cache..."
	poetry env remove --all
	@echo "Clean complete!"
