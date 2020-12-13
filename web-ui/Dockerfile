FROM node:lts-alpine3.9 AS build
WORKDIR /app
COPY . /app
RUN npm install -g @angular/cli
RUN npm install
RUN ng build
FROM nginx:alpine
COPY --from=build /app/config/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
RUN sed -i 's#<base href="/">#<base href="/web-ui/">#g' /usr/share/nginx/html/web-ui/index.html

