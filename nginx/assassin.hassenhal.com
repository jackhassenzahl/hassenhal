server {
    listen 80;
    server_name assassin.hassenhal.com;

    root /var/www/html/hassenhal;
	index assassin/index.html;

    location / {
		try_files $uri $uri/ =404;
	}
}
