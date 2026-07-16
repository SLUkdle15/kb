---
name: restaurant
description: Create a new restaurant note in this Obsidian vault. Use when the user asks to add a restaurant or capture initial restaurant attributes such as area, cuisine, price, parking, date suitability, map link, or past experience.
---

# Create Restaurant

Use this skill only to create new restaurant notes.

## Inputs

- Restaurant name.
- Optional place or area.
- Optional URL, map link, menu link, or delivery link.
- Optional cuisine, price, parking, date suitability, group suitability, solo suitability, noise, reservation, hours, and past experience.

## Storage

- Restaurant notes live in `resources/restaurants`.
- Use lowercase folder names.
- Do not use topic tags. Record comparable traits as fields or bullets.

## Restaurant Note Shape

Create dated restaurant notes:

```md
# Restaurant Name

Cuisine:
Location:
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
2. Search existing restaurant notes first to avoid duplicates.
3. Create a note named `YYYY-MM-DD - Restaurant Name.md` in `resources/restaurants`.
4. Use plain cuisine and location fields unless the user asks to create separate notes for them.
5. Add the restaurant to `resources/restaurants/restaurants.md`.
6. If the restaurant already exists, do not update it; report the existing note path instead.

## Guardrails

- Do not add tags for cuisine, price, location, or note type.
- Do not create a project for this workflow unless the user asks for a multi-step outcome.
- Do not store raw screenshots, PDFs, or exported menus in `resources`; put those under the proper `raw` subfolder and link them from the restaurant note.
- Keep notes useful for future comparison, not prose-heavy reviews.
- Do not update existing restaurant notes, append repeat visits, compare restaurants, or recommend what to eat.
