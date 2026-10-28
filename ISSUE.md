# slugify() keeps accents and produces repeated dashes
`slugify("Crème Brûlée -- Recipe")` returns `crème-brûlée----recipe`.

Expected `creme-brulee-recipe`: accents should be transliterated to ASCII, and runs of spaces, dashes or underscores should collapse into a single separator. This breaks our blog URLs for every French and Hungarian title.
