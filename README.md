# php


[![Build Status](https://travis-ci.org/infOpen/ansible-role-php.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-php)

Install php package.

## Requirements

This role requires Ansible 2.0 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role has some testing methods.

To use locally testing methods, you need to install Docker and/or Vagrant and Python requirements:

* Create and activate a virtualenv
* Install requirements

```
pip install -r requirements_dev.txt
```

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

### Default role variables

```yaml
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
php_module_to_enable: []
php_module_to_disable: []

# Services to manage if packages or configuration is updated
php_dependencies_services: "{{ _php_dependencies_services }}"
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.php }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
