# Install Nginx web server

exec {'install':
  provider => shell,
  command  => 'sudo apt update ; sudo apt install nginx -y; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html; sudo sed -i "s|server_name _;|server_name _;\n\n\t location /redirect_me { \n\t return 301 https://www.google.com;\n\t}|" /etc/nginx/sites-available/default; sudo /etc/init.d/nginx reload',
}
