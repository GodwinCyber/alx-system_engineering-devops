#!/usr/bin/env bash
# using Puppet to make changes to our configuration file. 

file_path { '/etc/ssh/ssh_config':
             ensure => 'present',
content => "
             #SSH configuration
             HOST*
             PasswordAuthentication no
             IdentityFile ~/.ssh/school
            "
}
