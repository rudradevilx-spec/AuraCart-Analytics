class ProxyManager:

    def __init__(self):

        self.proxies = []

    def add_proxy(self, proxy):

        if proxy not in self.proxies:

            self.proxies.append(proxy)

    def get_proxy(self):

        if not self.proxies:

            return None

        return self.proxies[0]

    def get_requests_proxy(self):

        proxy = self.get_proxy()

        if proxy is None:

            return None

        return {
            "http": proxy,
            "https": proxy
        }