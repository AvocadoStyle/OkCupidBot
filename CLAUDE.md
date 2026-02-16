# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OkCupid automation bot using Selenium WebDriver. Automates liking profiles and sending messages on OkCupid. Built by Eden Refaelov.

## Commands

```bash
# Install dependencies
make install          # or: poetry install

# Run the bot
make run              # or: poetry run python main.py

# Testing & code quality
make test             # or: poetry run pytest
make format           # or: poetry run black .
make lint             # or: poetry run flake8

# Environment
make shell            # Open Poetry shell
make clean            # Remove virtual environment
```

## Architecture

MVC-like pattern with Selenium automation. Entry point is `main.py`.

### Core Components

- **`main.py`** — Loads `.env` credentials, initializes the orchestrator, runs the message loop
- **`controller/classTool.py`** — `OkCupidSelenium` is the central orchestrator that composes all action handlers (BrowserDriver, BrowserAction, User, Like, Message)
- **`model/driver/browser_driver.py`** — `BrowserDriver` wraps Selenium Chrome WebDriver setup using `webdriver-manager` for automatic chromedriver resolution
- **`model/action/operation_action.py`** — `OperationAction` abstract base class for all action handlers
- **`model/action/browser_action.py`** — `BrowserAction` handles navigation between OkCupid sections (discover, likes)
- **`model/action/like_action.py`** — `Like` handles liking/disliking profiles with popup management
- **`model/action/message_action.py`** — `Message` handles the full message workflow: navigate to likes, click profile (4x4 grid), open message box, input text, send
- **`model/user/credentials.py`** — `User` credential holder
- **`model/Utilities/operation_utils.py`** — `sleep_decorator` adds configurable pre/post delays to methods
- **`data/navigation.yml`** — XPath definitions for OkCupid UI elements

### Key Patterns

- **Composition**: `OkCupidSelenium` owns all action handlers
- **Inheritance**: `Like` and `Message` extend `OperationAction`
- **Decorator**: `@sleep_decorator` wraps methods with timing delays
- **Selenium waits**: Uses `WebDriverWait` (up to 50s) rather than raw `time.sleep()` for element location

## Configuration

Credentials and Chrome profile path are loaded from `.env` via `python-dotenv`:
```
USER_NAME=...
PASSWORD=...
USER_CACHE_DATA=...   # Optional Chrome user profile cache path
```

## Dependencies

Python ^3.9 managed with Poetry. Key runtime deps: `selenium==4.2.0`, `python-dotenv`, `webdriver-manager`.

## Important Notes

- XPaths are hardcoded throughout action classes — these break when OkCupid changes its UI
- The message action uses row/column grid navigation (max 4x4) to select profiles
- Chrome window size is fixed at 1900x1024 in `BrowserDriver`
- The bot supports Hebrew text input for messages
