server {
    listen 80;
    server_name example.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.php index.html;

	location / {
		try_files $uri $uri/ =404;
		add_header Cache-Control "no-store, must-revalidate";
	}

    location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
    }
}
