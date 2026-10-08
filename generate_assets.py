import os
import base64
from PIL import Image
import io

def get_base64_png(path, size=None):
    im = Image.open(path)
    if size:
        im = im.resize(size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

id_b64 = get_base64_png('assets/id.png', (520, 520))
pointing_b64 = get_base64_png('assets/right_pointing.png', (520, 520))

# -------------------------------------------------------------
# 1. HERO SVG (DARK THEME)
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 390" width="100%" height="100%">
  <defs>
    <linearGradient id="heroDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#141E33"/>
    </linearGradient>
    <linearGradient id="heroDarkBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312E81"/>
      <stop offset="50%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#818CF8"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>
    <linearGradient id="avatarDarkGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="tagDarkBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="cardGlow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <filter id="avatarNeon" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#6366F1" flood-opacity="0.35"/>
    </filter>
    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .pulse-dot {{ animation: pulseDot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
      .float-badge {{ animation: floatY 4s ease-in-out infinite; }}
      .avatar-wrap {{ animation: subtleFloat 6s ease-in-out infinite; }}
      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(0.9); }}
      }}
      @keyframes floatY {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-5px); }}
      }}
      @keyframes subtleFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-4px); }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .pulse-dot, .float-badge, .avatar-wrap {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Main Dark Card -->
  <rect x="10" y="10" width="900" height="370" rx="24" fill="url(#heroDarkBg)" stroke="url(#heroDarkBorder)" stroke-width="1.5" filter="url(#cardGlow)"/>

  <!-- Ambient Star/Grid Dots -->
  <g opacity="0.3">
    <circle cx="80" cy="50" r="1.5" fill="#818CF8"/>
    <circle cx="120" cy="50" r="1.5" fill="#818CF8"/>
    <circle cx="160" cy="50" r="1.5" fill="#818CF8"/>
    <circle cx="80" cy="80" r="1.5" fill="#818CF8"/>
    <circle cx="120" cy="80" r="1.5" fill="#818CF8"/>
    <circle cx="160" cy="80" r="1.5" fill="#818CF8"/>
  </g>

  <!-- Left Content Column -->
  <!-- Status Pill -->
  <g transform="translate(48, 42)">
    <rect x="0" y="0" width="300" height="30" rx="15" fill="#064E3B" fill-opacity="0.6" stroke="#059669" stroke-width="1"/>
    <circle cx="15" cy="15" r="4.5" fill="#34D399" class="pulse-dot"/>
    <text x="28" y="19" class="font-sans" font-size="11" font-weight="700" fill="#6EE7B7" letter-spacing="0.5">OPEN TO OPPORTUNITIES • DEVELOPER</text>
  </g>

  <!-- Greeting & Headline -->
  <g transform="translate(48, 118)">
    <text x="0" y="0" class="font-sans" font-size="35" font-weight="800" fill="#FFFFFF" letter-spacing="-0.8">
      Hi, I'm <tspan fill="url(#textGrad)">Raj Dixit</tspan> 👋
    </text>
    <text x="0" y="34" class="font-sans" font-size="16" font-weight="500" fill="#94A3B8" letter-spacing="-0.2">
      Building software, solving problems, and turning ideas into products.
    </text>
  </g>

  <!-- Identity & Location Badges -->
  <g transform="translate(48, 192)">
    <!-- Role Badge -->
    <rect x="0" y="0" width="220" height="34" rx="10" fill="url(#tagDarkBg)" stroke="#334155" stroke-width="1"/>
    <text x="14" y="21" class="font-sans" font-size="12" font-weight="600" fill="#E2E8F0">
      💻 CS Student &amp; Developer
    </text>

    <!-- Location Badge -->
    <rect x="230" y="0" width="115" height="34" rx="10" fill="url(#tagDarkBg)" stroke="#334155" stroke-width="1"/>
    <text x="242" y="21" class="font-sans" font-size="12" font-weight="600" fill="#E2E8F0">
      📍 India
    </text>

    <!-- Core Stack Badge -->
    <rect x="355" y="0" width="175" height="34" rx="10" fill="url(#tagDarkBg)" stroke="#334155" stroke-width="1"/>
    <text x="367" y="21" class="font-sans" font-size="12" font-weight="600" fill="#E2E8F0">
      ⚡ Full-Stack &amp; AI
    </text>
  </g>

  <!-- Core Concept Ribbon: BUILD -> LEARN -> SHIP -->
  <g transform="translate(48, 258)">
    <rect x="0" y="0" width="482" height="74" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1.2"/>
    
    <!-- Item 1: BUILD -->
    <g transform="translate(18, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#312E81"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#A5B4FC">BUILD</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Software / Web</text>
    </g>

    <text x="145" y="44" class="font-sans" font-size="16" font-weight="700" fill="#475569">→</text>

    <!-- Item 2: LEARN -->
    <g transform="translate(170, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#064E3B"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#6EE7B7">LEARN</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">DSA / Systems</text>
    </g>

    <text x="295" y="44" class="font-sans" font-size="16" font-weight="700" fill="#475569">→</text>

    <!-- Item 3: SHIP -->
    <g transform="translate(320, 16)">
      <rect x="0" y="0" width="55" height="20" rx="5" fill="#581C87"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#D8B4FE">SHIP</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Real Solutions</text>
    </g>
  </g>

  <!-- Right Side: Illustrated Portrait & Glowing Ring Frame -->
  <g transform="translate(560, 25)" class="avatar-wrap">
    <!-- Ambient Neon Ring -->
    <circle cx="170" cy="165" r="145" fill="url(#avatarDarkGlow)"/>
    <circle cx="170" cy="165" r="138" fill="#0F172A" stroke="#38BDF8" stroke-width="2" stroke-opacity="0.6"/>
    
    <!-- Character Image Clip -->
    <clipPath id="avatarDarkClip">
      <circle cx="170" cy="165" r="132"/>
    </clipPath>
    
    <!-- Embedded Developer Avatar -->
    <image href="data:image/png;base64,{id_b64}" x="25" y="15" width="290" height="290" clip-path="url(#avatarDarkClip)" preserveAspectRatio="xMidYMid meet"/>

    <!-- Subtle Floating Code Badge -->
    <g transform="translate(10, 240)" class="float-badge" filter="url(#avatarNeon)">
      <rect x="0" y="0" width="124" height="34" rx="17" fill="#0F172A" stroke="#4F46E5" stroke-width="1.2"/>
      <circle cx="18" cy="17" r="9" fill="#312E81"/>
      <text x="13" y="21" class="font-sans" font-size="11" font-weight="700" fill="#A5B4FC">&lt;/&gt;</text>
      <text x="35" y="21" class="font-sans" font-size="11" font-weight="700" fill="#F8FAFC">Clean Code</text>
    </g>

    <!-- Top Floating Tech Pill -->
    <g transform="translate(230, 40)" class="float-badge">
      <rect x="0" y="0" width="95" height="30" rx="15" fill="#0F172A" stroke="#0284C7" stroke-width="1"/>
      <text x="16" y="19" class="font-sans" font-size="11" font-weight="700" fill="#38BDF8">🚀 Builder</text>
    </g>
  </g>
</svg>'''

with open('assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print('Wrote dark assets/hero.svg')

# -------------------------------------------------------------
# 2. ABOUT SVG (DARK THEME)
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 360" width="100%" height="100%">
  <defs>
    <linearGradient id="aboutDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="accentNeon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="aboutGlow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container Box -->
  <rect x="10" y="10" width="900" height="340" rx="20" fill="url(#aboutDarkBg)" stroke="#1E293B" stroke-width="1.5" filter="url(#aboutGlow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 38)">
    <rect x="0" y="0" width="112" height="24" rx="6" fill="#312E81"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#C7D2FE" letter-spacing="0.5">01 // ABOUT ME</text>
    <text x="126" y="17" class="font-sans" font-size="18" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">Engineering Mindset &amp; Philosophy</text>
  </g>

  <!-- Left Column: Story & Stance -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="505" height="235" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    
    <text x="24" y="32" class="font-sans" font-size="13" font-weight="700" fill="#818CF8" letter-spacing="0.3">PERSPECTIVE</text>
    <text x="24" y="58" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Passionate about robust code and tangible outcomes</text>
    
    <text x="24" y="90" class="font-sans" font-size="13.5" font-weight="400" fill="#94A3B8" line-height="22">
      <tspan x="24" dy="0">Computer Science undergraduate and full-stack software builder from</tspan>
      <tspan x="24" dy="24">Kanpur, India. Dedicated to crafting production systems end-to-end</tspan>
      <tspan x="24" dy="24">with React, Node.js, and MongoDB, bridging algorithmic foundations</tspan>
      <tspan x="24" dy="24">with modern AI automation workflows.</tspan>
    </text>

    <!-- Quote Box -->
    <g transform="translate(24, 168)">
      <rect x="0" y="0" width="457" height="46" rx="8" fill="#090E1D" stroke="#1E293B" stroke-width="1"/>
      <rect x="0" y="0" width="4" height="46" rx="2" fill="url(#accentNeon)"/>
      <text x="16" y="28" class="font-sans" font-size="12.5" font-weight="600" fill="#E2E8F0" font-style="italic">
        "Write clean code. Solve real problems. Ship meaningful products."
      </text>
    </g>
  </g>

  <!-- Right Column: 3 Pillars -->
  <g transform="translate(565, 85)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="310" height="70" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#312E81"/>
      <text x="22" y="40" class="font-sans" font-size="14">⚡</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">Software Craftsmanship</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Modular architectures &amp; scalable code</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="310" height="70" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#064E3B"/>
      <text x="22" y="40" class="font-sans" font-size="14">🧠</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">DSA &amp; Problem Solving</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Algorithmic efficiency &amp; optimization</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(0, 164)">
      <rect x="0" y="0" width="310" height="71" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#581C87"/>
      <text x="22" y="40" class="font-sans" font-size="14">🤖</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">AI &amp; Smart Automation</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Intelligent tools &amp; workflow pipelines</text>
    </g>
  </g>
</svg>'''

with open('assets/about.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)

print('Wrote dark assets/about.svg')

# -------------------------------------------------------------
# 3. TECH STACK SVG (DARK THEME)
# -------------------------------------------------------------
stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stackDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="stackGlow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="460" rx="20" fill="url(#stackDarkBg)" stroke="#1E293B" stroke-width="1.5" filter="url(#stackGlow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="115" height="24" rx="6" fill="#312E81"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#C7D2FE" letter-spacing="0.5">02 // TECH STACK</text>
    <text x="130" y="17" class="font-sans" font-size="18" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">Skills &amp; Technologies in Action</text>
  </g>

  <!-- Category 1: LANGUAGES -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    <!-- Category Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#6366F1"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#F8FAFC" letter-spacing="0.5">LANGUAGES</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#64748B">5 Core</text>

    <!-- Chips Grid -->
    <g transform="translate(18, 55)">
      <!-- Java -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="105" height="40" rx="10" fill="#1E293B" stroke="#7C2D12" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#EA580C"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">J</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#FB923C">Java</text>
      </g>
      <!-- C -->
      <g transform="translate(115, 0)">
        <rect x="0" y="0" width="85" height="40" rx="10" fill="#1E293B" stroke="#075985" stroke-width="1"/>
        <circle cx="18" cy="20" r="10" fill="#0284C7"/>
        <text x="14" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">C</text>
        <text x="36" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#38BDF8">C</text>
      </g>
      <!-- Python -->
      <g transform="translate(210, 0)">
        <rect x="0" y="0" width="120" height="40" rx="10" fill="#1E293B" stroke="#1E40AF" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#2563EB"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">Py</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#60A5FA">Python</text>
      </g>

      <!-- Row 2 -->
      <!-- JavaScript -->
      <g transform="translate(0, 52)">
        <rect x="0" y="0" width="135" height="40" rx="10" fill="#1E293B" stroke="#854D0E" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#CA8A04"/>
        <text x="14" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">JS</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#FDE047">JavaScript</text>
      </g>
      <!-- SQL -->
      <g transform="translate(145, 52)">
        <rect x="0" y="0" width="100" height="40" rx="10" fill="#1E293B" stroke="#5B21B6" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#7C3AED"/>
        <text x="14" y="24" class="font-sans" font-size="10" font-weight="800" fill="#FFFFFF">SQL</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#C084FC">SQL</text>
      </g>
    </g>
  </g>

  <!-- Category 2: WEB DEVELOPMENT -->
  <g transform="translate(470, 80)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#06B6D4"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#F8FAFC" letter-spacing="0.5">WEB DEVELOPMENT</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#64748B">5 Tools</text>

    <!-- Chips -->
    <g transform="translate(18, 55)">
      <!-- React -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="110" height="40" rx="10" fill="#1E293B" stroke="#155E75" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0891B2"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚛</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#22D3EE">React</text>
      </g>
      <!-- Node.js -->
      <g transform="translate(120, 0)">
        <rect x="0" y="0" width="115" height="40" rx="10" fill="#1E293B" stroke="#166534" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#16A34A"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⬢</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#4ADE80">Node.js</text>
      </g>
      <!-- Tailwind CSS -->
      <g transform="translate(245, 0)">
        <rect x="0" y="0" width="125" height="40" rx="10" fill="#1E293B" stroke="#115E59" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0D9488"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">≈</text>
        <text x="36" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#2DD4BF">Tailwind</text>
      </g>

      <!-- Row 2 -->
      <!-- HTML -->
      <g transform="translate(0, 52)">
        <rect x="0" y="0" width="110" height="40" rx="10" fill="#1E293B" stroke="#9F1239" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#E11D48"/>
        <text x="15" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">&lt;&gt;</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#FB7185">HTML5</text>
      </g>
      <!-- CSS -->
      <g transform="translate(120, 52)">
        <rect x="0" y="0" width="105" height="40" rx="10" fill="#1E293B" stroke="#075985" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0284C7"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">#</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#38BDF8">CSS3</text>
      </g>
    </g>
  </g>

  <!-- Category 3: TOOLS & ENVIRONMENT -->
  <g transform="translate(45, 270)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#10B981"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#F8FAFC" letter-spacing="0.5">DEV TOOLS &amp; PLATFORMS</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#64748B">3 Tools</text>

    <g transform="translate(18, 65)">
      <!-- Git -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="100" height="44" rx="10" fill="#1E293B" stroke="#9F1239" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#F43F5E"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⎇</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#FDA4AF">Git</text>
      </g>
      <!-- GitHub -->
      <g transform="translate(112, 0)">
        <rect x="0" y="0" width="120" height="44" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#475569"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">🐙</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">GitHub</text>
      </g>
      <!-- VS Code -->
      <g transform="translate(242, 0)">
        <rect x="0" y="0" width="125" height="44" rx="10" fill="#1E293B" stroke="#1D4ED8" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#2563EB"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">💻</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#60A5FA">VS Code</text>
      </g>
    </g>
  </g>

  <!-- Category 4: AI & AUTOMATION -->
  <g transform="translate(470, 270)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#8B5CF6"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#F8FAFC" letter-spacing="0.5">AI &amp; APPLIED COMPUTING</text>
    <text x="310" y="32" class="font-sans" font-size="11" font-weight="600" fill="#64748B">3 Domains</text>

    <g transform="translate(18, 65)">
      <!-- AI APIs -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="112" height="44" rx="10" fill="#1E293B" stroke="#6B21A8" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#9333EA"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚡</text>
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#D8B4FE">AI APIs</text>
      </g>
      <!-- Automation -->
      <g transform="translate(122, 0)">
        <rect x="0" y="0" width="124" height="44" rx="10" fill="#1E293B" stroke="#166534" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#16A34A"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚙</text>
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#4ADE80">Automation</text>
      </g>
      <!-- Computer Vision -->
      <g transform="translate(256, 0)">
        <rect x="0" y="0" width="114" height="44" rx="10" fill="#1E293B" stroke="#5B21B6" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#7C3AED"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">👁</text>
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#C084FC">Comp Vision</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

print('Wrote dark assets/stack.svg')

# -------------------------------------------------------------
# 4. PROJECTS SVG (DARK THEME)
# -------------------------------------------------------------
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 450" width="100%" height="100%">
  <defs>
    <linearGradient id="projDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="pDarkSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="430" rx="20" fill="url(#projDarkBg)" stroke="#1E293B" stroke-width="1.5" filter="url(#pDarkSh)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="158" height="24" rx="6" fill="#312E81"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#C7D2FE" letter-spacing="0.5">03 // CURRENTLY BUILDING</text>
    <text x="175" y="17" class="font-sans" font-size="18" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">Active Engineering &amp; Development Tracks</text>
  </g>

  <!-- 3 Project / Focus Cards -->
  <!-- Card 1: 01 Software Projects -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#1E3A8A"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#93C5FD">01</text>
    <rect x="175" y="20" width="70" height="22" rx="11" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <text x="187" y="35" class="font-sans" font-size="10" font-weight="700" fill="#6EE7B7">DEPLOYED</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#F8FAFC">AttendX &amp; Web Apps</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#818CF8">Full-Stack Production Suite</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#94A3B8">
      <tspan x="20" dy="0">Shipped smart attendance system</tspan>
      <tspan x="20" dy="20">with AI face biometric verification,</tspan>
      <tspan x="20" dy="20">QR dynamic codes, and GPS geofencing</tspan>
      <tspan x="20" dy="20">with React, Node.js &amp; Tailwind.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="55" height="24" rx="6" fill="#1E293B"/>
      <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">React</text>

      <rect x="62" y="0" width="60" height="24" rx="6" fill="#1E293B"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Node.js</text>

      <rect x="129" y="0" width="50" height="24" rx="6" fill="#1E293B"/>
      <text x="137" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">AI-Face</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#1E293B" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#38BDF8">Live Production →</text>
  </g>

  <!-- Card 2: 02 AI / Automation -->
  <g transform="translate(327, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#581C87"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#D8B4FE">02</text>
    <rect x="160" y="20" width="85" height="22" rx="11" fill="#3B0764" stroke="#7E22CE" stroke-width="1"/>
    <text x="172" y="35" class="font-sans" font-size="10" font-weight="700" fill="#C084FC">AUTOMATING</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#F8FAFC">AI &amp; Automation</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#C084FC">Intelligent Workflow Scripts</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#94A3B8">
      <tspan x="20" dy="0">Integrating smart AI APIs, vision</tspan>
      <tspan x="20" dy="20">processing, and custom Python automation</tspan>
      <tspan x="20" dy="20">to replace manual developer tasks with</tspan>
      <tspan x="20" dy="20">seamless intelligent pipelines.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="60" height="24" rx="6" fill="#1E293B"/>
      <text x="9" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Python</text>

      <rect x="67" y="0" width="60" height="24" rx="6" fill="#1E293B"/>
      <text x="75" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">AI APIs</text>

      <rect x="134" y="0" width="55" height="24" rx="6" fill="#1E293B"/>
      <text x="142" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Vision</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#1E293B" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#C084FC">Smart Workflows →</text>
  </g>

  <!-- Card 3: 03 Problem Solving -->
  <g transform="translate(610, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#064E3B"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#6EE7B7">03</text>
    <rect x="165" y="20" width="80" height="22" rx="11" fill="#022C22" stroke="#059669" stroke-width="1"/>
    <text x="175" y="35" class="font-sans" font-size="10" font-weight="700" fill="#34D399">PRACTICING</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#F8FAFC">Problem Solving</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#34D399">Data Structures &amp; Algorithms</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#94A3B8">
      <tspan x="20" dy="0">Practicing core algorithms in Java and C.</tspan>
      <tspan x="20" dy="20">Focusing on computational complexity,</tspan>
      <tspan x="20" dy="20">space-time optimization, and solid</tspan>
      <tspan x="20" dy="20">foundations for clean systems code.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="50" height="24" rx="6" fill="#1E293B"/>
      <text x="12" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Java</text>

      <rect x="57" y="0" width="40" height="24" rx="6" fill="#1E293B"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">C</text>

      <rect x="104" y="0" width="85" height="24" rx="6" fill="#1E293B"/>
      <text x="114" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Algorithms</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#1E293B" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#34D399">Core Foundations →</text>
  </g>
</svg>'''

with open('assets/projects.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)

print('Wrote dark assets/projects.svg')

# -------------------------------------------------------------
# 5. STATS & WORKFLOW SVG (DARK THEME)
# -------------------------------------------------------------
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 330" width="100%" height="100%">
  <defs>
    <linearGradient id="statsDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="stDarkSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="310" rx="20" fill="url(#statsDarkBg)" stroke="#1E293B" stroke-width="1.5" filter="url(#stDarkSh)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="138" height="24" rx="6" fill="#312E81"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#C7D2FE" letter-spacing="0.5">04 // DEV JOURNEY</text>
    <text x="154" y="17" class="font-sans" font-size="18" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">Engineering Focus &amp; Core Competencies</text>
  </g>

  <!-- 4 Pillar Stat Cards -->
  <g transform="translate(45, 80)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#1E3A8A"/>
      <text x="21" y="35" class="font-sans" font-size="13">🧠</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#60A5FA">ALGORITHMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#F8FAFC">DSA Mastery</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Java &amp; C Logic</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(212, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#064E3B"/>
      <text x="21" y="35" class="font-sans" font-size="13">⚡</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#34D399">ARCHITECTURE</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#F8FAFC">Clean Code</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Modular &amp; Scalable</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(424, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#581C87"/>
      <text x="21" y="35" class="font-sans" font-size="13">🌐</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#C084FC">WEB SYSTEMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#F8FAFC">Full-Stack Dev</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">React &amp; Node.js</text>
    </g>

    <!-- Pillar 4 -->
    <g transform="translate(636, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#7C2D12"/>
      <text x="21" y="35" class="font-sans" font-size="13">🚀</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#FB923C">INNOVATION</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#F8FAFC">AI Automation</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Pipelines &amp; Vision</text>
    </g>
  </g>

  <!-- Flow Visualizer Band -->
  <g transform="translate(45, 210)">
    <rect x="0" y="0" width="830" height="85" rx="14" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
    
    <text x="20" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#94A3B8" letter-spacing="0.5">DEV PIPELINE RHYTHM</text>
    <text x="700" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#34D399">● ACTIVE ITERATION</text>

    <!-- Visual Progress Tracks -->
    <g transform="translate(20, 44)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="185" height="22" rx="6" fill="#1E293B"/>
      <text x="14" y="15" class="font-sans" font-size="11" font-weight="700" fill="#818CF8">1. Deep Problem Solving</text>
      
      <text x="195" y="16" class="font-sans" font-size="12" font-weight="700" fill="#475569">→</text>

      <!-- Step 2 -->
      <rect x="215" y="0" width="185" height="22" rx="6" fill="#1E293B"/>
      <text x="230" y="15" class="font-sans" font-size="11" font-weight="700" fill="#38BDF8">2. Architectural Design</text>

      <text x="410" y="16" class="font-sans" font-size="12" font-weight="700" fill="#475569">→</text>

      <!-- Step 3 -->
      <rect x="430" y="0" width="185" height="22" rx="6" fill="#1E293B"/>
      <text x="444" y="15" class="font-sans" font-size="11" font-weight="700" fill="#C084FC">3. Implementation &amp; Test</text>

      <text x="625" y="16" class="font-sans" font-size="12" font-weight="700" fill="#475569">→</text>

      <!-- Step 4 -->
      <rect x="645" y="0" width="145" height="22" rx="6" fill="#1E293B"/>
      <text x="659" y="15" class="font-sans" font-size="11" font-weight="700" fill="#34D399">4. Ship &amp; Iterate</text>
    </g>
  </g>
</svg>'''

with open('assets/stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)

print('Wrote dark assets/stats.svg')

# -------------------------------------------------------------
# 6. CONNECT SVG (DARK THEME - NO YOUTUBE)
# -------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 370" width="100%" height="100%">
  <defs>
    <linearGradient id="connDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#141E33"/>
    </linearGradient>
    <filter id="cDarkSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .point-char {{ animation: gentlePoint 4s ease-in-out infinite; }}
      @keyframes gentlePoint {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(5px); }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .point-char {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="350" rx="20" fill="url(#connDarkBg)" stroke="#1E293B" stroke-width="1.5" filter="url(#cDarkSh)"/>

  <!-- Left Side: Pointing Character -->
  <g transform="translate(40, 20)" class="point-char">
    <!-- Character image -->
    <image href="data:image/png;base64,{pointing_b64}" x="0" y="5" width="310" height="310" preserveAspectRatio="xMidYMid meet"/>

    <!-- Speech bubble in Dark Style -->
    <g transform="translate(130, 20)">
      <rect x="0" y="0" width="185" height="38" rx="12" fill="#0F172A" stroke="#38BDF8" stroke-width="1.2"/>
      <text x="14" y="24" class="font-sans" font-size="12" font-weight="700" fill="#F8FAFC">Let's connect! 👉</text>
    </g>
  </g>

  <!-- Right Side: Social Navigation Cards (NO YOUTUBE) -->
  <g transform="translate(390, 42)">
    <!-- Section Header -->
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#312E81"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#C7D2FE" letter-spacing="0.5">05 // GET IN TOUCH</text>
    <text x="142" y="17" class="font-sans" font-size="18" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">Let's Build Something Together</text>
    
    <text x="0" y="52" class="font-sans" font-size="13" font-weight="400" fill="#94A3B8">
      Open for collaborations, developer networking, and software opportunities.
    </text>

    <!-- Social Rows (No YouTube) -->
    <g transform="translate(0, 72)">
      <!-- GitHub Card -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="480" height="46" rx="10" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#1E293B"/>
        <text x="18" y="28" class="font-sans" font-size="12" font-weight="700" fill="#FFFFFF">🐙</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">GitHub (@rajdixit070-v)</text>
        <text x="220" y="28" class="font-sans" font-size="12" font-weight="500" fill="#94A3B8">— Repositories &amp; Open Source</text>
        <text x="450" y="28" class="font-sans" font-size="14" font-weight="700" fill="#38BDF8">→</text>
      </g>

      <!-- LinkedIn Card -->
      <g transform="translate(0, 56)">
        <rect x="0" y="0" width="480" height="46" rx="10" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#0A66C2"/>
        <text x="18" y="28" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">in</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#60A5FA">LinkedIn (Raj Dixit)</text>
        <text x="210" y="28" class="font-sans" font-size="12" font-weight="500" fill="#94A3B8">— Professional Network &amp; Career</text>
        <text x="450" y="28" class="font-sans" font-size="14" font-weight="700" fill="#60A5FA">→</text>
      </g>

      <!-- Portfolio Card -->
      <g transform="translate(0, 112)">
        <rect x="0" y="0" width="480" height="46" rx="10" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#581C87"/>
        <text x="17" y="28" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌐</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#C084FC">Portfolio &amp; Shipped Apps</text>
        <text x="230" y="28" class="font-sans" font-size="12" font-weight="500" fill="#94A3B8">— AttendX, LibSphere &amp; Live Demos</text>
        <text x="450" y="28" class="font-sans" font-size="14" font-weight="700" fill="#C084FC">→</text>
      </g>
    </g>

    <!-- Subnote -->
    <text x="0" y="260" class="font-sans" font-size="12" font-weight="600" fill="#64748B">
      👇 Direct clickable links available in Markdown immediately below
    </text>
  </g>
</svg>'''

with open('assets/connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print('Wrote dark assets/connect.svg')
