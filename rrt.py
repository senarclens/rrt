#!/usr/bin/env python3

"""
Small script showing how REST APIs can automatically be tested for regressions.

This is just a small POC. It shows any change as failure, does not support
authentication and is limited to GET requests.

Adjust the variables OLD and NEW to two different versions of your API.
"""

from collections import namedtuple
import unittest

import requests

OLD = "http://localhost:3000"
NEW = "http://localhost:3001"



Request = namedtuple('Request', ('id', 'method', 'endpoint', 'payload'))


class RRT(unittest.TestCase):
    """
    Automatic regression tests for REST APIs.

    The actual test cases are injected.
    """
    def setUp(self):
        self._session = requests.Session()
        self._headers = {'Content-Type': 'application/json'}
        #self._session.auth = requests.auth.HTTPBasicAuth(username, password)


def test_generator(request):
    def test(self):
        r_v1 = getattr(self._session,
                       request.method.lower())(OLD + request.endpoint)
        v1 = r_v1.json()
        r_v2 = getattr(self._session,
                       request.method.lower())(NEW + request.endpoint)
        v2 = r_v2.json()
        self.assertEqual(v1, v2,
                         '\nrequest {} failed ({})'.format(request.id,
                                                           request.endpoint))
    return test


if __name__ == "__main__":
    with open('requests.csv') as f:
        next(f)
        requests_ = [Request(*l.split(',')) for l in f.readlines()]
    for request in requests_:
        name = 'test_%s' % request.id
        test = test_generator(request)
        setattr(RRT, name, test)
    unittest.main()

