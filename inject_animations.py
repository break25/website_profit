import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Animations Block
css_animations = """
    /* --- ANIMATIONS --- */
    @media (prefers-reduced-motion: no-preference) {
      /* Hero background zooom */
      @keyframes heroZoom {
        0%, 100% { background-size: 100% auto; }
        50% { background-size: 108% auto; }
      }
      .hero {
        animation: heroZoom 16s ease-in-out infinite;
      }
      @media (max-width: 768px) {
        @keyframes heroZoomMobile {
          0%, 100% { background-size: auto 100%; }
          50% { background-size: auto 108%; }
        }
        .hero {
          animation: heroZoomMobile 16s ease-in-out infinite;
        }
      }

      /* Hero text fade in */
      @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
      }
      .hero-eyebrow, .hero-title, .hero-desc, .hero-cta {
        opacity: 0;
        animation: slideUpFade 0.8s ease-out forwards;
      }
      .hero-eyebrow { animation-delay: 0.5s; }
      .hero-title { animation-delay: 0.9s; }
      .hero-desc { animation-delay: 1.3s; }
      .hero-cta { animation-delay: 1.7s; }

      /* Nav logo shimmer */
      @keyframes goldShimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
      }
      .nav-logo {
        background: linear-gradient(90deg, var(--c-dark) 20%, var(--c-brown) 50%, var(--c-dark) 80%);
        background-size: 200% auto;
        color: transparent !important;
        -webkit-background-clip: text;
        background-clip: text;
        animation: goldShimmer 4s ease-in-out 1 forwards;
        animation-delay: 0.2s;
      }

      /* Menu scroll slide up */
      .menu-item.scroll-anim {
        opacity: 0;
        transform: translateY(15px);
      }
      .menu-item.scroll-anim.is-visible {
        opacity: 1;
        transform: translateY(0);
      }

      /* Feature items hover glow */
      .feature-item {
        transition: background 0.3s, box-shadow 0.4s ease-out;
      }
      .feature-item:hover {
        background: var(--c-cream);
        box-shadow: inset 0 0 40px rgba(200, 146, 42, 0.08);
      }
    }
"""

if "/* --- ANIMATIONS --- */" not in content:
    content = content.replace("  </style>", css_animations + "\n  </style>")


# JS IntersectionObserver Block
js_observer = """
    /* ── SCROLL ANIMATIONS ── */
    document.addEventListener("DOMContentLoaded", () => {
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.menu-item').forEach(el => {
          el.classList.add('scroll-anim');
          observer.observe(el);
        });
      }
    });
"""

if "/* ── SCROLL ANIMATIONS ── */" not in content:
    content = content.replace("  </script>", js_observer + "\n  </script>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected CSS and JS animations.")
