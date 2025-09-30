server {
    listen 80;
    server_name hassenhal.com www.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.html;

	location / {
		add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0";
		try_files $uri $uri/ =404;
	}
}
