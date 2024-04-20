from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step('Click "Skip" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Search "Python" articles'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))


def test_open_first_article():
    with step('Click "Skip" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Search "Python" articles.'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')

    with step('Click the first article.'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

    with step('Verify content found.'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Python'))


def test_getting_started():
    with step('Verify welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('The Free '
                                                                                                  'Encyclopedia\n…in '
                                                                                                  'over 300 languages'))

        with step('Click "Continue" button'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with step('Verify second welcome screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('New ways to '
                                                                                                      'explore'))

        with step('Click "Continue" button'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with step('Verify third welcome screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Reading lists '
                                                                                                      'with sync'))
        with step('Click "Continue" button'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with step('Verify fourth welcome screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))
