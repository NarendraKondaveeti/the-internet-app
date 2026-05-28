# Python Playwright Automation Framework

This repository is an educational, interview-ready automation framework for [The Internet](https://the-internet.herokuapp.com/). It uses Python, Playwright, Pytest, Page Object Model, HTML reporting, logs, screenshots, traces, videos, retries, configurable environments, parallel execution, API support, Azure DevOps, and GitHub Actions.

## Application Coverage

The site exposes many small modules. This framework includes direct tests for login, checkboxes, dropdowns, tables, alerts, frames, child windows, upload, download, inputs, status-code navigation, and API health. The structure is ready to extend for the remaining public pages such as add/remove elements, basic auth, broken images, challenging DOM, context menu, digest auth, disappearing elements, drag and drop, dynamic content, dynamic loading, entry ad, exit intent, floating menu, forgot password, hovers, infinite scroll, key presses, large DOM, multiple windows, notification messages, redirect links, secure file download, shadow DOM, sliders, sortable tables, typos, and WYSIWYG editor.

Note: the site does not provide a true global search box or business filters. `test_search.py` and `test_filters.py` are included as educational placeholders mapped to the closest available dynamic/search-like and filter/navigation behaviors.

## Folder Structure

```text
project_root/
├── api/                 # API client classes
├── config/              # environment YAML files
├── fixtures/            # optional future reusable fixture data
├── locators/            # locator constants by module
├── logs/                # execution logs
├── pages/               # Page Object Model classes
├── reports/             # pytest-html reports
├── screenshots/         # failure screenshots
├── testdata/            # JSON and upload test data
├── tests/               # feature based pytest files
├── traces/              # Playwright trace zip files
├── utils/               # config, logger, waits, assertions, data readers
├── videos/              # Playwright videos
├── .github/workflows/   # GitHub Actions workflow
├── azure-pipelines.yml  # Azure DevOps pipeline
├── conftest.py          # pytest fixtures and hooks
├── pytest.ini           # pytest configuration
└── requirements.txt     # Python dependencies
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
```

## Execution Commands

Run all tests:

```powershell
pytest
```

Run smoke tests:

```powershell
pytest -m smoke
```

Run regression tests:

```powershell
pytest -m regression
```

Run headed mode for learning visibility:

```powershell
pytest --headed-mode --slow-mo 300
```

Run tests in parallel:

```powershell
pytest -n auto
```

Run against a specific environment:

```powershell
pytest --env qa
```

Generate HTML report:

```powershell
pytest --html=reports/report.html --self-contained-html
```

## Reports and Debugging

After execution, check:

- `reports/report.html` for the HTML report
- `logs/execution.log` for readable execution logs
- `screenshots/` for failure screenshots
- `traces/` for Playwright trace files
- `videos/` for video recordings

Open a trace:

```powershell
python -m playwright show-trace traces\<trace-file>.zip
```

## Framework Flow

1. `pytest` starts execution using `pytest.ini`.
2. `conftest.py` loads `config/environments.yaml`.
3. Browser and context fixtures create isolated Playwright sessions.
4. Test files call page object methods from `pages/`.
5. Page objects use Playwright locators and reusable helpers.
6. Failures trigger screenshot and trace capture.
7. HTML report, logs, screenshots, traces, and videos are stored locally or published in CI.

## Locator Strategy

Preferred locator order:

1. Playwright built-in locators: `get_by_role`, `get_by_text`, `get_by_label`, `get_by_placeholder`
2. CSS selectors when semantic locators are not available
3. XPath only when unavoidable

Each page object contains Telugu-English beginner comments explaining why a locator was selected.

## CI/CD

Azure DevOps uses `azure-pipelines.yml` with install and test stages. GitHub Actions uses `.github/workflows/playwright-python.yml` for push, pull request, and manual runs.

Typical GitHub setup:

```powershell
git init
git add .
git commit -m "Add Python Playwright automation framework"
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
```

## Troubleshooting

- Browser not found: run `python -m playwright install chromium`.
- Import error: confirm virtual environment is activated and `pip install -r requirements.txt` completed.
- Slow execution: remove `--headed-mode` or reduce `--slow-mo`.
- CI browser dependency issue: use `python -m playwright install --with-deps chromium` in Linux pipelines.
- Flaky UI: use Playwright auto-wait first, then add targeted explicit waits in `utils/wait_utils.py`.
