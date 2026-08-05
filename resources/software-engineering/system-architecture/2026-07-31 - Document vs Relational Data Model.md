---
type: distilled-note
---

# Document vs Relational Data Model

The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some applications it is closer to the data structures used by the application. The relational model counters by providing better support for joins, and many-to-one and many-to-many relationships.

Which data model leads to simpler application code?
Schema flexibility
	- Schema-on-read is similar to dynamic (runtime) type checking in programming languages, whereas schema-on-write is similar to static (compile-time) type checking.

The advantage of using an ID is that because it has no meaning to humans, it never needs to change.
