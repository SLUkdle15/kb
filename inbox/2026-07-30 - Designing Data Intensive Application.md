# Designing Data Intensive Application

The three concerns that are important in most software systems:

- Reliability: “continuing to work correctly, even when things go wrong.”
- Scalability: a system’s ability to cope with increased load.
	- how does system performance change as a specific load parameter grows?
	- performance: response time and usually it is better to use percentiles.
		- **-> High percentiles of response times, also known as tail latencies, are important because they directly affect users’ experience of the service**
- Maintainability
