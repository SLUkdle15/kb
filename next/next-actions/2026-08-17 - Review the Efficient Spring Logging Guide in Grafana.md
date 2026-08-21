# Review the Efficient Spring Logging Guide in Grafana

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Review the guide on logging efficiently from Spring into Grafana, and note what applies to NCTool and FCM. NCTool already emits JSON logs after [[archives/next-actions/2026-08-10 - Refactor the Log for NCTool|refactoring its log]], so focus on what to log, at which level, and how to keep volume and cost sane.

npm install --legacy-peer-deps

https://katyella.com/blog/spring-boot-logging-best-practices/
https://tayjava.com/technologies/logging-in-spring-boot-slf4j-logback-structured-logging-for-production
https://amigoscode.com/blogs/spring-boot-logging-guide
https://medium.com/parallel-engine-technologies/mastering-slf4j-with-logback-the-ultimate-guide-to-logging-patterns-22ce89d31a40
https://decodingtech.medium.com/logging-like-a-pro-mastering-slf4j-and-logback-for-effective-java-logging-aa4f3b61afa7
https://grafana.com/docs/loki/latest/send-data/
https://loki4j.github.io/loki-logback-appender/
https://medium.com/@bectorhimanshu/logging-and-monitoring-in-springboot-with-loki-and-visualizing-loki-logs-in-grafana-f15bad714996
https://www.baeldung.com/spring-boot-loki-grafana-logging
https://codingtechroom.com/tutorial/java-spring-boot-loki-grafana-logging-guide
https://github.com/tkowalcz/tjahzi

## Done When

I have a short set of logging practices I want to apply to NCTool and FCM, captured as a note or as a follow-up action.
