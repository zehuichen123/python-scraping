var page=require('webpage').create();


page.viewportSize={width:1024,height:768};
page.clipRect={top:0,left:0,width:1024,height:768};

page.open('https://lovesnowbest.site',function(status){
	console.log('Status: '+status);
	if(status==='success'){
		page.render('lovesnowbest.png');
	}
	phantom.exit();
});