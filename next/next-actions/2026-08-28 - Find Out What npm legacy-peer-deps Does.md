# Find Out What npm legacy-peer-deps Does

Area: [[areas/technical-growth/technical-growth|Technical Growth]]

## Action

Find out what `npm install --legacy-peer-deps` actually does, and when reaching for it is the right call versus papering over a real dependency conflict.

- What npm 7+ changed about peer dependencies, and why the flag exists.
- What it does to the resulting tree, and what breaks later when peers are genuinely incompatible.
- How it compares to `--force`, and to fixing the version range properly.

## Done When

I can say what the flag does and decide, on a given conflict, whether to use it or fix the versions.
