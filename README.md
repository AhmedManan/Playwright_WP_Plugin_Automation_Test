# WordPress Ecommerce Website Automation Test
In this repository contains an automation test suite built with Playwright, Python & Pytest. I implement the Page Object Model (POM) design pattern. The test suite covers various plugin test in a WordPress ecommerce (WooCommerce) environment.

## Table Of Content
- [View Live Report](#-view-live-report)
- [Project Setup](#-project-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Environment](#setting-up-environment)
  - [Performing Tests](#performing-tests)
  - [Report Generation](#report-generation)
- [Tests](#tests)
- [Additional Topics](#additional-topics)
  - [Playwright Javascript WordPress Plugin Test](#playwright-javascript-wordpress-plugin-test)
  - [Similar Topics & Articles](#similar-topics--articles)

## 🔎 View Live Report
Check the test report live:
- Allure Report: [View Allure Report]()
- HTML Report: [View HTML Self Contained Report]()


### Setting Up Environment
A .env file is a plain text file used to store environment variables for an application,
especially during local development or testing. It follows a simple key-value format, making
it easy to manage configuration settings. To setup the project you need to create a .env file
using the .env.example file provided in the project repository.
```bash
BASE_URL= Website Base URL
ADMIN_USERNAME= Admin Username
ADMIN_PASSWORD= Admin Password
```   
### Performing Tests
 The simplest way to run your tests is to call the pytest command with no arguments:

 ```bash
 pytest
``` 
 You can specify a file path or directory path after the pytest command. Example:
 ```bash
 pytest tests/test_cases/test_login.py
``` 
### Report Generation
 HTML reports are excellent for visually reviewing test results. The most popular plugin for this is pytest-html. First, install the plugin from terminal:
 ```bash
 pip install pytest-html
```
Generating an Allure Report provides a rich, interactive, and visually appealing summary of your test execution results. Here is how to set up and generate an Allure Report, specifically using Pytest (Python) as the example framework.
First, install it from terminal:
 ```bash
 pip install allure-pytest
```
Use the allure generate command to process the raw results into an HTML report structure.
 ```bash
 pytest--alluredir=reports/allure-results
```
Use the allure generate command to process the raw results into an HTML report structure.
 ```bash
 allure generate reports/allure-results-o reports/allure-report
```
The easiest way to view the report locally is to use the allure serve command, which starts a local web server and opens the report in your default browser.
 ```bash
allure serve reports/allure-results
```
## ✔️ Tests
### Part A: WordPress Functionality

| Test Case | Description | Status |
|-----------|-------------|--------|
| 01        | Verify WordPress Login Functionality | ✔️ |

### Part B: WooCommerce Plugin

| Scenario | Description | Status |
|----------|-------------|--------|
| 01       | End-to-End Checkout Flow | ✔️ |
| 02       | User Account Order History | ✔️ |

### Part C: Ninja Tables – Easy Data Table Builder

| Task | Description              | Status |
|------|--------------------------|--------|
| 01   | Plugin Installation Test | ✔️ |
| 02   | Plugin Activation Test   | ✔️ |

### Bonus 

| Task | Description                       | Status |
|------|-----------------------------------|--------|
| 01   | Run the test suite from GitAction | ✔️ |

## Additional Topics

### Playwright Javascript WordPress Plugin Test
In this bellow mentioned project/repository, it contains an automation test suite built with Playwright & JavaScript to test WordPress & WordPress Plugins. I implement the Page Object Model (POM) design pattern.

 **Project Link:** [JS_Playwright_WP_Plugin_Test](https://github.com/AhmedManan/JS_Playwright_WP_Plugin_Test)

### Similar Topics & Articles

[Python Complete Cheat Sheet](https://mananacademy.com/complete-python-cheat-sheet/)

[Complete JavaScript Cheat sheet](https://mananacademy.com/complete-javascript-cheat-sheet/)

[⬆️Back to Top](#qa-wppool-assignment)