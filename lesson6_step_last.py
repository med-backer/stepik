import time
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_items(browser):
    browser.get(link)
    time.sleep(15)
    print('Спим 15 секунд')
    btns=browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(btns) > 0,'not find basket'
    
