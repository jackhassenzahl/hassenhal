server {
    listen 80;
    server_name example.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.html index.php;

	location / {
		try_files $uri $uri/ =404;
		add_header Cache-Control "no-store, must-revalidate";
	}
}
