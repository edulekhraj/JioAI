import os
import shutil

import allure
import pytest
from selenium import webdriver
from pages.base_test import BaseTest
from utils.config_reader import get_base_url


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(get_base_url())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def base(driver):
    return BaseTest(driver)


def pytest_sessionstart(session):
    if os.path.exists("reports/allure-results"):
        shutil.rmtree("reports/allure-results")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs['driver']

        screenshot = driver.get_screenshot_as_png()

        allure.attach(
            screenshot,
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
