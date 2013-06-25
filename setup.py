#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012-2013 Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup

from httpstream import (__author__, __email__, __license__, __package__,
                        __version__)


setup(
    name=__package__,
    version=__version__,
    description="Stream based HTTP client",
    long_description="HTTPStream is a HTTP client library for Python which is "
                     "designed around iterable, streaming content that can "
                     "be consumed as it is received. It uses jsonstream to "
                     "allow large JSON documents to be decoded incrementally.",
    author=__author__,
    author_email=__email__,
    url="https://github.com/nigelsmall/httpstream",
    packages=[
        "httpstream",
    ],
    install_requires=[
        "distribute",
        "jsonstream",
    ],
    license=__license__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
    ],
)
