server {
    listen 80;
    server_name assassin.hassenhal.com;

    root /var/www/html/hassenhal/assassin;
	index index.html;

    location / {
		add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0";
		try_files $uri $uri/ =404;
	}
}
