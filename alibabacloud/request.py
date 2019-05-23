# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class APIRequest:

    def __init__(self, action_name, method, scheme, style, param_position="query"):
        self.action_name = action_name
        self.scheme = scheme  # http|https,TODO 所有protocol改为scheme
        self.method = method
        self.style = style
        self._param_position = param_position
        self._params = {}
        self.uri_pattern = ''
        self.path_params = {}

        # 以下参数仅兼容Common Request
        self._headers = {}
        self._body_params = {}
        self._query_params = {}
        self._content = None

    def _load_from_legacy_request(self, request):
        # request:acsrequest

        # FIXME：content
        self._content = request._content

        self._body_params = request._body_params
        self._query_params = request._params

        if self.style == 'ROA':
            self.uri_pattern = request._uri_pattern
            self.path_params = request._path_params
        return self

    @property
    def params(self):
        return self._params


class APIResponse:
    pass


class HTTPRequest:

    def __init__(self, accept_format=None, method=None, scheme=None, proxy=None,
                 signature=None, port=None,
                 headers=None, url=None, endpoint=None, timeout=None,
                 body="", retries=0, credentials=None):
        self.accept_format = accept_format
        self.body = body
        self.method = method
        self.scheme = scheme
        self.proxy = proxy
        self.port = port
        self.headers = headers
        self.url = url
        self.timeout = timeout
        self.signature = signature
        self.endpoint = endpoint
        self.retries = retries
        self.credentials = credentials


class HTTPResponse:

    def __init__(self, status_code=None, headers=None, content=None):
        self.status_code = status_code
        self.headers = headers
        self.content = content
