var url='https://music.163.com/#/user/home?id=16702185';
var page=require('webpage').create();

page.open(url,function(status){
	var title=page.evaluate(function(){
		return document.title;
	});
	console.log('Page title is '+ title);
	phantom.exit();
});