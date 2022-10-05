__author__ = 'kamta'

import json

import pytest


def test_home_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200


def test_generate_sequence_fixture(test_client):
    """
    """
    test_data = [5, 16, 8, 4, 2, 1]
    response = test_client.get('sequence/elem/5')
    data = json.loads(response.data.decode())
    assert type(data) == list
    assert data == test_data
    assert response.status_code == 200


def test_generate_sequence_longest_fixture(test_client):
    """
    """
    test_data = {"response": 3, "maxlength": 8}
    response = test_client.get('sequence/longest/5')
    data = json.loads(response.data.decode())
    assert type(data) == dict
    assert data == test_data
    assert response.status_code == 200


def test_generate_iris_describe_fixture(test_client):
    """
    """
    test_data = {
        "counts": {
            "sepal_length": 150,
            "sepal_width": 150,
            "petal_length": 150,
            "petal_width": 150,
            "species": 150
        },
        "maxvals": {
            "sepal_length": 7.9,
            "sepal_width": 4.4,
            "petal_length": 6.9,
            "petal_width": 2.5,
            "species": "virginica"
        },
        "minvals": {
            "sepal_length": 4.3,
            "sepal_width": 2,
            "petal_length": 1,
            "petal_width": 0.1,
            "species": "setosa"
        },
        "meanval": {
            "sepal_length": 5.843333333333334,
            "sepal_width": 3.0573333333333337,
            "petal_length": 3.7580000000000005,
            "petal_width": 1.1993333333333336
        },
        "message": "Iris detailed stats"
    }
    response = test_client.get('iris/describe')
    data = json.loads(response.data.decode())
    assert type(data) == dict
    assert data == test_data
    assert response.status_code == 200


def test_generate_iris_group_fixture(test_client):
    """
    """
    test_data = {
        "species_count at length 5": {
            "setosa": 28,
            "versicolor": 3,
            "virginica": 1
        }
    }
    response = test_client.get('irisgroup/sepal_length/5')
    data = json.loads(response.data.decode())
    assert type(data) == dict
    assert data == test_data
    assert response.status_code == 200
