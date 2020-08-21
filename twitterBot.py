from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like(self, tag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+tag+'&src=typeahead_click')
        time.sleep(3)
        for range in (1, 5):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('tweet')
            print(tweets)
            # # like = [bot.find_element_by_class_name(
            # #     'r-4qtqp9') for elem in tweets]
            # try:
            #     bot.get_attrubutr('svg').click()
            #     time.sleep(5)
            # except Exception as ex:
            #     time.sleep(50)


vikas = TwitterBot('username', 'password')
vikas.login()
vikas.like('developer')
