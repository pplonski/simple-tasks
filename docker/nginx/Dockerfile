FROM nginx:1.12-alpine
COPY --from=client /app/client/build /usr/share/nginx/html
RUN ls /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]
