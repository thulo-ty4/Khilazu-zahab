import os

# Ton code Adsense
meta_tag = '<meta name="google-adsense-account" content="ca-pub-4368298895659451">'

# Parcours tous les fichiers du projet
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Vérifie si déjà présent
            if meta_tag in content:
                continue

            # Insère avant </head>
            if "</head>" in content:
                new_content = content.replace("</head>", f"    {meta_tag}\n</head>")
            else:
                new_content = meta_tag + "\n" + content

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"✅ Meta ajouté dans {path}")
