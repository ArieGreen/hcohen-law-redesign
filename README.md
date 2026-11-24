# ח. כהן - משרד עורכי דין · אתר

```
site/      האתר שעולה לאוויר (מתפרסם אוטומטית בכל push ל-main)
src/       סקריפט הבנייה, תוכן המקור ותמונות המקור
DESIGN.md  כיוון העיצוב וההחלטות
```

## site/ - האתר
| כתובת | קובץ |
|---|---|
| `/` | `site/index.html` |
| `/about/` · `/team/` · `/team/hagai-cohen/` · `/contact/` · `/en/` | `site/<שם>/index.html` |
| `/areas/` ותחומים: `/areas/labor/`... | `site/areas/` |
| `/articles/` ומאמרים: `/articles/mikvaot/`... | `site/articles/` |
| דפי נושא: `/topics/...` | `site/topics/` |
| מדיניות ונגישות: `/legal/privacy/`... | `site/legal/` |
| עיצוב, סקריפטים, גופנים, תמונות | `site/assets/` (נערך ידנית) |
| לגוגל: `robots.txt`, `sitemap.xml`, `404.html` | `site/` |

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
- `SITE` - כתובת האתר. כשהדומיין יחובר, משנים כאן שורה אחת ובונים מחדש.
- `CONTENT_UPDATES`, `STATEMENT_UPDATES`, `TEAM_*` - שינויי טקסט שאושרו.
- `ORG_NAMES`, `FOUNDER_NAMES` - צורות השם שגוגל ומנועי AI מקבלים במידע המובנה.

## הוספת תמונה לעורך/ת דין
1. לשמור את המקור ב-`src/photos/<name>-original.jpg`.
2. לייצא ‎720×900‎ WebP אל `site/assets/img/<name>-720.webp` (חיתוך קרוב, הפנים בגודל דומה לשאר).
3. להוסיף ל-`TEAM_PHOTOS` ב-`src/build.py` ולהריץ את הבנייה.
