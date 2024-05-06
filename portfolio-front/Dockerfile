FROM node:18.13.0
LABEL maintainer="bensongathu23@gmail.com"
WORKDIR /code
COPY ./package.json /code/package.json
RUN npm install
COPY . /code
EXPOSE 3000

CMD [ "npm", "start" ]