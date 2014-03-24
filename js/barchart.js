<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>

<script type="text/javascript">

	var dataset = [ 
	{ key: 0, value: 5 },
	{ key: 1, value: 10 },
	{ key: 2, value: 13 },
	{ key: 3, value: 19 },
	{ key: 4, value: 21 },
	{ key: 5, value: 25 },
	{ key: 6, value: 22 },
	{ key: 7, value: 18 },
	{ key: 8, value: 15 },
	{ key: 9, value: 13 },
	{ key: 10, value: 11 },
	{ key: 11, value: 12 },
	{ key: 12, value: 15 },
	{ key: 13, value: 20 },
	{ key: 14, value: 18 },
	{ key: 15, value: 17 },
	{ key: 16, value: 16 },
	{ key: 17, value: 18 },
	{ key: 18, value: 23 },
	{ key: 19, value: 25 }
	];

	var key = function(d) {
		return d.key
	}

	var value = function(d) {
		return d.value
	}

	var duration = 400

	var margin = {top: 20, right: 10, bottom: 20, left: 30};

	var w = 960 - margin.left - margin.right,
	h = 500 - margin.top - margin.bottom;

	var xScale = d3.scale.ordinal()
	.domain(dataset.map(function(d) {return d.key; }))
	.rangeRoundBands([0, w], 0.1);

	var yScale = d3.scale.linear()
	.domain([0, d3.max(dataset, function(d) {
		return d.value
	})])
	.range([h, 0]);

	var heightScale = d3.scale.linear()
	.domain([0, d3.max(dataset, function(d) {
		return d.value
	})])
	.range([0, h])

	var colorScale = d3.scale.linear()
	.domain([d3.min(dataset, value), d3.max(dataset, value)])
	.range(["#e0f3db","#a8ddb5","#43a2ca"])

	var xAxis = d3.svg.axis()
	.scale(xScale)
	.orient('bottom')

	var yAxis = d3.svg.axis()
	.scale(yScale)
	.orient('left')

	var svg = d3.select("#svg").append("svg")
	.attr("width", w + margin.left + margin.right)
	.attr("height", h + margin.top + margin.bottom)
	.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")")

	var columns = svg.selectAll('g.column')
	.data(dataset, key)
	.enter()
	.append('g')
	.classed('column', true)
	.on('mouseover', function (d) {
		var xPosition = parseFloat(d3.select(this).select('rect').attr("x")) + xScale.rangeBand() / 2;
		var yPosition = parseFloat(d3.select(this).select('rect.imaginary').attr('height')) + 14;
		d3.select(this).append("text")
		.attr("id", "tooltip")
		.attr("x", xPosition)
		.attr("y", yPosition)
		.attr("text-anchor", "middle")
		.attr("font-family", "sans-serif")
		.attr("font-size", "11px")
		.attr("font-weight", "bold")
		.attr("fill", "black")
		.text(d.value);
	})
	.on('mouseout', function (d) {
		d3.select(this).select('.real')
		.transition()
		.duration(duration)
		.attr('fill', function(d) { return colorScale(d.value); })
		d3.select("#tooltip").remove();
	})
	.on("click", function() {
		sortBars();
	});

	columns.append('rect')
	.classed('imaginary', true)
	.attr({
		'x': function(d) { return xScale(d.key); },
		'width': xScale.rangeBand(),
		'y': 0,
		'height': function(d) { return h - heightScale(d.value); },
		'opacity': 0                   
	})

	columns.append('rect')
	.classed('real', true)
	.attr({
		'x': function(d) { return xScale(d.key); },
		'width': xScale.rangeBand(),
		'y': function(d) { return yScale(d.value); },
		'height': function(d) { return heightScale(d.value); },
		'fill': function(d) { return colorScale(d.value); }
	})


	svg.append('g')
	.attr('class', 'x axis')
	.attr('transform', 'translate(0,' + h + ')')
	.call(xAxis)

	svg.append('g')
	.attr('class', 'y axis')
	.call(yAxis)

	d3.selectAll('button')
	.on("click", function() {

		var id = d3.select(this).attr('id');
		if (id == 'add') {
			var maxValue = Math.random() * 100,
			lastKeyValue = dataset[dataset.length - 1].key,
			newNumber = Math.floor(Math.random() * maxValue);
			dataset.push({'key': lastKeyValue + 1,
				'value': newNumber});
		} else if (id == 'remove') {
			dataset.shift()
		}

		console.log(dataset)

		xScale.domain(dataset.map(function (d) {return d.key; }))
		yScale.domain([0, d3.max(dataset, value)])
		heightScale.domain([0, d3.max(dataset, value)])
		colorScale.domain([d3.min(dataset, value), d3.max(dataset, value)])

		columns = svg.selectAll('g.column')
		.data(dataset, key)

		columns.exit()
		.selectAll('rect.imaginary')
		.transition()
		.duration(duration)
		.attr('x', -w)
		.remove()
		columns.exit()
		.selectAll('rect.real')
		.transition()
		.duration(duration)
		.attr('x', -w)
		.remove();

		var new_columns = columns.enter()
		.append('g')
		.classed('column', true)
		.on('mouseover', function (d) {
			var xPosition = parseFloat(d3.select(this).select('rect').attr("x")) + xScale.rangeBand() / 2;
			var yPosition = parseFloat(d3.select(this).select('rect.imaginary').attr('height')) + 14;
			d3.select(this).append("text")
			.attr("id", "tooltip")
			.attr("x", xPosition)
			.attr("y", yPosition)
			.attr("text-anchor", "middle")
			.attr("font-family", "sans-serif")
			.attr("font-size", "11px")
			.attr("font-weight", "bold")
			.attr("fill", "black")
			.text(d.value);
		})
		.on('mouseout', function () {
			d3.select(this).select('.real')
			.transition()
			.duration(duration)
			.attr('fill', function(d) { return colorScale(d.value); })
			d3.select("#tooltip").remove();
		})

		new_columns.append('rect')
		.classed('imaginary', true)
		.attr({
			'x': w*2,
			'width': xScale.rangeBand(),
			'y': 0,
			'height': function(d) { return h - heightScale(d.value); },
			'opacity': 0                   
		})

		new_columns.append('rect')
		.classed('real', true)
		.attr({
			'x': w*2,
			'width': xScale.rangeBand(),
			'y': function(d) { return yScale(d.value); },
			'height': function(d) { return heightScale(d.value); },
			'fill': function(d) { return colorScale(d.value); }
		})

		columns.selectAll('rect.imaginary')
		.classed('imaginary', true)
		.attr({
			'x': function(d) { return xScale(d.key); },
			'width': xScale.rangeBand(),
			'y': 0,
			'height': function(d) { return h - heightScale(d.value); },
			'opacity': 0                   
		})

		columns.selectAll('rect.real')
		.transition()
		.duration(duration)
		.attr({
			'x': function(d) { return xScale(d.key); },
			'width': xScale.rangeBand(),
			'y': function(d) { return yScale(d.value); },
			'height': function(d) { return heightScale(d.value); },
			'fill': function(d) { return colorScale(d.value); }
		})

		svg.select('.x.axis')
		.transition()
		.duration(duration)
		.call(xAxis)

		svg.select('.y.axis')
		.transition()
		.duration(duration)
		.call(yAxis)
	});
</script>