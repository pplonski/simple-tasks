FROM node:8.12.0-alpine as client_builder

WORKDIR /app/client
ADD ./client /app/client

RUN npm install
RUN npm run build
RUN ls
RUN ls build
