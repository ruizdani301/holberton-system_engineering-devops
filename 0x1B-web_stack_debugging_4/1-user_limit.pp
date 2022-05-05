# Fixes  nginx
exec { 'nginx':
  command  => "sed -i '$ a\holberton hard nofile 1048576\nholberton soft nofile 1048576' /etc/security/limits.conf"
  provider => shell,
}