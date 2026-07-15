FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY levels/ /usr/share/nginx/html/levels/
EXPOSE 8080
