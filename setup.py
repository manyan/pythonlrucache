import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "LRUCache_with_TTL_project",
    version = "0.1.0",
    author = "Manyan Chen",
    author_email = "xxmajia@gmail.com",
    description = ("Simple Composite pattern to wrap more feature into pylru cache"),
    license = "xxmajia",
    keywords = "lru ttl",
    url = "https://github.com/manyan/leetcode/pythonlrucache",
    packages=['lru'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: BETA",
        "Topic :: Utilities",
    ],
)