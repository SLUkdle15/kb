---
name: restaurant
description: Create a new restaurant note in this Obsidian vault. Use when the user asks to add a restaurant or capture initial restaurant attributes such as area, cuisine, price, parking, date suitability, map link, or past experience.
---

# Create Restaurant

Use this skill only to create new restaurant notes.

## Inputs

- Restaurant name.
- Price bracket and revisit priority (required — ask if not given; see Workflow).
- Optional place or area.
- Optional URL or map link.
- Optional cuisine, parking, date suitability, hours, and past experience.

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

## Attributes

- Price:
- Parking:
- Good for date:
- Open late:
- Revisit priority:

## Best For

- 

## Past Experience

Visited: YYYY-MM-DD

Ordered:
- 

- Food rating:

Notes:
```

Prefer short, comparable values such as `cheap`, `mid`, `expensive`, `yes`, `no`, `limited`, or a 1-10 rating.

Add extra fields (website, menu, noise level, reservation, delivery, group/solo suitability, more ratings) only when the user provides a value for them — never as empty placeholders.

## Workflow

1. Read `AGENTS.md` and `resources/restaurants/restaurants.md` if present.
2. Search existing restaurant notes first to avoid duplicates.
3. If the capture does not include a price bracket (`cheap` / `mid` / `expensive`) and a revisit priority (1-10), ask for them before saving — these two fields drive meal decisions and are only reliably known right after a visit. If the user declines or does not answer, save the note anyway and say which fields are still empty.
4. Create a note named `YYYY-MM-DD - Restaurant Name.md` in `resources/restaurants`.
5. Use plain cuisine and location fields unless the user asks to create separate notes for them.
6. Add the restaurant to `resources/restaurants/restaurants.md`.
7. If the restaurant already exists, do not update it; report the existing note path instead.

## Guardrails

- Do not add tags for cuisine, price, location, or note type.
- Do not create a project for this workflow unless the user asks for a multi-step outcome.
- Do not store raw screenshots, PDFs, or exported menus in `resources`; put those under the proper `raw` subfolder and link them from the restaurant note.
- Keep notes useful for future comparison, not prose-heavy reviews.
- Do not update existing restaurant notes, append repeat visits, compare restaurants, or recommend what to eat.
