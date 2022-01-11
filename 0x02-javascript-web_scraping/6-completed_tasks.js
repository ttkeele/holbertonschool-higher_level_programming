#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
    if (error) {
	console.log(error);
    }
    const dict = JSON.parse(body).reduce((acc, elem) => {
	if (!acc[elem.userId]) {
	    if (elem.completed) {
		acc[elem.userId] = 1;
	    }
	} else {
	    if (elem.completed) {
		acc[elem.userId] += 1;
	    }
	}
	return acc;
    }, {});
    console.log(dict);
});
