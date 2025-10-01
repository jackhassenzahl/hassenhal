server {
    listen 80;
    server_name dev.hassenhal.com;

    root /var/www/html/hassenhal/dev;
	index index.html;

	location / {
		try_files $uri $uri/ =404;
		add_header Cache-Control "no-store, must-revalidate";
	}
}
