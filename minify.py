import os

html_file = r"c:\Users\prash\OneDrive\Desktop\Prashant Projects\index.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Images to WebP with width/height/lazy loading
html = html.replace('src="b.jpg" alt="Logo"', 'src="b.webp" alt="Logo" width="54" height="54" fetchpriority="high" decoding="async"')
html = html.replace('src="a.jpg" alt="Prashant Prajapati"', 'src="a.webp" alt="Prashant Prajapati" width="1467" height="1832" loading="lazy" decoding="async"')
html = html.replace('src="b.jpg" alt="Prashant Prajapati"', 'src="b.webp" alt="Prashant Prajapati" width="640" height="640" loading="lazy" decoding="async"')
html = html.replace('src="yt-logo.jpg"', 'src="yt-logo.webp" width="1024" height="1024" loading="lazy" decoding="async"')

# 2. Add Preload for b.webp
if '<link rel="preload" as="image" href="b.webp">' not in html:
    html = html.replace('</title>\n', '</title>\n<link rel="preload" as="image" href="b.webp">\n')

# 3. Optimize Google Fonts
html = html.replace('family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600', 'family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap')
html = html.replace('family=Poppins:wght@300;400;500;600;700"', 'family=Poppins:wght@300;400;500;600;700&display=swap"')
if '&display=swap&display=swap' in html: html = html.replace('&display=swap&display=swap', '&display=swap')

# 4. GPU Acceleration
html = html.replace('.particle{position:fixed;', '.particle{will-change:transform,opacity;position:fixed;')
html = html.replace('.spin-border::before{\n  content:\'\';', '.spin-border::before{\n  content:\'\';\n  will-change:transform;')
html = html.replace('.avatar-3d{position:relative;', '.avatar-3d{position:relative;will-change:transform;')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Safe optimizations applied to index.html successfully.")
