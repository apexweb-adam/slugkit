# slugkit

Tiny URL slug helper. It ships with a **known bug on purpose**: it is the demo target for
[RepoMedic](https://github.com/apexweb-adam/repomedic), an agent that turns a GitHub issue into a patch that passes the
repository's own tests.

```python
from slugkit import slugify
slugify("Crème Brûlée -- Recipe")   # buggy: 'crème-brûlée----recipe', expected 'creme-brulee-recipe'
```

Run the tests (3 of 5 fail until the bug is fixed):

```bash
python -m pytest -q
```

See [ISSUE.md](ISSUE.md) for the bug report that RepoMedic is pointed at. MIT licensed.
