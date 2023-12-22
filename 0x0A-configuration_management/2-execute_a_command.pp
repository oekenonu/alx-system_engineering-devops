# Terminate process killmenow

exec{ 'pkill killmenow':
  path => '/etc/bin:/usr/bin:/bin',
}
