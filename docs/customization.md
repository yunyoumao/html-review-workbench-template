# Customization

The JSON source of truth is:

```text
data/sample-review.json
```

Each item needs:

- `id`
- `title`
- `category`
- `severity`
- `status`
- `owner`
- `evidence`
- `next_step`

Supported severities:

- `High`
- `Medium`
- `Low`

Supported statuses:

- `Open`
- `In Progress`
- `Done`

After editing the JSON, run:

```powershell
python scripts\build_data_js.py
```

The generated `data/sample-review.js` lets the template work from `file://` without a local server.
