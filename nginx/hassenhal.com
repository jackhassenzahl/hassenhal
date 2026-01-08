server {
    listen 80;
    server_name hassenhal.com www.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.php index.html;

	location / {
		try_files $uri $uri/ =404;
	}

    location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php8.4-fpm.sock;
    }
}
