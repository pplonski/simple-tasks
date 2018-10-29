### STAGE 1: Build ###
FROM node:8.12.0-alpine as client_builder

WORKDIR /app/client
ADD ./client /app/client
RUN npm install && PUBLIC_URL=/client npm run build && rm -rf node_modules




### STAGE 2: Production Environment ###
FROM nginx:1.13.12-alpine
#ADD ./client /app/client
#WORKDIR /app/client/build
#COPY --from=client_builder /app/client/build /app/client/build
#RUN ls -al /app/client
#RUN ls -al /app/client/build

CMD ["nginx", "-g", "daemon off;"]
