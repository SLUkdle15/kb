# Clone Sheet Request Times Out on Serial HTTP Calls

Related project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]

One HTTP request triggers a series of HTTP requests — the clone action on an Excel sheet — and the original request returns a timeout.

Fixed by 2026-10-05 by replacing the fixed `A1:A100000` address with the open-ended `A:A` — recorded in [[projects/give-the-ai-chatbot-excel-tools/gotchas|Gotchas]].
