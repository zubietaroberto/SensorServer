/**
 * @author zubietaroberto
 */


$(function(){
	
	// set up the map
	map = new L.Map('map').setView([8.97, -79.53], 13);;

	// create the tile layer with correct attribution
	L.tileLayer('http://{s}.tile.cloudmade.com/517154c4043b4a68a7671387bf586d15/997/256/{z}/{x}/{y}.png', {
    	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    	maxZoom: 18
	}).addTo(map);
	
	//Get data from database
	$.get('ajax/station/', function(data){
		$.each(data, function(index, value){
			var fields = value.fields;
			
			var marker = L.marker([fields.latitude, fields.longitude]).addTo(map);
			marker.bindPopup(fields.name).openPopup();
			
		});
	});
})
