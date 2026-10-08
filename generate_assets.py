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
# 1. HERO SVG
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 390" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="45%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#EEF2FF"/>
    </linearGradient>
    <linearGradient id="heroBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E2E8F0"/>
      <stop offset="50%" stop-color="#C7D2FE"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="50%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="avatarGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0E7FF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#DBEAFE" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="tagBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EEF2FF"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
    <filter id="avatarShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#3B82F6" flood-opacity="0.12"/>
    </filter>
    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .pulse-dot {{ animation: pulseDot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
      .float-badge {{ animation: floatY 4s ease-in-out infinite; }}
      .avatar-wrap {{ animation: subtleFloat 6s ease-in-out infinite; }}
      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(0.9); }}
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

  <!-- Main Card -->
  <rect x="10" y="10" width="900" height="370" rx="24" fill="url(#heroBg)" stroke="url(#heroBorder)" stroke-width="1.5" filter="url(#cardShadow)"/>

  <!-- Subtle Top Decorative Grid Elements -->
  <g opacity="0.18">
    <circle cx="80" cy="50" r="1.5" fill="#4F46E5"/>
    <circle cx="120" cy="50" r="1.5" fill="#4F46E5"/>
    <circle cx="160" cy="50" r="1.5" fill="#4F46E5"/>
    <circle cx="80" cy="80" r="1.5" fill="#4F46E5"/>
    <circle cx="120" cy="80" r="1.5" fill="#4F46E5"/>
    <circle cx="160" cy="80" r="1.5" fill="#4F46E5"/>
  </g>

  <!-- Left Content Column -->
  <!-- Status Pill -->
  <g transform="translate(48, 42)">
    <rect x="0" y="0" width="285" height="30" rx="15" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <circle cx="15" cy="15" r="4.5" fill="#10B981" class="pulse-dot"/>
    <text x="28" y="19" class="font-sans" font-size="11" font-weight="700" fill="#065F46" letter-spacing="0.5">OPEN TO OPPORTUNITIES • DEV</text>
  </g>

  <!-- Greeting & Headline -->
  <g transform="translate(48, 120)">
    <text x="0" y="0" class="font-sans" font-size="34" font-weight="800" fill="#0F172A" letter-spacing="-0.8">
      Hi, I'm <tspan fill="url(#accentGrad)">Raj Dixit</tspan> 👋
    </text>
    <text x="0" y="34" class="font-sans" font-size="16.5" font-weight="500" fill="#475569" letter-spacing="-0.2">
      Building software, solving problems, and turning ideas into products.
    </text>
  </g>

  <!-- Identity & Location Badges -->
  <g transform="translate(48, 192)">
    <!-- Role Badge -->
    <rect x="0" y="0" width="210" height="34" rx="10" fill="url(#tagBg)" stroke="#E2E8F0" stroke-width="1"/>
    <text x="14" y="21" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      💻 CS Student &amp; Developer
    </text>

    <!-- Location Badge -->
    <rect x="220" y="0" width="105" height="34" rx="10" fill="url(#tagBg)" stroke="#E2E8F0" stroke-width="1"/>
    <text x="234" y="21" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      📍 India
    </text>

    <!-- Core Stack Badge -->
    <rect x="335" y="0" width="175" height="34" rx="10" fill="url(#tagBg)" stroke="#E2E8F0" stroke-width="1"/>
    <text x="349" y="21" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      ⚡ Full-Stack &amp; AI
    </text>
  </g>

  <!-- Core Concept Ribbon: BUILD -> LEARN -> SHIP -->
  <g transform="translate(48, 260)">
    <rect x="0" y="0" width="462" height="74" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Item 1: BUILD -->
    <g transform="translate(18, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#EEF2FF"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#4F46E5">BUILD</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">Software / Web</text>
    </g>

    <text x="135" y="44" class="font-sans" font-size="16" font-weight="700" fill="#CBD5E1">→</text>

    <!-- Item 2: LEARN -->
    <g transform="translate(160, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#F0FDF4"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#16A34A">LEARN</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">DSA / Systems</text>
    </g>

    <text x="280" y="44" class="font-sans" font-size="16" font-weight="700" fill="#CBD5E1">→</text>

    <!-- Item 3: SHIP -->
    <g transform="translate(305, 16)">
      <rect x="0" y="0" width="55" height="20" rx="5" fill="#FAF5FF"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#9333EA">SHIP</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">Real Solutions</text>
    </g>
  </g>

  <!-- Right Side: Illustrated Portrait & Ambient Glow Frame -->
  <g transform="translate(560, 25)" class="avatar-wrap">
    <!-- Ambient Backdrop Circle -->
    <circle cx="170" cy="165" r="145" fill="url(#avatarGlow)"/>
    <circle cx="170" cy="165" r="138" fill="#FFFFFF" stroke="#E0E7FF" stroke-width="2"/>
    
    <!-- Character Image Clip -->
    <clipPath id="avatarCircleClip">
      <circle cx="170" cy="165" r="132"/>
    </clipPath>
    
    <!-- Embedded Developer Avatar -->
    <image href="data:image/png;base64,{id_b64}" x="25" y="15" width="290" height="290" clip-path="url(#avatarCircleClip)" preserveAspectRatio="xMidYMid meet"/>

    <!-- Subtle Floating Code Badge -->
    <g transform="translate(10, 240)" class="float-badge" filter="url(#avatarShadow)">
      <rect x="0" y="0" width="124" height="34" rx="17" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2"/>
      <circle cx="18" cy="17" r="9" fill="#EEF2FF"/>
      <text x="13" y="21" class="font-sans" font-size="11" font-weight="700" fill="#4F46E5">&lt;/&gt;</text>
      <text x="35" y="21" class="font-sans" font-size="11" font-weight="700" fill="#1E293B">Clean Code</text>
    </g>

    <!-- Top Floating Tech Pill -->
    <g transform="translate(230, 40)" class="float-badge">
      <rect x="0" y="0" width="95" height="30" rx="15" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="19" class="font-sans" font-size="11" font-weight="700" fill="#2563EB">🚀 Builder</text>
    </g>
  </g>
</svg>'''

with open('assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print('Wrote assets/hero.svg')

# -------------------------------------------------------------
# 2. ABOUT SVG
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 360" width="100%" height="100%">
  <defs>
    <linearGradient id="aboutBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="aboutShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container Box -->
  <rect x="10" y="10" width="900" height="340" rx="20" fill="url(#aboutBg)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#aboutShadow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 38)">
    <rect x="0" y="0" width="112" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">01 // ABOUT ME</text>
    <text x="126" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Engineering Mindset &amp; Philosophy</text>
  </g>

  <!-- Left Column: Story & Stance -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="505" height="235" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <text x="24" y="32" class="font-sans" font-size="13" font-weight="700" fill="#4F46E5" letter-spacing="0.3">PERSPECTIVE</text>
    <text x="24" y="58" class="font-sans" font-size="15.5" font-weight="700" fill="#0F172A">Passionate about robust code and tangible outcomes</text>
    
    <text x="24" y="90" class="font-sans" font-size="13.5" font-weight="400" fill="#334155" line-height="22">
      <tspan x="24" dy="0">I'm a Computer Science student and software developer based in India,</tspan>
      <tspan x="24" dy="24">driven by building reliable applications and solving complex algorithmic</tspan>
      <tspan x="24" dy="24">challenges. I bridge foundational computer science with modern full-stack</tspan>
      <tspan x="24" dy="24">engineering and intelligent automation.</tspan>
    </text>

    <!-- Quote Box -->
    <g transform="translate(24, 168)">
      <rect x="0" y="0" width="457" height="46" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <rect x="0" y="0" width="4" height="46" rx="2" fill="url(#accentLine)"/>
      <text x="16" y="28" class="font-sans" font-size="12.5" font-weight="600" fill="#1E293B" font-style="italic">
        "Write clean code. Solve real problems. Ship meaningful products."
      </text>
    </g>
  </g>

  <!-- Right Column: 3 Pillars -->
  <g transform="translate(565, 85)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="310" height="70" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#EEF2FF"/>
      <text x="22" y="40" class="font-sans" font-size="14">⚡</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">Software Craftsmanship</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Modular architectures &amp; scalable code</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="310" height="70" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#F0FDF4"/>
      <text x="22" y="40" class="font-sans" font-size="14">🧠</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">DSA &amp; Problem Solving</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Algorithmic efficiency &amp; optimization</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(0, 164)">
      <rect x="0" y="0" width="310" height="71" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#FAF5FF"/>
      <text x="22" y="40" class="font-sans" font-size="14">🤖</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">AI &amp; Smart Automation</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Intelligent tools &amp; workflow pipelines</text>
    </g>
  </g>
</svg>'''

with open('assets/about.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)

print('Wrote assets/about.svg')

# -------------------------------------------------------------
# 3. TECH STACK SVG
# -------------------------------------------------------------
stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stackBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="cardSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
      .pill { transition: all 0.2s ease; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="460" rx="20" fill="url(#stackBg)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cardSh)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="115" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">02 // TECH STACK</text>
    <text x="130" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Skills &amp; Technologies in Action</text>
  </g>

  <!-- Category 1: LANGUAGES -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <!-- Category Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#4F46E5"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">LANGUAGES</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">5 Technologies</text>

    <!-- Chips Grid -->
    <g transform="translate(18, 55)">
      <!-- Java -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="105" height="40" rx="10" fill="#FFF7ED" stroke="#FED7AA" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#EA580C"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">J</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#9A3412">Java</text>
      </g>
      <!-- C -->
      <g transform="translate(115, 0)">
        <rect x="0" y="0" width="85" height="40" rx="10" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1"/>
        <circle cx="18" cy="20" r="10" fill="#0284C7"/>
        <text x="14" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">C</text>
        <text x="36" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#0369A1">C</text>
      </g>
      <!-- Python -->
      <g transform="translate(210, 0)">
        <rect x="0" y="0" width="120" height="40" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#2563EB"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">Py</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#1D4ED8">Python</text>
      </g>

      <!-- Row 2 -->
      <!-- JavaScript -->
      <g transform="translate(0, 52)">
        <rect x="0" y="0" width="135" height="40" rx="10" fill="#FEFCE8" stroke="#FEF08A" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#CA8A04"/>
        <text x="14" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">JS</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#854D0E">JavaScript</text>
      </g>
      <!-- SQL -->
      <g transform="translate(145, 52)">
        <rect x="0" y="0" width="100" height="40" rx="10" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#7C3AED"/>
        <text x="14" y="24" class="font-sans" font-size="10" font-weight="800" fill="#FFFFFF">SQL</text>
        <text x="40" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#6D28D9">SQL</text>
      </g>
    </g>
  </g>

  <!-- Category 2: WEB DEVELOPMENT -->
  <g transform="translate(470, 80)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#06B6D4"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">WEB DEVELOPMENT</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">5 Frameworks</text>

    <!-- Chips -->
    <g transform="translate(18, 55)">
      <!-- React -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="110" height="40" rx="10" fill="#ECFEFF" stroke="#A5F3FC" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0891B2"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚛</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#0E7490">React</text>
      </g>
      <!-- Node.js -->
      <g transform="translate(120, 0)">
        <rect x="0" y="0" width="115" height="40" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#16A34A"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⬢</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#15803D">Node.js</text>
      </g>
      <!-- Tailwind CSS -->
      <g transform="translate(245, 0)">
        <rect x="0" y="0" width="125" height="40" rx="10" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0D9488"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">≈</text>
        <text x="36" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#0F766E">Tailwind</text>
      </g>

      <!-- Row 2 -->
      <!-- HTML -->
      <g transform="translate(0, 52)">
        <rect x="0" y="0" width="110" height="40" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#E11D48"/>
        <text x="15" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">&lt;&gt;</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#BE123C">HTML5</text>
      </g>
      <!-- CSS -->
      <g transform="translate(120, 52)">
        <rect x="0" y="0" width="105" height="40" rx="10" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1"/>
        <circle cx="20" cy="20" r="10" fill="#0284C7"/>
        <text x="16" y="24" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">#</text>
        <text x="38" y="24" class="font-sans" font-size="12.5" font-weight="700" fill="#0369A1">CSS3</text>
      </g>
    </g>
  </g>

  <!-- Category 3: TOOLS & ENVIRONMENT -->
  <g transform="translate(45, 270)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#10B981"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">DEV TOOLS &amp; WORKFLOW</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">3 Utilities</text>

    <g transform="translate(18, 65)">
      <!-- Git -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="100" height="44" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#F43F5E"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⎇</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#BE123C">Git</text>
      </g>
      <!-- GitHub -->
      <g transform="translate(112, 0)">
        <rect x="0" y="0" width="120" height="44" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#1E293B"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">🐙</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">GitHub</text>
      </g>
      <!-- VS Code -->
      <g transform="translate(242, 0)">
        <rect x="0" y="0" width="125" height="44" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#2563EB"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">💻</text>
        <text x="42" y="27" class="font-sans" font-size="13" font-weight="700" fill="#1D4ED8">VS Code</text>
      </g>
    </g>
  </g>

  <!-- Category 4: AI & AUTOMATION -->
  <g transform="translate(470, 270)">
    <rect x="0" y="0" width="405" height="170" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <!-- Title -->
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#8B5CF6"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">AI &amp; APPLIED COMPUTING</text>
    <text x="310" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">3 Domains</text>

    <g transform="translate(18, 65)">
      <!-- AI APIs -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="112" height="44" rx="10" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#9333EA"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚡</text>
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#7E22CE">AI APIs</text>
      </g>
      <!-- Automation -->
      <g transform="translate(122, 0)">
        <rect x="0" y="0" width="124" height="44" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#16A34A"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">⚙</text>
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#15803D">Automation</text>
      </g>
      <!-- Computer Vision -->
      <g transform="translate(256, 0)">
        <rect x="0" y="0" width="114" height="44" rx="10" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
        <circle cx="22" cy="22" r="11" fill="#7C3AED"/>
        <text x="16" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">👁</text>
        <text x="40" y="27" class="font-sans" font-size="12" font-weight="700" fill="#6D28D9">Comp Vision</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

print('Wrote assets/stack.svg')

# -------------------------------------------------------------
# 4. PROJECTS SVG
# -------------------------------------------------------------
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 450" width="100%" height="100%">
  <defs>
    <linearGradient id="projBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="pCardSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="430" rx="20" fill="url(#projBg)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#pCardSh)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="158" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">03 // CURRENTLY BUILDING</text>
    <text x="175" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Active Engineering &amp; Development Tracks</text>
  </g>

  <!-- 3 Project / Focus Cards -->
  <!-- Card 1: 01 Software Projects -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#EFF6FF"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#2563EB">01</text>
    <rect x="175" y="20" width="70" height="22" rx="11" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <text x="187" y="35" class="font-sans" font-size="10" font-weight="700" fill="#065F46">BUILDING</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#0F172A">Software Projects</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#4F46E5">Full-Stack Web Architectures</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="20" dy="0">Architecting modular web applications</tspan>
      <tspan x="20" dy="20">with React and Node.js. Focused on</tspan>
      <tspan x="20" dy="20">responsive UI, robust state flows,</tspan>
      <tspan x="20" dy="20">and RESTful data interactions.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="55" height="24" rx="6" fill="#F1F5F9"/>
      <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">React</text>

      <rect x="62" y="0" width="60" height="24" rx="6" fill="#F1F5F9"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Node.js</text>

      <rect x="129" y="0" width="46" height="24" rx="6" fill="#F1F5F9"/>
      <text x="139" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">SQL</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#F1F5F9" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#2563EB">Production Systems →</text>
  </g>

  <!-- Card 2: 02 AI / Automation -->
  <g transform="translate(327, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#FAF5FF"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#9333EA">02</text>
    <rect x="160" y="20" width="85" height="22" rx="11" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="172" y="35" class="font-sans" font-size="10" font-weight="700" fill="#6D28D9">AUTOMATING</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#0F172A">AI &amp; Automation</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#9333EA">Intelligent Workflow Scripts</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="20" dy="0">Integrating smart AI APIs, vision</tspan>
      <tspan x="20" dy="20">processing, and custom Python automation</tspan>
      <tspan x="20" dy="20">to replace manual developer tasks with</tspan>
      <tspan x="20" dy="20">seamless intelligent pipelines.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="60" height="24" rx="6" fill="#F1F5F9"/>
      <text x="9" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Python</text>

      <rect x="67" y="0" width="60" height="24" rx="6" fill="#F1F5F9"/>
      <text x="75" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">AI APIs</text>

      <rect x="134" y="0" width="55" height="24" rx="6" fill="#F1F5F9"/>
      <text x="142" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Vision</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#F1F5F9" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#9333EA">Smart Workflows →</text>
  </g>

  <!-- Card 3: 03 Problem Solving -->
  <g transform="translate(610, 80)">
    <rect x="0" y="0" width="265" height="325" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Header Badge -->
    <rect x="20" y="20" width="45" height="22" rx="6" fill="#F0FDF4"/>
    <text x="32" y="35" class="font-sans" font-size="11" font-weight="800" fill="#16A34A">03</text>
    <rect x="165" y="20" width="80" height="22" rx="11" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="175" y="35" class="font-sans" font-size="10" font-weight="700" fill="#166534">PRACTICING</text>

    <!-- Title & Domain -->
    <text x="20" y="75" class="font-sans" font-size="17" font-weight="800" fill="#0F172A">Problem Solving</text>
    <text x="20" y="96" class="font-sans" font-size="12" font-weight="600" fill="#16A34A">Data Structures &amp; Algorithms</text>

    <!-- Description -->
    <text x="20" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="20" dy="0">Practicing core algorithms in Java and C.</tspan>
      <tspan x="20" dy="20">Focusing on computational complexity,</tspan>
      <tspan x="20" dy="20">space-time optimization, and solid</tspan>
      <tspan x="20" dy="20">foundations for clean systems code.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="50" height="24" rx="6" fill="#F1F5F9"/>
      <text x="12" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Java</text>

      <rect x="57" y="0" width="40" height="24" rx="6" fill="#F1F5F9"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">C</text>

      <rect x="104" y="0" width="85" height="24" rx="6" fill="#F1F5F9"/>
      <text x="114" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Algorithms</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="20" y1="275" x2="245" y2="275" stroke="#F1F5F9" stroke-width="1"/>
    <text x="20" y="302" class="font-sans" font-size="12" font-weight="700" fill="#16A34A">Core Foundations →</text>
  </g>
</svg>'''

with open('assets/projects.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)

print('Wrote assets/projects.svg')

# -------------------------------------------------------------
# 5. STATS & WORKFLOW SVG
# -------------------------------------------------------------
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 330" width="100%" height="100%">
  <defs>
    <linearGradient id="statsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="50%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <filter id="stSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="10" y="10" width="900" height="310" rx="20" fill="url(#statsBg)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#stSh)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="138" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">04 // DEV JOURNEY</text>
    <text x="154" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Engineering Focus &amp; Core Competencies</text>
  </g>

  <!-- 4 Pillar Stat Cards -->
  <g transform="translate(45, 80)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#EFF6FF"/>
      <text x="21" y="35" class="font-sans" font-size="13">🧠</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#2563EB">ALGORITHMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">DSA Mastery</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Java &amp; C Logic</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(212, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#ECFDF5"/>
      <text x="21" y="35" class="font-sans" font-size="13">⚡</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#059669">ARCHITECTURE</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">Clean Code</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Modular &amp; Scalable</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(424, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#FAF5FF"/>
      <text x="21" y="35" class="font-sans" font-size="13">🌐</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#7C3AED">WEB SYSTEMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">Full-Stack Dev</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">React &amp; Node.js</text>
    </g>

    <!-- Pillar 4 -->
    <g transform="translate(636, 0)">
      <rect x="0" y="0" width="195" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#FFF7ED"/>
      <text x="21" y="35" class="font-sans" font-size="13">🚀</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#EA580C">INNOVATION</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">AI Automation</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Pipelines &amp; Vision</text>
    </g>
  </g>

  <!-- Flow Visualizer Band -->
  <g transform="translate(45, 210)">
    <rect x="0" y="0" width="830" height="85" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <text x="20" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#475569" letter-spacing="0.5">DEV PIPELINE RHYTHM</text>
    <text x="700" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#10B981">● ACTIVE ITERATION</text>

    <!-- Visual Progress Tracks -->
    <g transform="translate(20, 44)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="185" height="22" rx="6" fill="#EEF2FF"/>
      <text x="14" y="15" class="font-sans" font-size="11" font-weight="700" fill="#4F46E5">1. Deep Problem Solving</text>
      
      <text x="195" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 2 -->
      <rect x="215" y="0" width="185" height="22" rx="6" fill="#F0F9FF"/>
      <text x="230" y="15" class="font-sans" font-size="11" font-weight="700" fill="#0284C7">2. Architectural Design</text>

      <text x="410" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 3 -->
      <rect x="430" y="0" width="185" height="22" rx="6" fill="#F5F3FF"/>
      <text x="444" y="15" class="font-sans" font-size="11" font-weight="700" fill="#7C3AED">3. Implementation &amp; Test</text>

      <text x="625" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 4 -->
      <rect x="645" y="0" width="145" height="22" rx="6" fill="#ECFDF5"/>
      <text x="659" y="15" class="font-sans" font-size="11" font-weight="700" fill="#059669">4. Ship &amp; Iterate</text>
    </g>
  </g>
</svg>'''

with open('assets/stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)

print('Wrote assets/stats.svg')

# -------------------------------------------------------------
# 6. CONNECT SVG
# -------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 370" width="100%" height="100%">
  <defs>
    <linearGradient id="connBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#EEF2FF"/>
    </linearGradient>
    <filter id="cSh" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#0F172A" flood-opacity="0.05"/>
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
  <rect x="10" y="10" width="900" height="350" rx="20" fill="url(#connBg)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cSh)"/>

  <!-- Left Side: Pointing Character -->
  <g transform="translate(40, 20)" class="point-char">
    <!-- Character image -->
    <image href="data:image/png;base64,{pointing_b64}" x="0" y="5" width="310" height="310" preserveAspectRatio="xMidYMid meet"/>

    <!-- Speech bubble -->
    <g transform="translate(140, 20)">
      <rect x="0" y="0" width="175" height="38" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
      <text x="14" y="24" class="font-sans" font-size="12" font-weight="700" fill="#1E293B">Let's connect! 👉</text>
    </g>
  </g>

  <!-- Right Side: Social Navigation Cards -->
  <g transform="translate(390, 36)">
    <!-- Section Header -->
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">05 // GET IN TOUCH</text>
    <text x="142" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Let's Build Something Together</text>
    
    <text x="0" y="52" class="font-sans" font-size="13" font-weight="400" fill="#475569">
      Open for collaborations, interesting tech discussions, or software opportunities.
    </text>

    <!-- Social Rows Preview (Clickable links in Markdown below) -->
    <g transform="translate(0, 72)">
      <!-- GitHub Card -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="480" height="42" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="21" r="12" fill="#0F172A"/>
        <text x="18" y="26" class="font-sans" font-size="12" font-weight="700" fill="#FFFFFF">🐙</text>
        <text x="48" y="26" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">GitHub (@rajdixit070-v)</text>
        <text x="220" y="26" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— 26+ Repositories &amp; Projects</text>
        <text x="450" y="26" class="font-sans" font-size="14" font-weight="700" fill="#2563EB">→</text>
      </g>

      <!-- LinkedIn Card -->
      <g transform="translate(0, 52)">
        <rect x="0" y="0" width="480" height="42" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="21" r="12" fill="#0A66C2"/>
        <text x="18" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">in</text>
        <text x="48" y="26" class="font-sans" font-size="13" font-weight="700" fill="#0A66C2">LinkedIn</text>
        <text x="118" y="26" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— Professional background &amp; networking</text>
        <text x="450" y="26" class="font-sans" font-size="14" font-weight="700" fill="#0A66C2">→</text>
      </g>

      <!-- Portfolio Card -->
      <g transform="translate(0, 104)">
        <rect x="0" y="0" width="480" height="42" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="21" r="12" fill="#7C3AED"/>
        <text x="17" y="26" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌐</text>
        <text x="48" y="26" class="font-sans" font-size="13" font-weight="700" fill="#7C3AED">Portfolio</text>
        <text x="115" y="26" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— Live deployments, case studies &amp; bio</text>
        <text x="450" y="26" class="font-sans" font-size="14" font-weight="700" fill="#7C3AED">→</text>
      </g>

      <!-- YouTube / Media Card -->
      <g transform="translate(0, 156)">
        <rect x="0" y="0" width="480" height="42" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="21" r="12" fill="#DC2626"/>
        <text x="17" y="26" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">▶</text>
        <text x="48" y="26" class="font-sans" font-size="13" font-weight="700" fill="#DC2626">YouTube &amp; Tech Media</text>
        <text x="208" y="26" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— Video demos &amp; tech tutorials</text>
        <text x="450" y="26" class="font-sans" font-size="14" font-weight="700" fill="#DC2626">→</text>
      </g>
    </g>

    <!-- Subnote -->
    <text x="0" y="295" class="font-sans" font-size="12" font-weight="600" fill="#64748B">
      👇 Direct clickable links available in Markdown immediately below
    </text>
  </g>
</svg>'''

with open('assets/connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print('Wrote assets/connect.svg')
