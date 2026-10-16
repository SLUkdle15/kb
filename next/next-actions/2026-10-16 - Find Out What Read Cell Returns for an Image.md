# Find Out What Read Cell Returns for an Image

Project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]
Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Put an image in a sheet and call the MCP read-cell tool on it, to see what comes back for a cell that holds a picture rather than a value.

Test both ways an image can sit in a sheet, because they are different objects to Graph: a floating picture anchored over a cell, and an in-cell image (`IMAGE()` or a pasted rich value). Note whether the cell reads back as empty, as text, as a URL, or as bytes.

If nothing usable comes back, record it in [[projects/give-the-ai-chatbot-excel-tools/gotchas|Gotchas]] as an architectural dead end — the chatbot then cannot see pictures in a sheet, and that shapes what the Excel tools can honestly promise.

## Done When

It is known and written down what the read-cell tool returns for each kind of image, so the answer does not have to be rediscovered.
