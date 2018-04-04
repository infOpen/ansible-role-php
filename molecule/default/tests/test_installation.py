"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('codename,package_name', [
    ('trusty', 'php5'),
    ('xenial', 'php'),
])
def test_packages(host, codename, package_name):
    """
    Ensure package installed
    """

    if host.system_info.codename != codename:
        pytest.skip('This element not apply on this codename')

    assert host.package(package_name).is_installed


@pytest.mark.parametrize('codename,path', [
    ('trusty', '/etc/php5/apache2/php.ini'),
    ('trusty', '/etc/php5/cli/php.ini'),
    ('xenial', '/etc/php/7.0/fpm/php.ini'),
    ('xenial', '/etc/php/7.0/cli/php.ini'),
])
def test_config_files(host, codename, path):
    """
    Ensure configuration files exists
    """

    if host.system_info.codename != codename:
        pytest.skip('This element not apply on this codename')

    cfg_file = host.file(path)
    assert cfg_file.exists
    assert cfg_file.is_file


@pytest.mark.parametrize('codename,path', [
    ('trusty', '/etc/php5/cli/php.ini'),
    ('xenial', '/etc/php/7.0/cli/php.ini'),
])
def test_config_files_content(host, codename, path):
    """
    Test configuration file content
    """

    if host.system_info.codename != codename:
        pytest.skip('This element not apply on this codename')

    cfg_file = host.file(path)
    assert cfg_file.contains('precision = 15')
    assert cfg_file.contains('\[sqlite\]') is False
    assert cfg_file.contains('\[sqlite3\]') is False


@pytest.mark.parametrize('codename,path', [
    ('trusty', '/etc/php5/cli/conf.d/20-json.ini'),
    ('xenial', '/etc/php/7.0/cli/conf.d/20-json.ini'),
])
def test_modules(host, codename, path):
    """
    Ensure JSON module is disabled
    """

    if host.system_info.codename != codename:
        pytest.skip('This element not apply on this codename')

    assert host.file(path).exists is False
