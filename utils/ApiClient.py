class ApiClient:
    @staticmethod
    def api_url():
        return "https://petstore.swagger.io"

    @staticmethod
    def headers():
        headers =\
            {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }
        return headers
