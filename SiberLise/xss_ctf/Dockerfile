# Apache ve PHP içeren base image
FROM php:8.2-apache

# Dosyaları kopyala
COPY index.php /var/www/html/
COPY comments.txt /var/www/html/

# Apache'nin yazabilmesi için gerekli izinler
RUN chown -R www-data:www-data /var/www/html/comments.txt \
    && chmod 666 /var/www/html/comments.txt

# CORS desteği için mod_headers aktif et
RUN a2enmod headers

EXPOSE 80
