import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update :root
html = html.replace("--font-display: 'Playfair Display', serif;", "--font-display: 'Cormorant Garamond', serif;")
html = html.replace("--font-body: 'Inter', sans-serif;", "--font-body: 'DM Sans', sans-serif;")

# 2. Update Font Link
# The exact string in index.html for fonts
old_link = "family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap"
new_link = "family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500&family=Libre+Baskerville:ital@1&display=swap"
html = html.replace(old_link, new_link)

# 3. Add font-weight: 300 to all font-family: var(--font-display)
def replace_weight(m):
    block = m.group(0)
    if re.search(r'font-weight:\s*\d00;', block):
        block = re.sub(r'font-weight:\s*\d00;', 'font-weight: 300;', block)
    else:
        block = block.replace("font-family: var(--font-display);", "font-family: var(--font-display);\n      font-weight: 300;")
    return block

html = re.sub(r'\{[^{}]*font-family:\s*var\(--font-display\);[^{}]*\}', replace_weight, html)

# 4. Hero Title font size
html = re.sub(
    r'(\.hero-title\s*\{[^}]*)font-size:\s*clamp\(3rem,\s*6vw,\s*5\.5rem\);',
    r'\g<1>font-size: clamp(3.5rem, 7vw, 6.5rem);',
    html
)

# 5. Remove Menu Price ::after
menu_after_css = """    .menu-item-price::after {
      content: '—';
      color: #C8922A;
      opacity: 0.5;
    }"""
html = html.replace(menu_after_css, "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
