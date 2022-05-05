# Fixes  nginx
exec { 'nginx':
  command  => "sed -i '$ a\holberton hard nofile 25000\nholberton soft nofile 25000' /etc/security/limits.conf"
  provider => shell,
}