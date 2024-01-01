# 100-puppet_ssh_config.pp
include stdlib

# Disable password authentication in SSH
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

# Configure SSH client to use the private key
file_line { 'Declare identity file':
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}
