# ח. כהן - משרד עורכי דין · אתר

```
docs/      האתר שעולה לאוויר (GitHub Pages מפרסם את התיקייה הזו בכל push ל-main)
src/       סקריפט הבנייה, תוכן המקור ותמונות המקור
DESIGN.md  כיוון העיצוב וההחלטות
```

## docs/ - האתר
| כתובת | קובץ |
|---|---|
| `/` | `docs/index.html` |
| `/about/` · `/team/` · `/team/hagai-cohen/` · `/contact/` · `/en/` | `docs/<שם>/index.html` |
| `/areas/` ותחומים: `/areas/labor/`... | `docs/areas/` |
| `/articles/` ומאמרים: `/articles/mikvaot/`... | `docs/articles/` |
| דפי נושא: `/topics/...` | `docs/topics/` |
| מדיניות ונגישות: `/legal/privacy/`... | `docs/legal/` |
| עיצוב, סקריפטים, גופנים, תמונות | `docs/assets/` (נערך ידנית) |
| לגוגל: `robots.txt`, `sitemap.xml`, `404.html` | `docs/` |

עמודי ה-HTML נוצרים מהסקריפט. לא עורכים אותם ידנית.

## src/ - בנייה
| מה | איפה |
|---|---|
| סקריפט הבנייה | `src/build.py` |
| טקסטים מקוריים (האתר המקורי, cochag12/hcohen-law @ 846d57a) | `src/original-site/` |
| תמונות מקור (צוות, תמונות התחומים) | `src/photos/` |

```
python src/build.py
```
דורש Python 3 ו-`beautifulsoup4`. בראש `src/build.py`:
- `SITE` - כתובת האתר (https://www.h-cohen.com/). כל הקישורים הקנוניים, מפת האתר והמידע המובנה נבנים ממנה.
- `CONTENT_UPDATES`, `STATEMENT_UPDATES`, `TEAM_*` - שינויי טקסט שאושרו.
- `ORG_NAMES`, `FOUNDER_NAMES` - צורות השם שגוגל ומנועי AI מקבלים במידע המובנה.

## הוספת תמונה לעורך/ת דין
1. לשמור את המקור ב-`src/photos/<name>-original.jpg`.
2. לייצא ‎720×900‎ WebP אל `docs/assets/img/<name>-720.webp` (חיתוך קרוב, הפנים בגודל דומה לשאר).
3. להוסיף ל-`TEAM_PHOTOS` ב-`src/build.py` ולהריץ את הבנייה.
