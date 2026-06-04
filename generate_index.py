import os
from pathlib import Path
from datetime import datetime

def generate_index():
    base_dir = Path(".")
    results_dir = base_dir / "results"
    
    if not results_dir.exists():
        print("Fehler: Der Ordner 'results' wurde nicht gefunden.")
        return

    # Alle HTML-Dateien im results-Ordner (und Unterordnern) finden
    html_files = sorted(results_dir.rglob("*.html"))
    
    # Nach übergeordnetem Verzeichnis gruppieren
    grouped_files = {}
    for filepath in html_files:
        # Relativen Pfad zum Basisverzeichnis ermitteln
        rel_path = filepath.relative_to(base_dir)
        parent_dir = rel_path.parent.name
        
        if parent_dir not in grouped_files:
            grouped_files[parent_dir] = []
        grouped_files[parent_dir].append({
            "name": filepath.name,
            "path": str(rel_path).replace("\\", "/") # Für Windows/Linux Kompatibilität
        })

    # HTML-Inhalt generieren
    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bachelorarbeit Reports</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --text-color: #f8fafc;
            --card-bg: #1e293b;
            --card-hover: #334155;
            --accent: #3b82f6;
            --accent-hover: #60a5fa;
            --border: #334155;
        }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 2rem;
            line-height: 1.5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border);
        }}
        h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        p.subtitle {{
            color: #94a3b8;
            font-size: 1.1rem;
        }}
        .category {{
            margin-bottom: 3rem;
            background: rgba(30, 41, 59, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--border);
        }}
        .category-title {{
            font-size: 1.5rem;
            margin-top: 0;
            margin-bottom: 1.5rem;
            color: #e2e8f0;
            border-left: 4px solid var(--accent);
            padding-left: 1rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1rem;
        }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.25rem;
            text-decoration: none;
            color: var(--text-color);
            transition: all 0.2s ease-in-out;
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        .card:hover {{
            background: var(--card-hover);
            transform: translateY(-2px);
            border-color: var(--accent);
            box-shadow: 0 8px 12px -3px rgba(0, 0, 0, 0.2);
        }}
        .card-title {{
            font-weight: 500;
            word-break: break-all;
        }}
        .card-icon {{
            color: var(--accent);
            flex-shrink: 0;
        }}
        footer {{
            margin-top: 4rem;
            text-align: center;
            color: #64748b;
            font-size: 0.9rem;
        }}
        @media (max-width: 600px) {{
            body {{ padding: 1rem; }}
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <header>
            <h1>Bachelorarbeit Reports</h1>
            <p class="subtitle">Übersicht aller generierten HTML-Ergebnisse und Metriken</p>
        </header>

"""

    for category, files in sorted(grouped_files.items()):
        html_content += f'        <div class="category">\n'
        html_content += f'            <h2 class="category-title">{category}</h2>\n'
        html_content += f'            <div class="grid">\n'
        
        for f in files:
            icon = '''<svg class="card-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'''
            
            html_content += f'''                <a href="{f['path']}" class="card">
                    {icon}
                    <span class="card-title">{f['name']}</span>
                </a>\n'''
                
        html_content += f'            </div>\n'
        html_content += f'        </div>\n'

    if not grouped_files:
        html_content += '        <p style="text-align:center; color:#94a3b8;">Keine HTML-Reports im Ordner <code>results/</code> gefunden.</p>\n'

    generation_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    html_content += f"""
        <footer>
            Zuletzt aktualisiert am {generation_time}
        </footer>
    </div>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Erfolgreich index.html generiert! {len(html_files)} Reports in {len(grouped_files)} Kategorien gefunden.")

if __name__ == "__main__":
    generate_index()
