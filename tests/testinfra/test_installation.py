"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_packages(SystemInfo, Package):

    if SystemInfo.codename == 'trusty':
        assert Package('php5').is_installed

    elif SystemInfo.codename == 'xenial':
        assert Package('php').is_installed
