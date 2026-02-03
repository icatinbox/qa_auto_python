def test_requests_import():
    import requests
    assert hasattr(requests, "__version__")