from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure import step


class WikipediaMainPage:

    @staticmethod
    def search(text: str):
        with step(f"Search for {text} on the main page"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(text)

    @staticmethod
    def should_have_search_results(text: str):
        with step(f"Checking that there are more than 0 search results and the first has {text} text"):
            results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))

    @staticmethod
    def open_search_result():
        with step("Clicking on the first search result"):
            browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).first.click()


main_page = WikipediaMainPage()
