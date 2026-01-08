server {
    listen 80;
    server_name example.hassenhal.com;

    root /var/www/html/hassenhal;
	index index.php index.html;

    location ^~ /cardgenerator/ {
        alias /var/www/html/hassenhal/cardgenerator/;
        index index.php;

        try_files $uri $uri/ /card/index.php?$query_string;

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php8.4-fpm.sock;
            fastcgi_param SCRIPT_FILENAME /var/www/html/hassenhal/cardgenerator$fastcgi_script_name;
        }
    }

	location / {
        try_files $uri $uri/ /index.php?$query_string;
        add_header Cache-Control "no-store, must-revalidate";
    }

}
