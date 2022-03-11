# execute a command

exec { 'kill killmenow':
command => '/usr/bin/env pkill -f killmenow'
}