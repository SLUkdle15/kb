# Server A to Server B Connectivity Checks

this is how server A calls B
looking up application belong to what pod -> what node
that node is in what ip range (A)
if calls B fail via webclient
1.check trace route -nI to B from A (reachable)
2. check port open to B both 80 and 443
3. some time the trace route succedd but the port is not open could check the port
4. normally if csoc whilelisting (this case guarding B) -> will allow range IP to trace route. 
5. if csoc not guard A then make them talk to each other.  in this case they need some form of public 
