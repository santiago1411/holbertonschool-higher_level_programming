#!/usr/bin/node
const args = process.argv[2];
const axios = require('axios').default;
const fs = require('fs');

axios.get(args)
  .then(function (response) {
    fs.writeFile(args[3], response.data, err => {
      if (err) {
        console.log(err);
      }
    });
  });
