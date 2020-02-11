#!/usr/bin/node

let fs = require("fs");
const argv = process.argv[2];

fs.readFile(argv, "r", "utf-8", function(error, data) {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});