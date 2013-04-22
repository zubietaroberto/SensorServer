$(function(){
		
		data = getData();
		
		var parsed_data = [];
		
		$.each(data, function(key, value){
			parsed_data.push({
				date: parseDate(value.fields.date),
				temperature: value.fields.temperature,
			});
		});
		
		drawChart(parsed_data);
});

function parseDate(dateString){
	
	//2013-04-21T17:10:25Z
	split1 = dateString.split("-");
	split2 = split1[2].split("T");
	split3 = split2[1].split(":");
	split4 = split3[2].split("Z");
	
	year = split1[0];
	month = split1[1] - 1;
	day = split2[0];
	hour = split3[0];
	minute = split3[1];
	second = split4[0];
		
	return new Date(year, month, day, hour, minute, second);
}

function drawChart(json){	
    // SERIAL CHART    
    chart = new AmCharts.AmSerialChart();
    chart.autoMarginOffset = 5;
    chart.marginBottom = 0;
    chart.pathToImages = "http://www.amcharts.com/lib/images/";
    chart.zoomOutButton = {
        backgroundColor: '#000000',
        backgroundAlpha: 0.15
    };
    chart.dataProvider = json;
    chart.categoryField = "date";
    chart.balloon.bulletSize = 5;

    // AXES
    // category
    var categoryAxis = chart.categoryAxis;
    categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
    categoryAxis.minPeriod = "mm"; // our data is daily, so we set minPeriod to DD
    categoryAxis.dashLength = 1;
    categoryAxis.gridAlpha = 0.15;
    categoryAxis.position = "top";
    categoryAxis.axisColor = "#DADADA";

    // value                
    var valueAxis = new AmCharts.ValueAxis();
    valueAxis.axisAlpha = 0;
    valueAxis.dashLength = 1;
    chart.addValueAxis(valueAxis);

    // GRAPH
    var graph = new AmCharts.AmGraph();
    graph.title = "red line";
    graph.valueField = "temperature";
    graph.bullet = "round";
    graph.bulletBorderColor = "#FFFFFF";
    graph.bulletBorderThickness = 2;
    graph.lineThickness = 2;
    graph.lineColor = "#5fb503";
    graph.negativeLineColor = "#efcc26";
    graph.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph);
    
    // CURSOR
    chartCursor = new AmCharts.ChartCursor();
    chartCursor.cursorPosition = "mouse";
    chartCursor.pan = true; // set it to fals if you want the cursor to work in "select" mode
    chart.addChartCursor(chartCursor);

    // WRITE
    chart.write("graph");
}