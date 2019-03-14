from page.base_page import BasePage


def test_by_attr():
    exp1 = BasePage.by_attr(text='test_text')
    assert exp1 == '//*[@text="test_text"]'
    exp2 = BasePage.by_attr(text='test_text', ele_id='test_id')
    assert exp2 == '//*[@text="test_text" and contains(@resource-id, "test_id")]'
