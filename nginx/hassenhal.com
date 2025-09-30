server {
    listen 80;
    server_name hassenhal.com www.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.html;

	location / {
		try_files $uri $uri/ =404;
	}
	location ~* \.js$ {
		add_header Cache-Control "no-store, must-revalidate";
	}

}
