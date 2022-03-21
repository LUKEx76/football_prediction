// Run with Phantom.js

var page = require('webpage').create();

var country = 'germany'
var league = 'bundesliga'
var season = '2013-2014'
var max_pages = 7
var page_count = 1


var url = `https://www.oddsportal.com/soccer/${country}/${league}-${season}/results/#/page/${page_count}/`;
console.log(url)
page.settings.userAgent = 'SpecialAgent';

page.onError = function(msg, trace) {
  console.log('The web page threw an error: ' + msg);
  return;
};

page.onConsoleMessage = function(msg) {
  console.log('The web page said: ' + msg);
};


for (page_count; page_count <= max_pages; page_count++) {
  page.open(url, function () {
  var script = "function(){ return document; }"//"function(){ return document.getElementById('tournamentTable').innerHTML; }";
  var html = page.evaluateJavaScript(script);
  console.log(html);
  //var fs = require('fs');
  //fs.write('ENG_13_14.html', html, 'a');

  phantom.exit(); 
});
}



