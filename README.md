# Playwright Enhanced Automation Framework

## Quick start (local)
1. python -m venv .venv
2. source .venv/bin/activate   # Windows: .venv\Scripts\activate
3. pip install -r requirements.txt
4. playwright install
5. cp .env.example .env        # edit if needed

## Run tests
pytest -m api --alluredir=allure-results
pytest -m ui --alluredir=allure-results
pytest --alluredir=allure-results

## View Allure report (if allure CLI installed)
allure generate allure-results --clean -o allure-report
allure open allure-report
allure serve allure-results (generate and serve the report)
