# Fixes  nginx
exec { 'nginx':
  command  => "sed -i '$ holberton hard nofile 1048576\nholberton soft nofile 1048576' /etc/security/limits.conf"
  provider => shell,
}
