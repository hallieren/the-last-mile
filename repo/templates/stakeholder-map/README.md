# stakeholder-map

Corresponding template: Template 5, Stakeholder Map (companion: Chapter 5) ([full appendix](../../../docs/appendices/template-05-stakeholder-map.md)).
Purpose: a fillable scaffold for the six-role map, plus a script that reminds you when an update is more than two weeks overdue.

| File | What it is | How to use |
|------|--------|--------|
| `stakeholder-map.md` | The 5.1 main table, fillable, plus the fear/win prompt library and the two questions to answer once the map is drawn | Copy it, fill in real names; update the "Last updated" line every time you revise it |
| `remind.py` | Update reminder script: reads the map's "Last updated" line, prints a reminder once it is more than N days old | `python3 remind.py your-map.md [--days 14]`; with no arguments it demos on the sample |
| `sample/stakeholder-map.md` | A filled example (from the book's Anchor & Helm case) | Reference for how to fill it in; also the script's default input |
