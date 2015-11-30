from __future__ import print_function

import json
import unittest
import os
from os import path
from fnmatch import fnmatch

import pyld
from jsonschema import validate

root_path = path.join(path.dirname(path.realpath(__file__)), '..')
schema_path = path.join(root_path, 'schema.json')
examples_path = path.join(root_path, 'examples')

with open(schema_path) as f:
    me_schema = json.load(f)

def validate_json(js):
    validate(js, me_schema)
    print("Ok")

def check_case(filename):
    print(filename)
    with open(filename) as f:
        validate_json(json.load(f))

def test_generator(folder=examples_path):
    for dirpath, dirnames, filenames in os.walk(folder):
        for i in filenames:
            if fnmatch(i, '*.json'):
                filename = path.join(dirpath, i)
                yield check_case, filename
                        

if __name__ == '__main__':
    unittest.main()
