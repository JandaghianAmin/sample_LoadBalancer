import pytest
from unittest import mock
from lb import LoadBalancer

def test_add_and_remove_server():
    l=LoadBalancer()
    l.add_server('server 1')
    l.add_server('server 2')
    l.add_server('server 3')
    assert l.Servers==['server 1','server 2','server 3']
    l.remove_server('server 2')
    assert l.Servers==['server 1','server 3']

def test_get_random_server():
    l=LoadBalancer()
    l.add_server('server 1')
    l.add_server('server 2')
    l.add_server('server 3')
    with mock.patch('random.choice', return_value='server 2'):
        choise = l.get_random_server()
        assert choise == 'server 2'

def test_get_round_robin():
    l=LoadBalancer()
    l.add_server('server 1')
    l.add_server('server 2')
    l.add_server('server 3')
    assert l.get_round_robin_server()=='server 1'
    assert l.get_round_robin_server()=='server 2'
    assert l.get_round_robin_server()=='server 3'
    assert l.get_round_robin_server()=='server 1'

def test_invalid_startgy():
    l=LoadBalancer()
    with pytest.raises(ValueError):
        l.get_next_server(strategy="invalid")
    
