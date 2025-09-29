server {
    listen 80;
    server_name assassin.hassenhal.com;

    root /var/www/html/hassenhal/assassin;
	index index.html;

    location / {
		try_files $uri $uri/ =404;
	}
}
