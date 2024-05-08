import pytest
from wikipedia_app.android_pages.main_page import main_page


@pytest.mark.parametrize("mobile_management", ["android"], indirect=True)
def test_wikipedia_search(mobile_management):
    main_page.search("Appium")
    main_page.should_have_search_results("Appium")


@pytest.mark.parametrize("mobile_management", ["android"], indirect=True)
def test_wikipedia_open_article(mobile_management):
    main_page.search("Webdriver")
    main_page.open_search_result()
