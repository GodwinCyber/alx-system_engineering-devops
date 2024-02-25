#!/usr/bin/env bash
# using Puppet to make changes to our configuration file. 

file_path { 'Authentications':
             ensure => 'present',
             path => '/etc/ssh/ssh_config',
content => "
             #SSH configuration
             HOST*
             PasswordAuthentication no
             IdentityFile ~/.ssh/school
            "
}
