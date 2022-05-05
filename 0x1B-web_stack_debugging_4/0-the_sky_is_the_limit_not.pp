# Fixes  nginx
exec { 'nginx':
  command => 'sed -i '3i worker_rlimit_nofile 1048576 /etc/nginx/nginx.conf; sudo service nginx restart',
  path    => ['/bin', '/user/bin', '/usr/sbin']
}
