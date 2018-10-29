FROM node:8.12.0-alpine

WORKDIR /app/client
ADD ./client /app/client

# RUN npm install && npm run bundle && npm run build && rm -rf node_modules
RUN npm install
RUN npm run build

RUN ls build
RUN pwd

#RUN npm install -g pm2

#CMD ["pm2", "serve", "build", "--no-daemon", "--port", "5000"]

RUN npm install -g pm2
CMD ["serve", "-s", "build", "-l", "5000"]
