const fs = require('fs');

// Load HTML and data
const html = fs.readFileSync('index.html', 'utf8');
const dataContent = fs.readFileSync('data/madinah_books.js', 'utf8');

// Simple DOM simulation
const { JSDOM } = require('jsdom');
const dom = new JSDOM(html, { runScripts: "dangerously" });
const window = dom.window;
const document = window.document;

// Execute madinah_books.js
dom.window.eval(dataContent);
console.log("MADINAH_DATA loaded in DOM. Books count:", dom.window.MADINAH_DATA.books.length);

// Execute app.js
const appJs = fs.readFileSync('app.js', 'utf8');
dom.window.eval(appJs);

console.log("app.js evaluated successfully without syntax error.");
