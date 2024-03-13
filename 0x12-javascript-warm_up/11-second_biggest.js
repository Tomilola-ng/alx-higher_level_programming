#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
	const args = argv.slice(2);
	args.sort((a, b) => b - a);

	console.log(args[1]);
}
