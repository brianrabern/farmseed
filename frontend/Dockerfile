FROM node:14

WORKDIR /frontend

COPY frontend/ .

RUN npm install
RUN npm cache clean --force

EXPOSE 3000

CMD ["npm", "start"]
