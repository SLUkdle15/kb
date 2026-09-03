---
type: distilled-note
---

# npm legacy-peer-deps Ignores Peer Dependencies

**Why you need it:** an unmaintained package declares a stale peer range that no longer matches your app, and no version arrangement satisfies everyone. The flag says "I've decided this is fine."

**Example:** on npm 10.9.8, `react-diff-viewer@3.1.1` peers React 15/16 while the app runs React 18, so `npm install` fails with `ERESOLVE`. With the flag it installs and the library uses the React 18 already there.

**Why npm can't just nest both:** normally npm resolves a version conflict by giving each package its own nested copy. React is an exception — hooks and context live in module-level state, so components from one copy can't render inside another. There's no working two-version arrangement, which is why npm errors instead of nesting.

So once the tree is resolved there's a single copy, and every library gets it regardless of what its peer range said. `import React from 'react'` inside `react-diff-viewer` returns React 18. The mismatch only matters if the library calls an API that major removed.
