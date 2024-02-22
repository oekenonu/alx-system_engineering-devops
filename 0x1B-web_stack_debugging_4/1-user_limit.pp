# Enable the user holberton on server.
# Increase hard file limit for user holberton.

exec { 'increase-hard-file-limit-for-user-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton.
exec { 'increase-soft-file-limit-for-user-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
