server {
    listen 80;
    server_name gti.hassenhal.com;

    root /var/www/html/hassenhal;
	index gti/index.html;

    location / {
		try_files $uri $uri/ =404;
	}
}
