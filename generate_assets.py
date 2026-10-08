import os
import base64
from PIL import Image, ImageOps
import io

def get_base64_png(path, size=None, flip_h=False):
    im = Image.open(path)
    if flip_h:
        im = ImageOps.mirror(im)
    if size:
        im = im.resize(size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

id_b64 = get_base64_png('assets/id.png', (540, 540))
# Right side character in connect.svg pointing toward left (into content)
pointing_left_b64 = get_base64_png('assets/right_pointing.png', (540, 540), flip_h=True)

# -------------------------------------------------------------
# 1. HERO SVG (UNIFORM CLEAN LIGHT THEME - STRICT TWO COLUMNS)
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 380" width="100%" height="100%">
  <defs>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="50%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="avatarRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0E7FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
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
        50% {{ transform: translateY(-4px); }}
      }}
      @keyframes subtleFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-3px); }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .pulse-dot, .float-badge, .avatar-wrap {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Uniform Clean White Base Card -->
  <rect x="8" y="8" width="924" height="364" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#softShadow)"/>

  <!-- LEFT COLUMN: STRICTLY x=45 to x=515 (NO OVERLAP) -->
  <!-- Status Pill -->
  <g transform="translate(45, 38)">
    <rect x="0" y="0" width="295" height="28" rx="14" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <circle cx="14" cy="14" r="4.5" fill="#10B981" class="pulse-dot"/>
    <text x="26" y="18" class="font-sans" font-size="11" font-weight="700" fill="#065F46" letter-spacing="0.5">OPEN TO OPPORTUNITIES • DEVELOPER</text>
  </g>

  <!-- Greeting & Headline -->
  <g transform="translate(45, 114)">
    <text x="0" y="0" class="font-sans" font-size="34" font-weight="800" fill="#0F172A" letter-spacing="-0.8">
      Hi, I'm <tspan fill="url(#textGrad)">Raj Dixit</tspan> 👋
    </text>
    <text x="0" y="34" class="font-sans" font-size="15.5" font-weight="500" fill="#475569" letter-spacing="-0.2">
      Building software, solving problems, and turning ideas into products.
    </text>
  </g>

  <!-- Identity Badges -->
  <g transform="translate(45, 186)">
    <!-- Role Badge -->
    <rect x="0" y="0" width="205" height="32" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="12" y="20" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      💻 CS Student &amp; Developer
    </text>

    <!-- Location Badge -->
    <rect x="215" y="0" width="115" height="32" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="227" y="20" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      📍 Kanpur, India
    </text>

    <!-- Stack Badge -->
    <rect x="340" y="0" width="130" height="32" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="352" y="20" class="font-sans" font-size="12" font-weight="600" fill="#334155">
      ⚡ Full-Stack &amp; AI
    </text>
  </g>

  <!-- Core Motif: BUILD -> LEARN -> SHIP (Width 470px) -->
  <g transform="translate(45, 248)">
    <rect x="0" y="0" width="470" height="74" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Item 1: BUILD -->
    <g transform="translate(18, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#EEF2FF"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#4F46E5">BUILD</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">Software / Web</text>
    </g>

    <text x="140" y="44" class="font-sans" font-size="16" font-weight="700" fill="#CBD5E1">→</text>

    <!-- Item 2: LEARN -->
    <g transform="translate(165, 16)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#F0FDF4"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#16A34A">LEARN</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">DSA / Systems</text>
    </g>

    <text x="290" y="44" class="font-sans" font-size="16" font-weight="700" fill="#CBD5E1">→</text>

    <!-- Item 3: SHIP -->
    <g transform="translate(315, 16)">
      <rect x="0" y="0" width="55" height="20" rx="5" fill="#FAF5FF"/>
      <text x="10" y="14" class="font-sans" font-size="10" font-weight="800" fill="#9333EA">SHIP</text>
      <text x="0" y="34" class="font-sans" font-size="11.5" font-weight="500" fill="#475569">Real Products</text>
    </g>
  </g>

  <!-- RIGHT COLUMN: STRICTLY x=580 to x=900 (SEPARATE & NO OVERLAP) -->
  <g transform="translate(600, 22)" class="avatar-wrap">
    <!-- Clean Circular Frame -->
    <circle cx="150" cy="160" r="142" fill="url(#avatarRing)"/>
    <circle cx="150" cy="160" r="136" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2"/>
    
    <!-- Character Image Clip -->
    <clipPath id="heroAvatarClip">
      <circle cx="150" cy="160" r="130"/>
    </clipPath>
    
    <!-- Embedded Developer Avatar -->
    <image href="data:image/png;base64,{id_b64}" x="10" y="15" width="280" height="280" clip-path="url(#heroAvatarClip)" preserveAspectRatio="xMidYMid meet"/>

    <!-- Bottom Code Badge (strictly on right side) -->
    <g transform="translate(0, 235)" class="float-badge">
      <rect x="0" y="0" width="118" height="32" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="url(#softShadow)"/>
      <circle cx="16" cy="16" r="8" fill="#EEF2FF"/>
      <text x="12" y="20" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5">&lt;/&gt;</text>
      <text x="32" y="20" class="font-sans" font-size="11" font-weight="700" fill="#1E293B">Clean Code</text>
    </g>

    <!-- Top Badge (strictly on right side) -->
    <g transform="translate(200, 20)" class="float-badge">
      <rect x="0" y="0" width="90" height="28" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" filter="url(#softShadow)"/>
      <text x="14" y="18" class="font-sans" font-size="11" font-weight="700" fill="#2563EB">🚀 Builder</text>
    </g>
  </g>
</svg>'''

with open('assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print('Wrote uniform light assets/hero.svg')

# -------------------------------------------------------------
# 2. ABOUT SVG (UNIFORM CLEAN LIGHT THEME)
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 360" width="100%" height="100%">
  <defs>
    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="aboutShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container Box -->
  <rect x="8" y="8" width="924" height="344" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#aboutShadow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="112" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">01 // ABOUT ME</text>
    <text x="126" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Engineering Mindset &amp; Philosophy</text>
  </g>

  <!-- Left Column: Story -->
  <g transform="translate(45, 82)">
    <rect x="0" y="0" width="510" height="235" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <text x="24" y="32" class="font-sans" font-size="12.5" font-weight="700" fill="#4F46E5" letter-spacing="0.3">PERSPECTIVE</text>
    <text x="24" y="58" class="font-sans" font-size="15.5" font-weight="700" fill="#0F172A">Passionate about robust code and tangible outcomes</text>
    
    <text x="24" y="90" class="font-sans" font-size="13.5" font-weight="400" fill="#334155" line-height="22">
      <tspan x="24" dy="0">Computer Science undergraduate and full-stack software builder from</tspan>
      <tspan x="24" dy="24">Kanpur, India. Dedicated to crafting production systems end-to-end</tspan>
      <tspan x="24" dy="24">with React, Node.js, and MongoDB, bridging algorithmic foundations</tspan>
      <tspan x="24" dy="24">with modern AI automation workflows.</tspan>
    </text>

    <!-- Quote Box -->
    <g transform="translate(24, 168)">
      <rect x="0" y="0" width="462" height="46" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <rect x="0" y="0" width="4" height="46" rx="2" fill="url(#accentLine)"/>
      <text x="16" y="28" class="font-sans" font-size="12.5" font-weight="600" fill="#1E293B" font-style="italic">
        "Write clean code. Solve real problems. Ship meaningful products."
      </text>
    </g>
  </g>

  <!-- Right Column: 3 Pillars -->
  <g transform="translate(575, 82)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="320" height="70" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#EEF2FF"/>
      <text x="22" y="40" class="font-sans" font-size="14">⚡</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">Software Craftsmanship</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Modular architectures &amp; scalable code</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="320" height="70" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#F0FDF4"/>
      <text x="22" y="40" class="font-sans" font-size="14">🧠</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">DSA &amp; Problem Solving</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Algorithmic efficiency &amp; optimization</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(0, 164)">
      <rect x="0" y="0" width="320" height="71" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="35" r="16" fill="#FAF5FF"/>
      <text x="22" y="40" class="font-sans" font-size="14">🤖</text>
      <text x="56" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">AI &amp; Smart Automation</text>
      <text x="56" y="48" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Intelligent tools &amp; workflow pipelines</text>
    </g>
  </g>
</svg>'''

with open('assets/about.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)

print('Wrote uniform light assets/about.svg')

# -------------------------------------------------------------
# 3. TECH STACK SVG (UNIFORM CLEAN LIGHT THEME)
# -------------------------------------------------------------
stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <filter id="stackShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="8" y="8" width="924" height="464" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#stackShadow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="115" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">02 // TECH STACK</text>
    <text x="130" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Skills &amp; Technologies in Action</text>
  </g>

  <!-- Category 1: LANGUAGES -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="415" height="170" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#4F46E5"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">LANGUAGES</text>
    <text x="330" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">5 Core</text>

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
  <g transform="translate(480, 80)">
    <rect x="0" y="0" width="415" height="170" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#06B6D4"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">WEB DEVELOPMENT</text>
    <text x="330" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">5 Tools</text>

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
    <rect x="0" y="0" width="415" height="170" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#10B981"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">DEV TOOLS &amp; PLATFORMS</text>
    <text x="330" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">3 Tools</text>

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
        <rect x="0" y="0" width="120" height="44" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
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
  <g transform="translate(480, 270)">
    <rect x="0" y="0" width="415" height="170" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="18" y="18" width="6" height="18" rx="3" fill="#8B5CF6"/>
    <text x="32" y="32" class="font-sans" font-size="13" font-weight="800" fill="#0F172A" letter-spacing="0.5">AI &amp; APPLIED COMPUTING</text>
    <text x="320" y="32" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">3 Domains</text>

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
        <text x="40" y="27" class="font-sans" font-size="12.5" font-weight="700" fill="#6D28D9">Comp Vision</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

print('Wrote uniform light assets/stack.svg')

# -------------------------------------------------------------
# 4. PROJECTS SVG (UNIFORM CLEAN LIGHT THEME)
# -------------------------------------------------------------
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 450" width="100%" height="100%">
  <defs>
    <filter id="pCardShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="8" y="8" width="924" height="434" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#pCardShadow)"/>

  <!-- Section Header -->
  <g transform="translate(45, 36)">
    <rect x="0" y="0" width="158" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">03 // CURRENTLY BUILDING</text>
    <text x="175" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Active Engineering &amp; Development Tracks</text>
  </g>

  <!-- 3 Project / Focus Cards -->
  <!-- Card 1: AttendX -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="270" height="325" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Badges -->
    <rect x="18" y="18" width="45" height="22" rx="6" fill="#EFF6FF"/>
    <text x="30" y="33" class="font-sans" font-size="11" font-weight="800" fill="#2563EB">01</text>
    <rect x="175" y="18" width="75" height="22" rx="11" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <text x="185" y="33" class="font-sans" font-size="10" font-weight="700" fill="#065F46">DEPLOYED</text>

    <!-- Title & Domain -->
    <text x="18" y="75" class="font-sans" font-size="16.5" font-weight="800" fill="#0F172A">AttendX &amp; Web Apps</text>
    <text x="18" y="96" class="font-sans" font-size="12" font-weight="600" fill="#4F46E5">Full-Stack Production Suite</text>

    <!-- Description -->
    <text x="18" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="18" dy="0">Shipped smart attendance system</tspan>
      <tspan x="18" dy="20">with AI face biometric verification,</tspan>
      <tspan x="18" dy="20">dynamic QR codes, and GPS geofencing</tspan>
      <tspan x="18" dy="20">with React, Node.js &amp; Tailwind.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(18, 230)">
      <rect x="0" y="0" width="55" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">React</text>

      <rect x="62" y="0" width="60" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Node.js</text>

      <rect x="129" y="0" width="55" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="137" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">AI-Face</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="18" y1="275" x2="250" y2="275" stroke="#E2E8F0" stroke-width="1"/>
    <text x="18" y="302" class="font-sans" font-size="12" font-weight="700" fill="#2563EB">Live Production App →</text>
  </g>

  <!-- Card 2: AI / Automation -->
  <g transform="translate(335, 80)">
    <rect x="0" y="0" width="270" height="325" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Badges -->
    <rect x="18" y="18" width="45" height="22" rx="6" fill="#FAF5FF"/>
    <text x="30" y="33" class="font-sans" font-size="11" font-weight="800" fill="#9333EA">02</text>
    <rect x="165" y="18" width="85" height="22" rx="11" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="175" y="33" class="font-sans" font-size="10" font-weight="700" fill="#6D28D9">AUTOMATING</text>

    <!-- Title & Domain -->
    <text x="18" y="75" class="font-sans" font-size="16.5" font-weight="800" fill="#0F172A">AI &amp; Automation</text>
    <text x="18" y="96" class="font-sans" font-size="12" font-weight="600" fill="#9333EA">Intelligent Workflow Scripts</text>

    <!-- Description -->
    <text x="18" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="18" dy="0">Integrating smart AI APIs, vision</tspan>
      <tspan x="18" dy="20">processing, and custom Python automation</tspan>
      <tspan x="18" dy="20">to replace manual developer tasks with</tspan>
      <tspan x="18" dy="20">seamless intelligent pipelines.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(18, 230)">
      <rect x="0" y="0" width="60" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="9" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Python</text>

      <rect x="67" y="0" width="60" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="75" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">AI APIs</text>

      <rect x="134" y="0" width="55" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="142" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Vision</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="18" y1="275" x2="250" y2="275" stroke="#E2E8F0" stroke-width="1"/>
    <text x="18" y="302" class="font-sans" font-size="12" font-weight="700" fill="#9333EA">Smart Workflows →</text>
  </g>

  <!-- Card 3: Problem Solving -->
  <g transform="translate(625, 80)">
    <rect x="0" y="0" width="270" height="325" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Badges -->
    <rect x="18" y="18" width="45" height="22" rx="6" fill="#F0FDF4"/>
    <text x="30" y="33" class="font-sans" font-size="11" font-weight="800" fill="#16A34A">03</text>
    <rect x="165" y="18" width="85" height="22" rx="11" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="175" y="33" class="font-sans" font-size="10" font-weight="700" fill="#166534">PRACTICING</text>

    <!-- Title & Domain -->
    <text x="18" y="75" class="font-sans" font-size="16.5" font-weight="800" fill="#0F172A">Problem Solving</text>
    <text x="18" y="96" class="font-sans" font-size="12" font-weight="600" fill="#16A34A">Data Structures &amp; Algorithms</text>

    <!-- Description -->
    <text x="18" y="130" class="font-sans" font-size="12.5" font-weight="400" fill="#475569">
      <tspan x="18" dy="0">Practicing core algorithms in Java and C.</tspan>
      <tspan x="18" dy="20">Focusing on computational complexity,</tspan>
      <tspan x="18" dy="20">space-time optimization, and solid</tspan>
      <tspan x="18" dy="20">foundations for clean systems code.</tspan>
    </text>

    <!-- Tech Chips -->
    <g transform="translate(18, 230)">
      <rect x="0" y="0" width="50" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Java</text>

      <rect x="57" y="0" width="40" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="70" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">C</text>

      <rect x="104" y="0" width="85" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="114" y="16" class="font-sans" font-size="10.5" font-weight="600" fill="#334155">Algorithms</text>
    </g>

    <!-- Bottom Indicator -->
    <line x1="18" y1="275" x2="250" y2="275" stroke="#E2E8F0" stroke-width="1"/>
    <text x="18" y="302" class="font-sans" font-size="12" font-weight="700" fill="#16A34A">Core Foundations →</text>
  </g>
</svg>'''

with open('assets/projects.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)

print('Wrote uniform light assets/projects.svg')

# -------------------------------------------------------------
# 5. STATS & WORKFLOW SVG (UNIFORM CLEAN LIGHT THEME)
# -------------------------------------------------------------
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 330" width="100%" height="100%">
  <defs>
    <filter id="stShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="8" y="8" width="924" height="314" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#stShadow)"/>

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
      <rect x="0" y="0" width="200" height="110" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#EFF6FF"/>
      <text x="21" y="35" class="font-sans" font-size="13">🧠</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#2563EB">ALGORITHMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">DSA Mastery</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Java &amp; C Logic</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(216, 0)">
      <rect x="0" y="0" width="200" height="110" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#ECFDF5"/>
      <text x="21" y="35" class="font-sans" font-size="13">⚡</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#059669">ARCHITECTURE</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">Clean Code</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Modular &amp; Scalable</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(432, 0)">
      <rect x="0" y="0" width="200" height="110" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#FAF5FF"/>
      <text x="21" y="35" class="font-sans" font-size="13">🌐</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#7C3AED">WEB SYSTEMS</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">Full-Stack Dev</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">React &amp; Node.js</text>
    </g>

    <!-- Pillar 4 -->
    <g transform="translate(648, 0)">
      <rect x="0" y="0" width="202" height="110" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="30" r="14" fill="#FFF7ED"/>
      <text x="21" y="35" class="font-sans" font-size="13">🚀</text>
      <text x="52" y="32" class="font-sans" font-size="11" font-weight="700" fill="#EA580C">INNOVATION</text>
      <text x="20" y="70" class="font-sans" font-size="14" font-weight="800" fill="#0F172A">AI Automation</text>
      <text x="20" y="90" class="font-sans" font-size="11.5" font-weight="500" fill="#64748B">Pipelines &amp; Vision</text>
    </g>
  </g>

  <!-- Flow Visualizer Band -->
  <g transform="translate(45, 210)">
    <rect x="0" y="0" width="850" height="85" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    
    <text x="20" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#475569" letter-spacing="0.5">DEV PIPELINE RHYTHM</text>
    <text x="720" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#10B981">● ACTIVE ITERATION</text>

    <!-- Visual Progress Tracks -->
    <g transform="translate(20, 44)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="190" height="22" rx="6" fill="#EEF2FF"/>
      <text x="14" y="15" class="font-sans" font-size="11" font-weight="700" fill="#4F46E5">1. Deep Problem Solving</text>
      
      <text x="200" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 2 -->
      <rect x="220" y="0" width="190" height="22" rx="6" fill="#F0F9FF"/>
      <text x="234" y="15" class="font-sans" font-size="11" font-weight="700" fill="#0284C7">2. Architectural Design</text>

      <text x="420" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 3 -->
      <rect x="440" y="0" width="190" height="22" rx="6" fill="#F5F3FF"/>
      <text x="454" y="15" class="font-sans" font-size="11" font-weight="700" fill="#7C3AED">3. Implementation &amp; Test</text>

      <text x="640" y="16" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">→</text>

      <!-- Step 4 -->
      <rect x="660" y="0" width="150" height="22" rx="6" fill="#ECFDF5"/>
      <text x="674" y="15" class="font-sans" font-size="11" font-weight="700" fill="#059669">4. Ship &amp; Iterate</text>
    </g>
  </g>
</svg>'''

with open('assets/stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)

print('Wrote uniform light assets/stats.svg')

# -------------------------------------------------------------
# 6. CONNECT SVG (STRICT TWO COLUMNS: TEXT LEFT, IMAGE RIGHT)
# -------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 370" width="100%" height="100%">
  <defs>
    <filter id="cShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.04"/>
    </filter>
    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .point-char {{ animation: gentlePoint 4s ease-in-out infinite; }}
      @keyframes gentlePoint {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(-5px); }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .point-char {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Container -->
  <rect x="8" y="8" width="924" height="354" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cShadow)"/>

  <!-- LEFT COLUMN: STRICTLY x=45 to x=515 (TEXT & CARDS ONLY) -->
  <g transform="translate(45, 38)">
    <!-- Section Header -->
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#EEF2FF"/>
    <text x="10" y="16" class="font-sans" font-size="10.5" font-weight="800" fill="#4F46E5" letter-spacing="0.5">05 // GET IN TOUCH</text>
    <text x="142" y="17" class="font-sans" font-size="18" font-weight="800" fill="#0F172A" letter-spacing="-0.3">Let's Build Something Together</text>
    
    <text x="0" y="52" class="font-sans" font-size="13" font-weight="400" fill="#475569">
      Open for collaborations, developer networking, and software opportunities.
    </text>

    <!-- Social Cards on Left (Width: 470px) -->
    <g transform="translate(0, 72)">
      <!-- GitHub Card -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="470" height="46" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#0F172A"/>
        <text x="18" y="28" class="font-sans" font-size="12" font-weight="700" fill="#FFFFFF">🐙</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0F172A">GitHub (@rajdixit070-v)</text>
        <text x="220" y="28" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— Repositories &amp; Open Source</text>
        <text x="440" y="28" class="font-sans" font-size="14" font-weight="700" fill="#2563EB">→</text>
      </g>

      <!-- LinkedIn Card -->
      <g transform="translate(0, 56)">
        <rect x="0" y="0" width="470" height="46" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#0A66C2"/>
        <text x="18" y="28" class="font-sans" font-size="11" font-weight="800" fill="#FFFFFF">in</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#0A66C2">LinkedIn (Raj Dixit)</text>
        <text x="210" y="28" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— Professional Network &amp; Career</text>
        <text x="440" y="28" class="font-sans" font-size="14" font-weight="700" fill="#0A66C2">→</text>
      </g>

      <!-- Portfolio Card -->
      <g transform="translate(0, 112)">
        <rect x="0" y="0" width="470" height="46" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="24" cy="23" r="12" fill="#7C3AED"/>
        <text x="17" y="28" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌐</text>
        <text x="48" y="28" class="font-sans" font-size="13" font-weight="700" fill="#7C3AED">Portfolio &amp; Shipped Apps</text>
        <text x="230" y="28" class="font-sans" font-size="12" font-weight="500" fill="#64748B">— AttendX, LibSphere &amp; Live Demos</text>
        <text x="440" y="28" class="font-sans" font-size="14" font-weight="700" fill="#7C3AED">→</text>
      </g>
    </g>

    <!-- Subnote -->
    <text x="0" y="260" class="font-sans" font-size="12" font-weight="600" fill="#64748B">
      👇 Direct clickable links available in Markdown immediately below
    </text>
  </g>

  <!-- RIGHT COLUMN: STRICTLY x=580 to x=900 (IMAGE ONLY - NEVER OVERLAPPING TEXT) -->
  <g transform="translate(585, 20)" class="point-char">
    <!-- Pointing character strictly in the right area -->
    <image href="data:image/png;base64,{pointing_left_b64}" x="25" y="10" width="300" height="300" preserveAspectRatio="xMidYMid meet"/>

    <!-- Speech bubble on right side pointing toward left -->
    <g transform="translate(0, 18)">
      <rect x="0" y="0" width="165" height="34" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" filter="url(#cShadow)"/>
      <text x="14" y="22" class="font-sans" font-size="12" font-weight="700" fill="#1E293B">👈 Let's connect!</text>
    </g>
  </g>
</svg>'''

with open('assets/connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print('Wrote uniform light assets/connect.svg with separate columns')
