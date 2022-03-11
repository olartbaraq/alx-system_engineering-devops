# Puppet script to create a file

file { '/tmp/school':
owner   => 'www-data',
group   => 'www-data',
mode    => '0774',
content => 'I love Puppet',
}