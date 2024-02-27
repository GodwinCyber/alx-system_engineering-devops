# create a file in /tmpfile

file {'/tmp/school':
    ensure  => 'file',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
