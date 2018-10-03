$(document).on("change", ".file_multi_video", function(evt) {
  var $source = $('#video_here');
  var html = ""
  console.log("this=========>",this.files)
  for(var i=0;i<this.files.length;i++){
	html = '<video width="400" controls id="videoplayer'+i+'">'
			+'<source src="'+URL.createObjectURL(this.files[i])+'" id="video_here'+i+'">'
    +'Your browser does not support HTML5 video.'
+'</video>'
  $('#videoLoad').append(html)
  //$('#video_here'+i).parent()[0].load();
  }
  var videoplayer = document.getElementById("videoplayer0")
  videoplayer.addEventListener("loadeddata", function() {
 	console.log("Audio data loaded",$(this));
 	console.log("Audio duration: " + this.duration);
	
	
  });
  $('video').load();