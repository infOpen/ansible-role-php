php
===

[![Build Status](https://travis-ci.org/infOpen/ansible-role-php.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-php)

Install php package.

Requirements
------------

This role requires Ansible 1.5 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Default role variables

    # Package variables
    #------------------
    php_package_state   : present

    php_module_to_enable  : []
    php_module_to_disable : []


    #============================= Main configuration ==============================

    # PHP section
    php_config_main_display_errors          : "Off"
    php_config_main_display_startup_errors  : "Off"
    php_config_main_error_reporting         : "E_ALL & ~E_DEPRECATED & ~E_STRICT"
    php_config_main_html_errors             : "On"
    php_config_main_log_errors              : "On"
    php_config_main_max_input_time          : "60 (60 seconds)"
    php_config_main_output_buffering        : 4096
    php_config_main_register_argc_argv      : "Off"
    php_config_main_request_order           : "GP"
    php_config_main_session_bug_compat_42   : "Off"
    php_config_main_session_bug_compat_warn : "Off"
    php_config_main_session_gc_divisor      : 1000
    php_config_main_session_hash_bits_per_character : 5
    php_config_main_short_open_tag          : "Off"
    php_config_main_track_errors            : "Off"
    php_config_main_url_rewriter_tags :
      - "a=href"
      - "area=href"
      - "frame=src"
      - "input=src"
      - "form=fakeentry"
    php_config_main_variables_order     : "GPCS"

    # php.ini options
    php_config_main_user_ini_filename   : False
    php_config_main_user_ini_cache_ttl  : 300

    # Language options
    php_config_main_language_engine                         : "On"
    php_config_main_language_short_open_tag                 : "Off"
    php_config_main_language_asp_tags                       : "Off"
    php_config_main_language_precision                      : 14

    php_config_main_language_output_buffering               : 4096
    php_config_main_language_output_handler                 : False

    php_config_main_language_zlib_output_compression        : "Off"
    php_config_main_language_zlib_output_compression_level  : -1
    php_config_main_language_zlib_output_handler            : False

    php_config_main_language_implicit_flush                 : "Off"
    php_config_main_language_unserialize_callback_func      : False
    php_config_main_language_serialize_precision            : 17

    php_config_main_language_open_basedir                   : False
    php_config_main_language_disable_functions :
      - pcntl_alarm
      - pcntl_fork
      - pcntl_waitpid
      - pcntl_wait
      - pcntl_wifexited
      - pcntl_wifstopped
      - pcntl_wifsignaled
      - pcntl_wexitstatus
      - pcntl_wtermsig
      - pcntl_wstopsig
      - pcntl_signal
      - pcntl_signal_dispatch
      - pcntl_get_last_error
      - pcntl_strerror
      - pcntl_sigprocmask
      - pcntl_sigwaitinfo
      - pcntl_sigtimedwait
      - pcntl_exec
      - pcntl_getpriority
      - pcntl_setpriority
    php_config_main_language_disable_classes : []

    php_config_main_language_highlight_color :
      string  : "#DD0000"
      comment : "#FF9900"
      keyword : "#007700"
      default : "#0000BB"
      html    : "#000000"

    php_config_main_language_ignore_user_abort    : "On"
    php_config_main_language_realpath_cache_size  : "16k"
    php_config_main_language_realpath_cache_ttl   : 120

    php_config_main_language_zend_enable_gc       : "On"
    php_config_main_language_zend_multibyte       : "Off"
    php_config_main_language_zend_script_encoding : ""


    # Miscellaneous
    php_config_main_miscellaneous_expose_php      : "On"


    # Resource Limits
    php_config_main_ressource_limits_max_execution_time      : 30
    php_config_main_ressource_limits_max_input_time          : 60
    php_config_main_ressource_limits_max_input_nesting_level : 64
    php_config_main_ressource_limits_max_input_vars          : 1000
    php_config_main_ressource_limits_memory_limit            : "128M"


    # Error handling and logging
    php_config_main_error_reporting         : "E_ALL & ~E_DEPRECATED & ~E_STRICT"
    php_config_main_display_errors          : "Off"
    php_config_main_display_startup_errors  : "Off"

    php_config_main_log_errors              : "On"
    php_config_main_log_errors_max_len      : 1024

    php_config_main_ignore_repeated_errors  : "Off"
    php_config_main_ignore_repeated_source  : "Off"

    php_config_main_report_memleaks         : "On"
    php_config_main_report_zend_debug       : 0
    php_config_main_track_errors            : "Off"

    php_config_main_xmlrpc_errors           : 0
    php_config_main_xmlrpc_error_number     : 0

    php_config_main_html_errors             : "On"
    php_config_main_docref_root             : ""
    php_config_main_docref_ext              : ".html"

    php_config_main_error_prepend_string    : ""
    php_config_main_error_append_string     : ""

    php_config_main_error_log                : "/var/log/apache2/php-errors.log"
    php_config_main_windows_show_crt_warning : 0


    # Data Handling
    php_config_main_arg_separator_output    : "&"
    php_config_main_arg_separator_input     : "&"

    php_config_main_variables_order         : "GPCS"
    php_config_main_request_order           : "GP"

    php_config_main_register_argc_argv      : "Off"
    php_config_main_auto_globals_jit        : "On"

    php_config_main_enable_post_data_reading : "On"
    php_config_main_post_max_size            : 8M

    php_config_main_auto_prepend_file       : ""
    php_config_main_auto_append_file        : ""

    php_config_main_default_mimetype        : "text/html"
    php_config_main_default_charset         : ""

    php_config_main_always_populate_raw_post_data : "Off"


    # Paths and Directories
    php_config_main_include_path :
      - "."
      - "/usr/share/php"
      - "/usr/share/php/PEAR"
    php_config_main_doc_root                : ""
    php_config_main_user_dir                : ""
    php_config_main_extension_dir           : "./"
    php_config_main_sys_temp_dir            : "/tmp"

    php_config_main_enable_dl               : "Off"

    php_config_main_cgi_force_redirect      : 1
    php_config_main_cgi_nph                 : 0
    php_config_main_cgi_redirect_status_env : ""
    php_config_main_cgi_fix_pathinfo        : 1
    php_config_main_fastcgi_impersonate     : 0
    php_config_main_fastcgi_logging         : 1
    php_config_main_cgi_rfc2616_headers     : 0


    # File Uploads
    php_config_main_file_uploads            : "On"
    php_config_main_upload_tmp_dir          : "/tmp"
    php_config_main_upload_max_filesize     : 2M
    php_config_main_max_file_uploads        : 20


    # Fopen wrappers
    php_config_main_allow_url_fopen          : "On"
    php_config_main_allow_url_include        : "Off"
    php_config_main_from                     : ""
    php_config_main_user_agent               : ""
    php_config_main_default_socket_timeout   : 60
    php_config_main_auto_detect_line_endings : "Off"


    # Dynamic Extensions
    php_config_main_dynamic_extensions : []


    # Module Settings
    php_config_main_module_cli_server_color : "On"

    php_config_main_module_date_timezone            : "Europe/Paris"
    php_config_main_module_date_default_latitude    : "31.7667"
    php_config_main_module_date_default_longitude   : "35.2333"
    php_config_main_module_date_sunrise_zenith      : "90.583333"
    php_config_main_module_date_sunset_zenith       : "90.583333"

    php_config_main_module_filter_default           : "unsafe_raw"
    php_config_main_module_filter_default_flags     : ""

    php_config_main_module_iconv_input_encoding     : "ISO-8859-1"
    php_config_main_module_iconv_internal_encoding  : "ISO-8859-1"
    php_config_main_module_iconv_output_encoding    : "ISO-8859-1"

    php_config_main_module_intl_default_locale      : ""
    php_config_main_module_intl_error_level         : 0

    php_config_main_module_sqlite_assoc_case        : 0
    php_config_main_module_sqlite3_extension_dir    : ""

    php_config_main_module_pcre_backtrack_limit     : 100000
    php_config_main_module_pcre_recursion_limit     : 100000

    php_config_main_module_pdo_odbc_connection_pooling  : "strict"
    php_config_main_module_pdo_odbc_db2_instance_name   : ""

    php_config_main_module_pdo_mysql_cache_size     : 2000
    php_config_main_module_pdo_mysql_default_socket : ""

    php_config_main_module_phar_readonly            : "On"
    php_config_main_module_phar_require_hash        : "On"
    php_config_main_module_phar_cache_list          : ""

    php_config_main_module_SMTP                         : "localhost"
    php_config_main_module_smtp_port                    : 25
    php_config_main_module_sendmail_from                : ""
    php_config_main_module_sendmail_path                : "sendmail -t -i"
    php_config_main_module_mail_force_extra_parameters  : ""
    php_config_main_module_mail_add_x_header            : "On"
    php_config_main_module_mail_log                     : ""

    php_config_main_module_sql_safe_mode            : "Off"

    php_config_main_module_odbc_default_db          : ""
    php_config_main_module_odbc_default_user        : ""
    php_config_main_module_odbc_default_pw          : ""
    php_config_main_module_odbc_default_cursortype  : "SQL_CURSOR_STATIC"
    php_config_main_module_odbc_allow_persistent    : "On"
    php_config_main_module_odbc_check_persistent    : "On"
    php_config_main_module_odbc_max_persistent      : -1
    php_config_main_module_odbc_max_links           : -1
    php_config_main_module_odbc_defaultlrl          : 4096
    php_config_main_module_odbc_defaultbinmode      : 1
    php_config_main_module_birdstep_max_links       : -1

    php_config_main_module_ibase_allow_persistent   : 1
    php_config_main_module_ibase_max_persistent     : -1
    php_config_main_module_ibase_max_links          : -1
    php_config_main_module_ibase_default_db         : ""
    php_config_main_module_ibase_default_user       : ""
    php_config_main_module_ibase_default_password   : ""
    php_config_main_module_ibase_default_charset    : ""
    php_config_main_module_ibase_timestampformat    : "%Y-%m-%d %H:%M:%S"
    php_config_main_module_ibase_dateformat         : "%Y-%m-%d"
    php_config_main_module_ibase_timeformat         : "%H:%M:%S"

    php_config_main_module_mysql_allow_local_infile : "On"
    php_config_main_module_mysql_allow_persistent   : "On"
    php_config_main_module_mysql_cache_size         : 2000
    php_config_main_module_mysql_max_persistent     : -1
    php_config_main_module_mysql_max_links          : -1
    php_config_main_module_mysql_default_port       : ""
    php_config_main_module_mysql_default_socket     : ""
    php_config_main_module_mysql_default_host       : ""
    php_config_main_module_mysql_default_user       : ""
    php_config_main_module_mysql_default_password   : ""
    php_config_main_module_mysql_connect_timeout    : 60
    php_config_main_module_mysql_trace_mode         : "Off"

    php_config_main_module_mysqli_max_persistent     : -1
    php_config_main_module_mysqli_allow_local_infile : "On"
    php_config_main_module_mysqli_allow_persistent   : "On"
    php_config_main_module_mysqli_max_links          : -1
    php_config_main_module_mysqli_cache_size         : 2000
    php_config_main_module_mysqli_default_port       : 3306
    php_config_main_module_mysqli_default_socket     : ""
    php_config_main_module_mysqli_default_host       : ""
    php_config_main_module_mysqli_default_user       : ""
    php_config_main_module_mysqli_default_pw         : ""
    php_config_main_module_mysqli_reconnect          : "Off"

    php_config_main_module_mysqlnd_collect_statistics        : "On"
    php_config_main_module_mysqlnd_collect_memory_statistics : "Off"
    php_config_main_module_mysqlnd_net_cmd_buffer_size       : False #2048
    php_config_main_module_mysqlnd_net_read_buffer_size      : False #32768

    php_config_main_module_oci8_privileged_connect      : "Off"
    php_config_main_module_oci8_max_persistent          : -1
    php_config_main_module_oci8_persistent_timeout      : -1
    php_config_main_module_oci8_ping_interval           : 60
    php_config_main_module_oci8_connection_class        : ""
    php_config_main_module_oci8_events                  : "Off"
    php_config_main_module_oci8_statement_cache_size    : 20
    php_config_main_module_oci8_default_prefetch        : 100
    php_config_main_module_oci8_old_oci_close_semantics : "Off"

    php_config_main_module_pgsql_allow_persistent       : "On"
    php_config_main_module_pgsql_auto_reset_persistent  : "Off"
    php_config_main_module_pgsql_max_persistent         : -1
    php_config_main_module_pgsql_max_links              : -1
    php_config_main_module_pgsql_ignore_notice          : 0
    php_config_main_module_pgsql_log_notice             : 0

    php_config_main_module_sybct_allow_persistent       : "On"
    php_config_main_module_sybct_max_persistent         : -1
    php_config_main_module_sybct_max_links              : -1
    php_config_main_module_sybct_min_server_severity    : 10
    php_config_main_module_sybct_min_client_severity    : 10
    php_config_main_module_sybct_timeout                : ""
    php_config_main_module_sybct_packet_size            : False # No info in doc
    php_config_main_module_sybct_login_timeout          : 60
    php_config_main_module_sybct_hostname               : ""
    php_config_main_module_sybct_deadlock_retry_count   : 0

    php_config_main_module_bcmath_scale : 0

    php_config_main_module_browscap     : ""

    php_config_main_module_session_save_handler             : "files"
    php_config_main_module_session_save_path                : ""
    php_config_main_module_session_use_strict_mode          : 0
    php_config_main_module_session_use_cookies              : 1
    php_config_main_module_session_cookie_secure            : ""
    php_config_main_module_session_use_only_cookies         : 1
    php_config_main_module_session_name                     : "PHPSESSID"
    php_config_main_module_session_auto_start               : 0
    php_config_main_module_session_cookie_lifetime          : 0
    php_config_main_module_session_cookie_path              : "/"
    php_config_main_module_session_cookie_domain            : ""
    php_config_main_module_session_cookie_httponly          : ""
    php_config_main_module_session_serialize_handler        : "php"
    php_config_main_module_session_gc_probability           : 0
    php_config_main_module_session_gc_divisor               : 1000
    php_config_main_module_session_gc_maxlifetime           : 1400
    php_config_main_module_session_bug_compat_42            : "Off"
    php_config_main_module_session_bug_compat_warn          : "Off"
    php_config_main_module_session_referer_check            : ""
    php_config_main_module_session_entropy_length           : 0
    php_config_main_module_session_entropy_file             : ""
    php_config_main_module_session_cache_limiter            : "nocache"
    php_config_main_module_session_cache_expire             : 180
    php_config_main_module_session_use_trans_sid            : 0
    php_config_main_module_session_hash_function            : 0
    php_config_main_module_session_hash_bits_per_character  : 5
    php_config_main_module_session_upload_progress_enabled  : "On"
    php_config_main_module_session_upload_progress_cleanup  : "On"
    php_config_main_module_session_upload_progress_prefix   : "upload_progress_"
    php_config_main_module_session_upload_progress_name     : "PHP_SESSION_UPLOAD_PROGRESS"
    php_config_main_module_session_upload_progress_freq     : "1%"
    php_config_main_module_session_upload_progress_min_freq : "1"
    php_config_main_module_url_rewriter_tags :
      - "a=href"
      - "area=href"
      - "frame=src"
      - "input=src"
      - "form=fakeentry"

    php_config_main_module_mssql_allow_persistent       : "On"
    php_config_main_module_mssql_max_persistent         : -1
    php_config_main_module_mssql_max_links              : -1
    php_config_main_module_mssql_min_error_severity     : 10
    php_config_main_module_mssql_min_message_severity   : 10
    php_config_main_module_mssql_compatibility_mode     : "Off"
    php_config_main_module_mssql_connect_timeout        : 5
    php_config_main_module_mssql_timeout                : 60
    php_config_main_module_mssql_textlimit              : 4096
    php_config_main_module_mssql_textsize               : 4096
    php_config_main_module_mssql_batchsize              : 0
    php_config_main_module_mssql_datetimeconvert        : "On"
    php_config_main_module_mssql_secure_connection      : "Off"
    php_config_main_module_mssql_max_procs              : -1
    php_config_main_module_mssql_charset                : ""

    php_config_main_module_assert_active                : "On"
    php_config_main_module_assert_warning               : "On"
    php_config_main_module_assert_bail                  : "Off"
    php_config_main_module_assert_callback              : ""
    php_config_main_module_assert_quiet_eval            : 0

    php_config_main_module_com_typelib_file                 : ""
    php_config_main_module_com_allow_dcom                   : "false"
    php_config_main_module_com_autoregister_typelib         : "false"
    php_config_main_module_com_autoregister_casesensitive   : "true"
    php_config_main_module_com_autoregister_verbose         : "false"
    php_config_main_module_com_code_page                    : ""

    php_config_main_module_mbstring_language                    : "neutral"
    php_config_main_module_mbstring_internal_encoding           : ""
    php_config_main_module_mbstring_http_input                  : "pass"
    php_config_main_module_mbstring_http_output                 : "pass"
    php_config_main_module_mbstring_encoding_translation        : "Off"
    php_config_main_module_mbstring_detect_order                : ""
    php_config_main_module_mbstring_substitute_character        : ""
    php_config_main_module_mbstring_func_overload               : 0
    php_config_main_module_mbstring_strict_detection            : "On"
    php_config_main_module_mbstring_http_output_conv_mimetype   : '^(text/|application/xhtml\+xml)'

    php_config_main_module_gd_jpeg_ignore_warning       : 0

    php_config_main_module_exif_encode_unicode          : "ISO-8859-15"
    php_config_main_module_exif_decode_unicode_motorola : "UCS-2BE"
    php_config_main_module_exif_decode_unicode_intel    : "UCS-2LE"
    php_config_main_module_exif_encode_jis              : ""
    php_config_main_module_exif_decode_jis_motorola     : "JIS"
    php_config_main_module_exif_decode_jis_intel        : "JIS"

    php_config_main_module_tidy_default_config  : ""
    php_config_main_module_tidy_clean_output    : "Off"

    php_config_main_module_soap_wsdl_cache_enabled  : 1
    php_config_main_module_soap_wsdl_cache_dir      : "/tmp"
    php_config_main_module_soap_wsdl_cache_ttl      : 86400
    php_config_main_module_soap_wsdl_cache_limit    : 5

    php_config_main_module_sysvshm_init_mem : 10000

    php_config_main_module_ldap_max_links   : -1

    php_config_main_module_mcrypt_algorithms_dir    : ""
    php_config_main_module_mcrypt_modes_dir         : ""

    php_config_main_module_dba_default_handler : ""

    php_config_main_module_opcache_enable                   : 1
    php_config_main_module_opcache_enable_cli               : 0
    php_config_main_module_opcache_memory_consumption       : 64
    php_config_main_module_opcache_interned_strings_buffer  : 4
    php_config_main_module_opcache_max_accelerated_files    : 2000
    php_config_main_module_opcache_max_wasted_percentage    : 5
    php_config_main_module_opcache_use_cwd                  : 1
    php_config_main_module_opcache_validate_timestamps      : 1
    php_config_main_module_opcache_revalidate_freq          : 2
    php_config_main_module_opcache_revalidate_path          : 0
    php_config_main_module_opcache_save_comments            : 1
    php_config_main_module_opcache_load_comments            : 1
    php_config_main_module_opcache_fast_shutdown            : 0
    php_config_main_module_opcache_enable_file_override     : 0
    php_config_main_module_opcache_optimization_level       : "0xffffffff"
    php_config_main_module_opcache_inherited_hack           : 1
    php_config_main_module_opcache_dups_fix                 : 0
    php_config_main_module_opcache_blacklist_filename       : ""
    php_config_main_module_opcache_max_file_size            : 0
    php_config_main_module_opcache_consistency_checks       : 0
    php_config_main_module_opcache_force_restart_timeout    : 180
    php_config_main_module_opcache_error_log                : ""
    php_config_main_module_opcache_log_verbosity_level      : 1
    php_config_main_module_opcache_preferred_memory_model   : ""
    php_config_main_module_opcache_protect_memory           : 0

    php_config_main_module_curl_cainfo : ""


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: achaussier.php }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
