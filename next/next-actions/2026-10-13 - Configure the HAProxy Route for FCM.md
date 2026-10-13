# Configure the HAProxy Route for FCM

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/add-an-haproxy-route|Add an HAProxy Route]]

## Action

Add the FCM path to the shared HAProxy frontend and point the backend at the right upstream. Two questions to settle while doing it:

- There are two ways in: the old API gateway Kong, and the k8s pods directly — but k8s has its own Kong plane in front of them. Which one should the backend target, and why can I route straight there at all?
- Where does the `no route` come from — HAProxy picking no backend, or Kong matching no route? The `set-header Host` step is the likely place it is decided, since Kong matches on the hostname it expects.

## Done When

The FCM path answers end to end through a curl, and I can name which Kong matched the route.
