# Review the Efficient Spring Logging Guide in Grafana

Area: [[areas/work-systems/work-systems|Work Systems]]
Due: 2026-09-03

## Action

Review the guide on logging efficiently from Spring into Grafana, and note what applies to NCTool and FCM. NCTool already emits JSON logs after [[archives/next-actions/2026-08-10 - Refactor the Log for NCTool|refactoring its log]], so focus on what to log, at which level, and how to keep volume and cost sane.

Also cover how to find and search a log file from the Linux terminal, for when Grafana is not available or the log only exists on the box: locating the file, searching it, following it live, and reading rotated or compressed logs.



https://decodingtech.medium.com/logging-like-a-pro-mastering-slf4j-and-logback-for-effective-java-logging-aa4f3b61afa7
https://grafana.com/docs/loki/latest/send-data/
https://loki4j.github.io/loki-logback-appender/
https://medium.com/@bectorhimanshu/logging-and-monitoring-in-springboot-with-loki-and-visualizing-loki-logs-in-grafana-f15bad714996
https://www.baeldung.com/spring-boot-loki-grafana-logging
https://codingtechroom.com/tutorial/java-spring-boot-loki-grafana-logging-guide
https://github.com/tkowalcz/tjahzi

## Done When

- I have a short set of logging practices I want to apply to NCTool and FCM, captured as a note or as a follow-up action.
- I can search a log file from the Linux terminal without looking it up.

## Disposition

Completed 2026-09-03. Captured as [[resources/software-engineering/logging/logging|the Logging collection]]. The Linux terminal half of the Done When was not covered.
