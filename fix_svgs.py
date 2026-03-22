import sys
import re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix hero CTA SVG
    content = content.replace(
        """    .hero-cta svg {
      width: 14px;
      transition: transform 0.3s;
    }""", 
        """    .hero-cta svg {
      width: 14px;
      height: 14px;
      flex-shrink: 0;
      transition: transform 0.3s;
    }"""
    )

    # Fix contact fab btn SVG
    content = content.replace(
        """    .contact-fab-btn svg {
      width: 22px;
      stroke: var(--c-bg);
    }""",
        """    .contact-fab-btn svg {
      width: 22px;
      height: 22px;
      flex-shrink: 0;
      stroke: var(--c-bg);
    }"""
    )
    
    # Strictly enforce SVGs in contact-row with inline attributes to be bulletproof
    content = content.replace(
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width:16px; height:16px; flex-shrink:0; display:block;">'
    )
    
    # Actually the hero CTA SVG might have gotten replaced by the above inline style because it shares the same viewBox!
    # Let's fix that if it happened. The hero CTA doesn't want 16px, it wants 14px.
    # But wait, .hero-cta svg CSS will override inline if we use !important, or let's not replace that globally.
    content = content.replace(
        """<a class="hero-cta" onclick="showPage('menu')">
          Explore the Menu
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width:16px; height:16px; flex-shrink:0; display:block;">""",
        """<a class="hero-cta" onclick="showPage('menu')">
          Explore the Menu
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width:14px; height:14px; flex-shrink:0; display:block;">"""
    )
    
    # The fab btn SVG:
    content = content.replace(
        """<button class="contact-fab-btn" id="contactBtn" onclick="toggleContact()" title="Contact us">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width:16px; height:16px; flex-shrink:0; display:block;">""",
        """<button class="contact-fab-btn" id="contactBtn" onclick="toggleContact()" title="Contact us">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width:22px; height:22px; flex-shrink:0; display:block;">"""
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed SVG explicit height/width constraints")
except Exception as e:
    print(e)
