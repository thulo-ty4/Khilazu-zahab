import os
import re

# Dossier contenant les fichiers HTML
folder = '.'

# Fonction pour améliorer un fichier HTML
def improve_html(file_path):
    # Déduire le titre depuis le nom du fichier
    filename = os.path.basename(file_path)
    match = re.search(r'(\d+)', filename)
    chapter_number = match.group(1) if match else ""
    chapter_title = f"الفصل {chapter_number} في ذكر"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire le contenu du <body>
    start = content.find('<body>')
    end = content.find('</body>')
    body_content = content[start+6:end].strip() if start != -1 and end != -1 else content

    # Nettoyer et transformer les <p> et <span>
    body_content = re.sub(r'<p[^>]*>.*?<span[^>]*>(.*?)</span>.*?</p>', r'<p class="verse">\1</p>', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<br\s*/?>', '\n', body_content)  # remplacer <br> par saut de ligne

    # Construire le HTML amélioré
    improved = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<meta name="google-adsense-account" content="ca-pub-4368298895659451">
<title>{chapter_title}</title>
<style>
  body {{
    font-family: 'Times New Roman', serif;
    background: #f9f9f9;
    color: #111;
    text-align: center;
    line-height: 1.6;
    padding: 20px;
    margin: 0;
  }}
  .chapter {{
    max-width: 800px;
    margin: auto;
    background: #fff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }}
  .chapter h2 {{
    font-size: 28px;
    margin-bottom: 20px;
    color: #2c3e50;
  }}
  .verse {{
    font-size: 18pt;
    margin: 15px 0;
    line-height: 1.5;
    color: #333;
    font-weight: bold;
    white-space: pre-line;
  }}
  .separator {{
    margin: 25px 0;
    font-size: 20pt;
    font-weight: bold;
    color: #555;
  }}
  @media screen and (max-width: 600px) {{
    .chapter {{ padding: 20px; }}
    .chapter h2 {{ font-size: 22px; }}
    .verse {{ font-size: 16pt; }}
  }}
</style>
</head>
<body>
<div class="chapter">
<h2>{chapter_title}</h2>
{body_content}
</div>
</body>
</html>
"""

    # Écrire le fichier amélioré
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(improved)
    print(f"{filename} amélioré ✅")

# Parcourir tous les fichiers HTML du dossier
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        improve_html(os.path.join(folder, filename))
