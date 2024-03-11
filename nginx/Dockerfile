FROM nginx:1.19-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
RUN apk --no-cache add openssl
RUN openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
-keyout localhost.key -out localhost.crt \
-subj "/C=US/ST=YourState/L=YourCity/O=YourOrganization/CN=localhost"
RUN mkdir -p /etc/ssl/certs /etc/ssl/private
RUN mv localhost.crt /etc/ssl/certs/
RUN mv localhost.key /etc/ssl/private/
