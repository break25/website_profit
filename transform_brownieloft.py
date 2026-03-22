import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Global Rename "Maison" to "The Brownie Loft"
# Doing this globally is safe except perhaps "maison-website" if it occurs in path, but it doesn't in index.html content.
content = content.replace("Maison", "The Brownie Loft")
content = content.replace("hello@maisonbakery.in", "hello@brownieloft.in")
content = content.replace('<div class="hero-big-glyph">M</div>', '<div class="hero-big-glyph">B</div>')
content = content.replace('<span class="hero-badge-inner">M</span>', '<span class="hero-badge-inner">B</span>')

# 2. Hero Tagline
old_tagline = "Small-batch pastries, single-origin coffees, and slow breakfasts made from locally sourced ingredients. A place to pause and savour."
new_tagline = "Handcrafted brownies & cheesecakes. Made with obsession."
content = content.replace(old_tagline, new_tagline)

# 3. Hero Background & Overlay
content = content.replace(
    "background: url('https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=2000&auto=format&fit=crop') center/cover no-repeat;",
    "background: url('https://images.unsplash.com/photo-1564355808539-22fda35bed7e?q=80&w=2000&auto=format&fit=crop') center/cover no-repeat;"
)

content = content.replace(
    "background: linear-gradient(to right, rgba(253,246,236,0.95) 0%, rgba(253,246,236,0.7) 50%, rgba(253,246,236,0.1) 100%);",
    "background: rgba(0, 0, 0, 0.65);"
)
content = content.replace(
    "background: linear-gradient(to bottom, rgba(253,246,236,0.95) 0%, rgba(253,246,236,0.85) 60%, rgba(253,246,236,0.4) 100%);",
    "background: rgba(0, 0, 0, 0.65);"
)

# 4. CSS Variables
css_vars_old = '''    :root {
      --brand-name: "The Brownie Loft";
      --c-bg:        #FDF6EC;
      --c-cream:     #F3E3D3;
      --c-parchment: #ecdcc8;
      --c-taupe:     #A68A64;
      --c-brown:     #6A4E36;
      --c-dark:      #3B2314;
      --c-muted:     #9c8670;
      --c-white:     #fffcf8;'''

css_vars_new = '''    :root {
      --brand-name: "The Brownie Loft";
      --c-bg:        #1C0F0A;
      --c-cream:     #2C1A12;
      --c-parchment: #3D2314;
      --c-taupe:     #C8922A;
      --c-brown:     #C8922A;
      --c-dark:      #F5ECD7;
      --c-muted:     #D4C4A8;
      --c-white:     #2C1A12;'''
content = content.replace(css_vars_old, css_vars_new)

# Note: In the previous edit, we set `<title>Maison · A Café & Bakery</title>`, since Maison mapped to The Brownie Loft, it became `<title>The Brownie Loft · A Café & Bakery</title>`.

# Add Typography Explicit Gold for headings
heading_css = '''
    h1, h2, h3, h4, h5, h6, .hero-title, .section-title, .menu-section-head h3, .menu-item-name, .hero-big-glyph, .hero-badge-inner, .about-art, .feature-title, .stat-num, .team-name {
      color: var(--c-brown) !important;
    }
'''
if heading_css not in content:
    content = content.replace("  </style>", heading_css + "\n  </style>")

# Update Navbar Link Hover Line
content = content.replace("background: rgba(253, 248, 243, 0.92);", "background: rgba(28, 15, 10, 0.92);") # Fix navbar BG

# Fix quotes colors and hero text explicitly
content = content.replace("color: var(--c-dark);", "color: var(--c-dark);") # Text defaults to F5ECD7 now
# but we have `<div class="hero-left">`, some text has inline `color:`.
# We want to replace `rgba(253,248,243,0.5)` with `rgba(245, 236, 215, 0.5)` for footer text
content = content.replace("rgba(253,248,243,0.5)", "rgba(245,236,215,0.5)")

# Replace Food Menu Details HTML
menu_html_start = content.find("    <!-- Pastries & Bread -->")
menu_html_end = content.find("  </div><!-- /menu-grid -->")

if menu_html_start != -1 and menu_html_end != -1:
    new_food_menu = '''    <!-- Brownies -->
    <div>
      <div class="menu-section-head"><h3>Brownies</h3></div>
      <div class="menu-items">
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Classic Dark Brownie</div>
            <div class="menu-item-desc">70% Valrhona chocolate, sea salt flakes</div>
          </div>
          <div class="menu-item-price">₹ 220</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Lotus Biscoff Brownie</div>
            <div class="menu-item-desc">Crushed biscoff swirl, caramel drizzle</div>
          </div>
          <div class="menu-item-price">₹ 260</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Walnut Fudge Brownie</div>
            <div class="menu-item-desc">Dense, chewy, double chocolate</div>
          </div>
          <div class="menu-item-price">₹ 240</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Brownie Sundae</div>
            <div class="menu-item-desc">Warm brownie, vanilla bean ice cream, hot fudge</div>
          </div>
          <div class="menu-item-price">₹ 320</div>
        </div>
      </div>
    </div>

    <!-- Cheesecakes -->
    <div>
      <div class="menu-section-head"><h3>Cheesecakes</h3></div>
      <div class="menu-items">
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Basque Burnt Cheesecake</div>
            <div class="menu-item-desc">Caramelised top, soft molten centre</div>
          </div>
          <div class="menu-item-price">₹ 280</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Blueberry Cheesecake</div>
            <div class="menu-item-desc">Biscuit base, fresh blueberry compote</div>
          </div>
          <div class="menu-item-price">₹ 300</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">Lotus Biscoff Cheesecake</div>
            <div class="menu-item-desc">No-bake, biscoff crust, cold served</div>
          </div>
          <div class="menu-item-price">₹ 320</div>
        </div>
        <div class="menu-item">
          <div class="menu-item-info">
            <div class="menu-item-name">New York Classic</div>
            <div class="menu-item-desc">Dense, creamy, graham cracker crust</div>
          </div>
          <div class="menu-item-price">₹ 260</div>
        </div>
      </div>
    </div>
'''
    content = content[:menu_html_start] + new_food_menu + content[menu_html_end:]

# Replace the specific drinks CSS
content = content.replace("photo-1495474472201-41dbd4a0a7d9", "photo-1495474472287-4d71bcdd2085") # Filter Coffee
content = content.replace("photo-1541795742398-466ee50a2de4", "photo-1571934811356-5cc061b6821f") # Turmeric Latte

# Strip old Food CSS rules and insert new ones
old_food_css_start = content.find("/* Pastries */")
old_food_css_end = content.find("'''", old_food_css_start) # Wait, my earlier script injected it into index.html without `'''` - so let's find end of `<style>` or just use regex

if old_food_css_start != -1:
    end_of_style = content.find("</style>", old_food_css_start)
    new_food_css = '''/* Brownies */
    .menu-grid > div:nth-child(2) .menu-item:nth-child(1)::before { background-image: url('https://images.unsplash.com/photo-1564355808539-22fda35bed7e?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(2)::before { background-image: url('https://images.unsplash.com/photo-1558961363-fa8fdf82db35?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(3)::before { background-image: url('https://images.unsplash.com/photo-1606313564200-e75d5e30476c?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(4)::before { background-image: url('https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=200&auto=format&fit=crop'); }

    /* Cheesecakes */
    .menu-grid > div:nth-child(3) .menu-item:nth-child(1)::before { background-image: url('https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(2)::before { background-image: url('https://images.unsplash.com/photo-1565958011703-44f9829ba187?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(3)::before { background-image: url('https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(4)::before { background-image: url('https://images.unsplash.com/photo-1524351199678-941a58a3df50?q=80&w=200&auto=format&fit=crop'); }
'''
    content = content[:old_food_css_start] + new_food_css + heading_css + "\n  " + content[end_of_style:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated perfectly.")
