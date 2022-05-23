
class Cookie:

    def __init__(self,driver):
            self.driver = driver


    def cookiesCapture(self):
        cookie_names_captured = []
        cookies = self.driver.get_cookies()
        print(len(cookies))
        print("cookies list :- \n", cookies)
        print(cookies)
        for i in cookies:
            cookie_names_captured.append(i['name'])

