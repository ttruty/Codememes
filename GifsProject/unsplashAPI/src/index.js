// require syntax
const Unsplash = require('unsplash-js').default;
const toJson =  require('unsplash-js').toJson;
const fetch = require('node-fetch');
global.fetch=fetch;

const unsplash = new Unsplash({
  accessKey: "##########################",
  // Optionally you can also configure a custom header to be sent with every request
  headers: {
    "X-Custom-Header": "stuff"
  },
  // Optionally if using a node-fetch polyfill or a version of fetch which supports the timeout option, you can configure the request timeout for all requests
  timeout: 500 // values set in ms
});

for (i=0; i < 50; i++)
{
	try{
		unsplash.photos.getRandomPhoto()
			.then(toJson)
			.then(json => {				
				//console.log(json);
				console.log(json.urls.regular);
			});
		}
	catch (err) {
		next("ERROR:");
	}
}
		
