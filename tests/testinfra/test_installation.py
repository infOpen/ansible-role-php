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


def test_config_files(SystemInfo, File):

    files = []

    if SystemInfo.codename == 'trusty':
        files = ['/etc/php5/apache2/php.ini', '/etc/php5/cli/php.ini']

    elif SystemInfo.codename == 'xenial':
        files = ['/etc/php/7.0/fpm/php.ini', '/etc/php/7.0/cli/php.ini']

    for current_file in files:
        cfg_file = File(current_file)
        assert cfg_file.exists
        assert cfg_file.is_file


def test_config_files_content(SystemInfo, File):

    cfg_file_path = ''

    if SystemInfo.codename == 'trusty':
        cfg_file_path = '/etc/php5/cli/php.ini'

    elif SystemInfo.codename == 'xenial':
        cfg_file_path = '/etc/php/7.0/cli/php.ini'

    cfg_file = File(cfg_file_path)
    assert cfg_file.contains('precision = 15')
    assert cfg_file.contains('\[sqlite\]') is False
    assert cfg_file.contains('\[sqlite3\]') is False


def test_modules(SystemInfo, File):

    module_link_path = ''

    if SystemInfo.codename == 'trusty':
        module_link_path = '/etc/php5/cli/conf.d/20-json.ini'

    elif SystemInfo.codename == 'xenial':
        module_link_path = '/etc/php/7.0/cli/conf.d/20-json.ini'

    assert File(module_link_path).exists is False
