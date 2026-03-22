import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Fonts
content = re.sub(
    r'<link href=\"https://fonts.googleapis.com/css2[^>]+>',
    '<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap\" rel=\"stylesheet\">',
    content
)

# Update CSS variables
content = content.replace('\'Cormorant Garamond\', serif', '\'Playfair Display\', serif')
content = content.replace('\'Jost\', sans-serif', '\'Inter\', sans-serif')
content = content.replace('--c-bg:        #fdf8f3;', '--c-bg:        #FDF6EC;')
content = content.replace('--c-dark:      #2e1f0f;', '--c-dark:      #3B2314;')
content = content.replace('--c-brown:     #7a5c3e;', '--c-brown:     #6A4E36;') # Slightly adjusting brown to match the new dark
content = content.replace('--c-taupe:     #c4a882;', '--c-taupe:     #A68A64;')
content = content.replace('--c-cream:     #f5ede0;', '--c-cream:     #F3E3D3;')

# Full width hero
hero_css_old = '''    .hero {
      min-height: calc(100vh - var(--nav-h));
      display: grid;
      grid-template-columns: 1fr 1fr;
      position: relative;
      overflow: hidden;
    }'''
hero_css_new = '''    .hero {
      min-height: calc(100vh - var(--nav-h));
      display: flex;
      align-items: center;
      position: relative;
      overflow: hidden;
      background: url('https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=2000&auto=format&fit=crop') center/cover no-repeat;
    }
    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(253,246,236,0.95) 0%, rgba(253,246,236,0.7) 50%, rgba(253,246,236,0.1) 100%);
      z-index: 1;
    }
    @media (max-width: 768px) {
      .hero::before {
        background: linear-gradient(to bottom, rgba(253,246,236,0.95) 0%, rgba(253,246,236,0.85) 60%, rgba(253,246,236,0.4) 100%);
      }
    }'''
content = content.replace(hero_css_old, hero_css_new)

hero_right_css_old = '''    .hero-right {
      position: relative;
      background: var(--c-cream);
      overflow: hidden;
    }'''
hero_right_css_new = '''    .hero-right {
      display: none;
    }'''
content = content.replace(hero_right_css_old, hero_right_css_new)

hero_left_css_old = '''    .hero-left {
      display: flex; flex-direction: column;
      justify-content: center;
      padding: 8vw 5vw 8vw 8vw;
      position: relative;
      z-index: 2;
    }'''
hero_left_css_new = '''    .hero-left {
      display: flex; flex-direction: column;
      justify-content: center;
      padding: 8vw 5vw 8vw 8vw;
      position: relative;
      z-index: 2;
      max-width: 650px;
    }'''
content = content.replace(hero_left_css_old, hero_left_css_new)


# Smooth hover effects on buttons and menu items
menu_item_css_old = '''    .menu-item {
      padding: 1.4rem 0;
      border-bottom: 1px solid var(--c-cream);
      display: flex; justify-content: space-between; align-items: start;
      gap: 1rem;
      transition: padding-left 0.3s;
      cursor: default;
    }

    .menu-item:hover { padding-left: 0.5rem; }'''

menu_item_css_new = '''    .menu-item {
      padding: 1.4rem;
      border-bottom: 1px solid var(--c-cream);
      border-radius: 12px;
      display: flex; justify-content: space-between; align-items: center;
      gap: 1.5rem;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      background: transparent;
      border: 1px solid transparent;
      margin-bottom: 0.5rem;
    }

    .menu-item:hover {
      background: var(--c-white);
      border-color: var(--c-parchment);
      box-shadow: 0 12px 36px rgba(59, 35, 20, 0.06);
      transform: translateY(-3px) scale(1.01);
      padding-left: 1.8rem;
    }
    
    .menu-item::before {
      content: '';
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background-size: cover;
      background-position: center;
      flex-shrink: 0;
      box-shadow: 0 4px 12px rgba(59,35,20,0.12);
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
      background-color: var(--c-cream);
    }
    
    .menu-item:hover::before {
      transform: scale(1.08) rotate(4deg);
    }

    /* Assigning food photos using nth-child selectors */
    /* Drinks */
    .menu-grid > div:nth-child(1) .menu-item:nth-child(1)::before { background-image: url('https://images.unsplash.com/photo-1495474472201-41dbd4a0a7d9?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(1) .menu-item:nth-child(2)::before { background-image: url('https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(1) .menu-item:nth-child(3)::before { background-image: url('https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(1) .menu-item:nth-child(4)::before { background-image: url('https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(1) .menu-item:nth-child(5)::before { background-image: url('https://images.unsplash.com/photo-1541795742398-466ee50a2de4?q=80&w=200&auto=format&fit=crop'); }
    
    /* Pastries */
    .menu-grid > div:nth-child(2) .menu-item:nth-child(1)::before { background-image: url('https://images.unsplash.com/photo-1517433670267-08bbd4be890f?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(2)::before { background-image: url('https://images.unsplash.com/photo-1601000938259-9e92002320b2?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(3)::before { background-image: url('https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(2) .menu-item:nth-child(4)::before { background-image: url('https://images.unsplash.com/photo-1509365465985-25d11c17e812?q=80&w=200&auto=format&fit=crop'); }

    /* Plates */
    .menu-grid > div:nth-child(3) .menu-item:nth-child(1)::before { background-image: url('https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(2)::before { background-image: url('https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(3)::before { background-image: url('https://images.unsplash.com/photo-1525351484163-7529414344d8?q=80&w=200&auto=format&fit=crop'); }
    .menu-grid > div:nth-child(3) .menu-item:nth-child(4)::before { background-image: url('https://images.unsplash.com/photo-1519915028121-7d3463d20b13?q=80&w=200&auto=format&fit=crop'); }
'''
content = content.replace(menu_item_css_old, menu_item_css_new)

hero_cta_old = '''    .hero-cta {
      display: inline-flex; align-items: center; gap: 0.75rem;
      background: var(--c-dark);
      color: var(--c-white);
      padding: 0.85rem 2rem;
      font-family: var(--font-body);
      font-size: 0.7rem;
      font-weight: 300;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: pointer;
      border: none;
      transition: background 0.3s, transform 0.2s;
      text-decoration: none;
    }

    .hero-cta:hover { background: var(--c-brown); transform: translateY(-1px); }'''

hero_cta_new = '''    .hero-cta {
      display: inline-flex; align-items: center; gap: 0.75rem;
      background: var(--c-dark);
      color: var(--c-white);
      padding: 0.85rem 2rem;
      font-family: var(--font-body);
      font-size: 0.7rem;
      font-weight: 400;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: pointer;
      border: none;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      text-decoration: none;
      border-radius: 4px;
      box-shadow: 0 4px 15px rgba(59,35,20,0.2);
    }

    .hero-cta:hover { 
      background: var(--c-brown); 
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(59,35,20,0.3);
    }'''

content = content.replace(hero_cta_old, hero_cta_new)

# Apply responsive fix for the larger menu item padding
media_query_old = '''    @media (max-width: 768px) {
      .hero { grid-template-columns: 1fr; }
      .hero-right { min-height: 40vw; }
      .features { grid-template-columns: 1fr; }
      .feature-item { border-right: none; border-bottom: 1px solid var(--c-parchment); }
      .about-split { grid-template-columns: 1fr; }
      .about-stats { grid-template-columns: 1fr 1fr; }
      .team-grid { grid-template-columns: 1fr 1fr; }
      .menu-items { grid-template-columns: 1fr; }
    }'''

media_query_new = '''    @media (max-width: 768px) {
      .hero { grid-template-columns: 1fr; }
      .hero-right { min-height: 40vw; }
      .features { grid-template-columns: 1fr; }
      .feature-item { border-right: none; border-bottom: 1px solid var(--c-parchment); }
      .about-split { grid-template-columns: 1fr; }
      .about-stats { grid-template-columns: 1fr 1fr; }
      .team-grid { grid-template-columns: 1fr 1fr; }
      .menu-items { grid-template-columns: 1fr; }
      
      .menu-item {
        flex-direction: column;
        align-items: flex-start;
        padding: 1.2rem;
      }
      .menu-item:hover {
        padding-left: 1.2rem;
        transform: translateY(-2px);
      }
      .menu-item::before {
        width: 100%;
        height: 180px;
        border-radius: 8px;
        margin-bottom: 0.5rem;
      }
      .menu-item-info {
        width: 100%;
      }
    }'''

content = content.replace(media_query_old, media_query_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
