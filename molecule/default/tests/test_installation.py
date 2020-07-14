"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_VERSIONS = {
    'buster': '7.3',
    'stretch': '7.0',
    'focal': '7.4',
    'bionic': '7.2',
    'xenial': '7.0',
}


def test_packages(host):
    """
    Ensure package installed
    """

    assert host.package('php').is_installed


def test_config_files(host):
    """
    Ensure configuration files exists
    """

    _version = PHP_VERSIONS[host.system_info.codename]

    assert host.file('/etc/php/{}/fpm/php.ini'.format(_version)).exists
    assert host.file('/etc/php/{}/fpm/php.ini'.format(_version)).is_file

    assert host.file('/etc/php/{}/cli/php.ini'.format(_version)).exists
    assert host.file('/etc/php/{}/cli/php.ini'.format(_version)).is_file


def test_config_files_content(host):
    """
    Test configuration file content
    """

    _version = PHP_VERSIONS[host.system_info.codename]

    cfg_file = host.file('/etc/php/{}/cli/php.ini'.format(_version))
    assert cfg_file.contains('precision = 15')
    assert cfg_file.contains(r'\[sqlite\]') is False
    assert cfg_file.contains(r'\[sqlite3\]') is False


def test_modules(host):
    """
    Ensure JSON module is disabled
    """

    _version = PHP_VERSIONS[host.system_info.codename]

    cfg_file = host.file('/etc/php/{}/cli/conf.d/20-json.ini'.format(_version))
    assert cfg_file.exists is False
