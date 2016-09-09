"""
Base utilities to build API operation managers and objects on top of.
"""

import abc
import contextlib
import copy
import hashlib
import inspect
import os
import threading

from oslo_utils import strutils
from requests import Response
import six

from harborclient import exceptions
from harborclient import utils


class Manager(object):
    """Manager for API service.

    Managers interact with a particular type of API (projects, users, reposiries,
    etc.) and provide CRUD operations for them.
    """

    def __init__(self, api):
        self.api = api

    @property
    def client(self):
        return self.api.client

    @property
    def api_version(self):
        return self.api.api_version

    def _list(self, url, body=None):
        if body:
            resp, body = self.api.client.post(url, body=body)
        else:
            resp, body = self.api.client.get(url)
        return resp, body

    def _get(self, url):
        return self.api.client.get(url)

    def _create(self, url, body, **kwargs):
        return self.api.client.post(url, body=body)

    def _delete(self, url):
        return self.api.client.delete(url)

    def _update(self, url, body, **kwargs):
        return self.api.client.put(url, body=body)
