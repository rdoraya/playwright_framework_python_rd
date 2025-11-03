FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install firefox --with-deps

CMD ["pytest", "-v", "--alluredir=allure-results"]
