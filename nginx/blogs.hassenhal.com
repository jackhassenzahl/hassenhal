server {
    listen 80;
    server_name blogs.hassenhal.com;

    root /var/www/html/hassenhal;
	index blogs/index.html;

    location / {
		try_files $uri $uri/ =404;
	}
}
