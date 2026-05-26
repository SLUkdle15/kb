---
name: restaurant-kb
description: Create, update, query, and recommend from a personal restaurant knowledge base in this Obsidian vault. Use when the user asks to add a restaurant, record a visit, capture restaurant attributes, compare places, or decide what to eat based on constraints like area, budget, parking, date suitability, cuisine, mood, or past experience.
---

# Restaurant KB

Use this skill for restaurant notes and meal decisions.

## Inputs

- Restaurant name.
- Optional place or area.
- Optional URL, map link, menu link, or delivery link.
- Optional cuisine, price, parking, date suitability, group suitability, solo suitability, noise, reservation, hours, and past experience.
- Optional current decision constraints: area, budget, transport, meal type, craving, time, companions, avoid list.

## Storage

- Restaurant notes live in `resources/restaurants`.
- Area notes live in `resources/locations` when useful.
- Cuisine notes live in `resources/cuisines` when useful.
- Use lowercase folder names.
- Do not use topic tags. Record comparable traits as fields or bullets.

## Restaurant Note Shape

Create dated restaurant notes:

```md
# Restaurant Name

Cuisine: [[resources/cuisines/cuisine]]
Location: [[resources/locations/area]]
Map:
Website:
Menu:

## Attributes

- Price:
- Parking:
- Good for date:
- Good for solo:
- Good for group:
- Noise level:
- Reservation:
- Open late:
- Delivery:
- Revisit priority:

## Best For

- 

## Past Experience

Visited: YYYY-MM-DD

Ordered:
- 

Ratings:
- Food:
- Value:
- Atmosphere:
- Convenience:

Notes:
```

Omit unknown fields only when they add clutter. Prefer short, comparable values such as `cheap`, `mid`, `expensive`, `yes`, `no`, `limited`, `quiet`, `moderate`, `loud`, or a 1-10 rating.

## Workflow

1. Read `AGENTS.md` and `resources/restaurants/restaurants.md` if present.
2. If adding a restaurant, search existing restaurant notes first to avoid duplicates.
3. Create a note named `YYYY-MM-DD - Restaurant Name.md` in `resources/restaurants`.
4. Link cuisine and location notes when known. Create simple cuisine or location notes only when the link would be reused.
5. Add the restaurant to `resources/restaurants/restaurants.md`.
6. If recording a repeat visit, append a new dated entry under `## Past Experience` instead of replacing old experience.
7. If recommending what to eat, rank matching restaurants and explain the top choice from stored attributes and past experience.

## Recommendation Heuristics

When the user asks what to eat:

1. Identify hard constraints: area, budget, open now or date/time, transport, companion, dietary avoid list.
2. Identify soft preferences: craving, novelty, comfort, date mood, convenience, revisit priority.
3. Prefer restaurants with direct evidence from `Attributes` and `Past Experience`.
4. Penalize unknowns only when the constraint matters.
5. Return a short ranked list with a clear first pick and why.

If key decision context is missing, make a reasonable default and state it briefly. Ask a question only when the recommendation would be arbitrary.

## Guardrails

- Do not add tags for cuisine, price, location, or note type.
- Do not create a project for this workflow unless the user asks for a multi-step outcome.
- Do not store raw screenshots, PDFs, or exported menus in `resources`; put those under the proper `raw` subfolder and link them from the restaurant note.
- Keep notes useful for future comparison, not prose-heavy reviews.
