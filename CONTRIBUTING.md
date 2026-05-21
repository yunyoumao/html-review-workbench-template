# Contributing

Contributions are welcome if they keep the template dependency-free and public-safe.

Good contributions include:

- Better keyboard and screen-reader behavior.
- Cleaner responsive layout.
- New synthetic review templates.
- Validation rules and tests.

Before opening a pull request:

- Use fictional review data only.
- Do not commit private review notes, manuscript content, company names, local paths, or credentials.
- Run `python scripts/build_data_js.py`.
- Run `python -m unittest discover -s tests`.
- Run `python scripts/validate_public_assets.py`.
