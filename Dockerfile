FROM node:22-alpine
WORKDIR /app
COPY server.js index.html ./
COPY levels/ ./levels/
ENV PORT=8080 DB_PATH=/data/scores.json
EXPOSE 8080
CMD ["node", "server.js"]
