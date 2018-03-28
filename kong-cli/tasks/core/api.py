from tasks.config import config


class ApiCallTask(object):
    def __init__(self, name, doc, endpoint, endpoint_params, requests_method):
        self.__name__ = name
        self.__doc__ = doc
        self._endpoint = endpoint
        self._method = requests_method
        self._endpoint_params = endpoint_params

    @property
    def full_api_url(self):
        return config.kong_admin_url + self._endpoint

    def __call__(self, *args, **kwargs):
        invoke_ctx, options = args[0], args[1:]

        options = ('', ) if not options else options
        api_url = self.full_api_url.format(*options)

        # send request to api
        response = self._method(api_url, data=kwargs)
        print(response.content.decode())
