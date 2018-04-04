# php

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-php/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-php)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-php/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-php)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-php/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-php/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-php/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-php/)
[![Ansible Role](https://img.shields.io/ansible/role/13080.svg)](https://galaxy.ansible.com/infOpen/php/)

Install php package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Installation
php_apt_update_cache: True
php_apt_cache_valid_time: 3600
php_packages: "{{ _php_packages }}"

# Configuration
php_config_base_path: "{{ _php_config_base_path }}"
php_config_files_owner: 'root'
php_config_files_group: 'root'
php_config_files_mode: '0644'
php_config_settings: "{{ _php_config_settings }}"

# Modules management
php_modules_binary_disable: "{{ _php_modules_binary_disable }}"
php_modules_binary_enable: "{{ _php_modules_binary_enable }}"
php_modules_enabled: "{{ _php_modules_enabled }}"

# Services to manage if packages or configuration is updated
php_dependencies_services: "{{ _php_dependencies_services }}"
```

## How define ...

### Custom settings into ini files

``` yaml
php_config_settings:
  - dest: "{{ php_config_base_path }}/cli/php.ini"
    settings:
      - section: 'PHP'
        option: 'precision'
        value: 15
      - section: 'sqlite3'
        state: 'absent'
      - section: 'sqlite'
        state: 'absent'
  - dest: "{{ php_config_base_path }}/apache2/php.ini"
    settings: []
```

### Enabled modules

``` yaml
php_modules_enabled:
  - 'json'
  - 'opcache'
  - 'pdo'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.php }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
