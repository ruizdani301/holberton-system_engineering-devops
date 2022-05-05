# Fixes  nginx
exec { 'nginx':
  command => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx && sudo service nginx restart',
  provider    => shell,
}
