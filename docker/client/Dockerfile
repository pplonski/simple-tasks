FROM node:8.12.0-alpine

WORKDIR /app/client
ADD ./client /app/client

RUN npm install && npm run build && rm -rf node_modules

RUN ls build
RUN ls build/static
RUN ls build/static/js
RUN pwd

#RUN npm install -g pm2
#CMD ["pm2", "serve", "build", "--no-daemon", "--port", "5000"]

RUN npm install http-server -g
CMD ["http-server", "./build", "-p", "5000"]
