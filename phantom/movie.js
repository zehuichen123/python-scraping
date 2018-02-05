var page=require('webpage').create();
console.log('the default user agent is '+page.settings.userAgent);
page.settings.userAgent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36';
page.open('http://movie.mtime.com/108737/',function(status){
	if(status!=='success'){
		console.log('Unable to access network');
	}
	else{
		var ua=page.evaluate(function(){
			return document.getElementById('ratingRegion').textContent;
		});
		console.log(ua);
	}
	phantom.exit();
});