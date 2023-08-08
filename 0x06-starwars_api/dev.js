#!/usr/bin/node

/* eslint-disable */
const request = require('request');

function getCharacterEndPoints(filmID) {
  const filmURL = `https://swapi-api.alx-tools.com/api/films/${filmID}`;
  return new Promise((resolve, reject) => {
    request(filmURL, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

getCharacterEndPoints(3)
  .then((userEndPoints) => {
    const requests = userEndPoints.map((element) => {
      return new Promise((resolve, reject) => {
        request(element, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(requests)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => console.log(error));
  })
  .catch((error) => console.log(error));
