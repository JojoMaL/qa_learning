[![QA tests](https://github.com/JojoMaL/qa_learning/actions/workflows/main.yml/badge.svg)](https://github.com/JojoMaL/qa_learning/actions/workflows/main.yml)

# QA Learning

A personal study project for learning **test automation** with Python. It combines UI tests built with **Playwright** and API tests, all run with **pytest**.

## Tech stack

- Python 3
- [pytest](https://docs.pytest.org/) as the test runner
- [Playwright](https://playwright.dev/python/) (via `pytest-playwright`) for browser automation
- Chromium as the default browser

## Project structure

```
qa_learning/
├── pages/          # Page objects (UI locators and actions)
├── tests/          # Test cases
├── pytest.ini      # pytest configuration and custom markers
└── login_error.png # Example failure screenshot from a login test
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/JojoMaL/qa_learning.git
cd qa_learning
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```


## Running the tests

`pytest.ini` already sets `-v --browser=chromium`, so this is enough to run everything:

```bash
pytest
```

Run only a group of tests using markers:

```bash
pytest -m smoke        # critical, fast tests
pytest -m login        # login-related tests
pytest -m users        # user-related tests
pytest -m api          # API tests
pytest -m playwright   # Playwright UI tests
```

Other useful options:

```bash
pytest --headed                  # watch the browser while tests run
pytest --junitxml=report.xml     # generate a JUnit XML report
pytest tests/test_file.py        # run a single file
```

## Test markers

| Marker | Description |
|--------------|------------------------------|
| `users` | Tests related to users |
| `login` | Tests related to login |
| `playwright` | Tests related to Playwright |
| `api` | Tests related to API |
| `smoke` | Critical, fast tests |

## Reports and screenshots

- `report.xml` is a JUnit-style test report that CI tools can read.
- `login_error.png` is a screenshot captured when a login test failed, useful for debugging.

## What I'm learning

- Writing UI tests with Playwright
- Organizing tests with the Page Object pattern
- Testing APIs with pytest
- Grouping and filtering tests with markers
- Generating test reports and capturing failure evidence

## Author

**JojoMaL** · [GitHub profile](https://github.com/JojoMaL)
