from selenium import webdriver

url = 'https://www.youtube.com/c/KalleHallden/videos'
driver = webdriver.Chrome('/home/Avimanyu/git/My-Python-Garbage/chromedriver')
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="video-title"]').click()
