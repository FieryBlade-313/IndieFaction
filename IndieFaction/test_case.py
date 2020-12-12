import pytest
import requests


def test_index():
    r = requests.get('http://localhost:8000')
    assert r.status_code == 200


def test_failure():
    r = requests.get('http://localhost:8000/not_existing')
    assert r.status_code == 404


def test_fail():
    r = requests.get('http://localhost:8000/random')
    assert r.status_code == 404
