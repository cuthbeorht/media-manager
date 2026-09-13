import pytest


@pytest.fixture
def project_root(request):
    return request.config.rootpath
