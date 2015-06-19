$(document).ready(function() {
	var gauges = [];

	function createGauge(name, label, min, max) {
		var config = {
			size : 120,
			label : label,
			min : undefined != min ? min : 0,
			max : undefined != max ? max : 100,
			minorTicks : 5
		}

		var range = config.max - config.min;
		config.yellowZones = [ {
			from : config.min + range * 0.75,
			to : config.min + range * 0.9
		} ];
		config.redZones = [ {
			from : config.min + range * 0.9,
			to : config.max
		} ];

		gauges[name] = new Gauge(name + "GaugeContainer", config);
		gauges[name].render();
	}

	function createGauges() {
		createGauge("cpu", "CPU");
	}

	function updateGauges() {
		var url = location.href.split("/");
		$.get("/zport/getCPUJSON", {
			ip : url[url.length - 2]
		}).done(function(data) {
			data = JSON.parse(data);
			gauges['cpu'].redraw(data['used'] || 0);
		});
	}

	function initialize() {
		createGauges();
		updateGauges();
		setInterval(updateGauges, 5 * 60 * 1000);
	}
	initialize();
})
