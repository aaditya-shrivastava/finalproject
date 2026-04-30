# import streamlit as st

# st.set_page_config(
#     page_title="Manufacturing AI Platform",
#     page_icon="🏭",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # ── Ports — change these to match your Docker/K8s service URLs ──
# MULTIMODAL_URL  = "http://13.202.61.65:8080/manufacturing-creator/"
# MULTIAGENT_URL  = "http://13.202.61.65:8080/multi-agent-manufacturing/"  

# st.markdown("""
# <style>
#     html, body, [class*="css"] { background-color: #0f1117; }
#     .stApp { background-color: #0f1117; }
#     section[data-testid="stSidebar"] { display: none; }

#     .badge {
#         display: inline-block;
#         background: #1a1d27;
#         border: 0.5px solid #2a2d3a;
#         border-radius: 20px;
#         color: #888;
#         font-size: 0.75rem;
#         padding: 4px 14px;
#         letter-spacing: 0.5px;
#         margin-bottom: 1rem;
#     }
#     .main-title {
#         font-size: 2.2rem;
#         font-weight: 700;
#         color: #ffffff;
#         text-align: center;
#         margin: 0 0 0.4rem 0;
#     }
#     .main-sub {
#         font-size: 1rem;
#         color: #666;
#         text-align: center;
#         margin-bottom: 2.5rem;
#     }
#     .tool-card {
#         background: #1a1d27;
#         border: 1px solid #2a2d3a;
#         border-radius: 14px;
#         padding: 1.8rem 1.6rem;
#         text-align: left;
#         transition: border-color 0.2s;
#     }
#     .tool-card:hover { border-color: #00d4ff; }
#     .tool-card .icon {
#         font-size: 1.8rem;
#         margin-bottom: 0.8rem;
#     }
#     .tool-card h3 {
#         color: #e8e8e8;
#         font-size: 1.1rem;
#         margin: 0 0 0.5rem 0;
#     }
#     .tool-card p {
#         color: #666;
#         font-size: 0.85rem;
#         line-height: 1.6;
#         margin: 0 0 1rem 0;
#     }
#     .tool-card .tags span {
#         display: inline-block;
#         background: #12161f;
#         border: 0.5px solid #2a2d3a;
#         color: #555;
#         font-size: 0.72rem;
#         padding: 2px 10px;
#         border-radius: 20px;
#         margin-right: 4px;
#     }
#     .footer {
#         text-align: center;
#         color: #333;
#         font-size: 0.75rem;
#         margin-top: 3rem;
#     }
#     div[data-testid="stLinkButton"] a {
#         background: linear-gradient(135deg, #00d4ff, #0099cc) !important;
#         color: #000 !important;
#         font-weight: 700 !important;
#         border: none !important;
#         border-radius: 8px !important;
#         padding: 0.55rem 1.4rem !important;
#         font-size: 0.9rem !important;
#         text-decoration: none !important;
#         display: inline-block;
#     }
# </style>
# """, unsafe_allow_html=True)


# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown('<div style="text-align:center"><span class="badge"> Datagami &nbsp;·&nbsp; Group 12D1</span></div>', unsafe_allow_html=True)
# st.markdown('<div class="main-title">🏭 Manufacturing AI Platform</div>', unsafe_allow_html=True)
# st.markdown('<div class="main-sub">Select a tool to get started</div>', unsafe_allow_html=True)


# # ── Tool Cards ────────────────────────────────────────────────────────────────
# col1, col2 = st.columns(2, gap="large")

# with col1:
#     st.markdown("""
#     <div class="tool-card">
#         <div class="icon">🖼️</div>
#         <h3>Multimodal Creator</h3>
#         <p>Enter a manufacturing concept and get a detailed technical narrative along with a photorealistic visual prototype.</p>
#         <div class="tags">
#             <span>GPT-4o-mini</span>
#             <span>DALL·E 3</span>
#             <span>ChromaDB</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.link_button("Open Multimodal Creator →", MULTIMODAL_URL, use_container_width=True)

# with col2:
#     st.markdown("""
#     <div class="tool-card">
#         <div class="icon">🔍</div>
#         <h3>Multi-Agent Research</h3>
#         <p>test Describe your manufacturing needs and AI agents will research suppliers, pricing, and generate a full procurement report.</p>
#         <div class="tags">
#             <span>CrewAI</span>
#             <span>Llama 3.3</span>
#             <span>DuckDuckGo</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.link_button("Open Multi-Agent Research →", MULTIAGENT_URL, use_container_width=True)


# # ── Footer ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="footer">
#     Powered by GPT-4o · DALL·E 3 · CrewAI · Llama 3.3 · Streamlit
# </div>
# """, unsafe_allow_html=True)




import streamlit as st

st.set_page_config(
    page_title="Manufacturing AI Platform",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

MULTIMODAL_URL = "http://13.202.61.65:8080/manufacturing-creator/"
MULTIAGENT_URL = "http://13.202.61.65:8080/multi-agent-manufacturing/"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"], .stApp {
    background-color: #0e0f14 !important;
    font-family: 'Space Grotesk', sans-serif;
}
section[data-testid="stSidebar"] { display: none !important; }
.block-container { padding-top: 1rem !important; max-width: 900px !important; padding-left: 1rem !important; padding-right: 1rem !important; }

/* ── Background grid ── */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(99,102,241,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,102,241,0.04) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    z-index: 0;
}

/* ── Top orb glow ── */
.stApp::after {
    content: '';
    position: fixed;
    top: -80px;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 360px;
    background: radial-gradient(ellipse, rgba(99,102,241,0.1) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    animation: orb-pulse 6s ease-in-out infinite;
}
@keyframes orb-pulse {
    0%, 100% { opacity: 0.6; transform: translateX(-50%) scale(1); }
    50%       { opacity: 1;   transform: translateX(-50%) scale(1.1); }
}

/* ── Navbar ── */
.navbar {
    position: relative;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.1rem 2rem;
    margin-top: 1rem;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    background: rgba(255,255,255,0.02);
    animation: fade-down 0.5s ease both;
}
.nav-logo { font-family: 'Space Mono', monospace; font-size: .8rem; font-weight: 700; color: #fff; letter-spacing: 2px; }
.nav-logo span { color: #818cf8; }
.nav-pill { background: rgba(99,102,241,0.1); border: 1px solid rgba(99,102,241,0.2); border-radius: 999px; padding: 4px 14px; font-size: .6rem; color: #818cf8; letter-spacing: 2px; font-family: 'Space Mono', monospace; }
.nav-live { display: flex; align-items: center; gap: 6px; font-size: .6rem; color: rgba(255,255,255,0.3); font-family: 'Space Mono', monospace; letter-spacing: 1px; }
.live-dot { width: 5px; height: 5px; border-radius: 50%; background: #22d3ee; box-shadow: 0 0 8px #22d3ee; animation: lv 2s ease-in-out infinite; display: inline-block; }
@keyframes lv { 0%,100%{opacity:1} 50%{opacity:.3} }

/* ── Hero ── */
.hero { position: relative; z-index: 5; text-align: center; padding: 2.5rem 2rem 1.8rem; animation: fade-down 0.6s 0.1s ease both; }
.hero-tag { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 4px; padding: 5px 14px; font-size: .62rem; color: rgba(255,255,255,0.3); letter-spacing: 3px; font-family: 'Space Mono', monospace; margin-bottom: 1.3rem; text-transform: uppercase; }
.hero-title { font-size: 2.4rem; font-weight: 700; color: #fff; line-height: 1.1; margin-bottom: .5rem; letter-spacing: -1px; }
.hero-title .accent { background: linear-gradient(135deg, #818cf8, #22d3ee); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-desc { font-size: .85rem; color: rgba(255,255,255,0.25); max-width: 420px; margin: 0 auto 2rem; line-height: 1.7; font-weight: 300; }

.stats-row { display: flex; justify-content: center; gap: 1px; margin-bottom: 2.8rem; }
.stat-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: .7rem 1.6rem; text-align: center; }
.stat-box:first-child { border-radius: 8px 0 0 8px; }
.stat-box:last-child  { border-radius: 0 8px 8px 0; }
.stat-val { font-family: 'Space Mono', monospace; font-size: 1.2rem; font-weight: 700; color: #818cf8; }
.stat-lbl { font-size: .58rem; color: rgba(255,255,255,0.2); letter-spacing: 2px; text-transform: uppercase; margin-top: 2px; }

/* ── Cards ── */
.card {
    position: relative;
    border-radius: 16px;
    padding: 2rem 1.8rem 1.6rem;
    cursor: pointer;
    transition: transform 0.1s ease, box-shadow 0.1s ease;
    will-change: transform;
    animation: fade-up 0.7s 0.2s ease both;
}
.card-1 {
    background: linear-gradient(145deg, #13152b, #0e1020);
    border: 1px solid rgba(99,102,241,0.2);
    box-shadow: 0 2px 0 0 rgba(99,102,241,0.4), 0 8px 32px rgba(99,102,241,0.15), 0 24px 60px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.06);
}
.card-2 {
    background: linear-gradient(145deg, #1a1020, #120d1a);
    border: 1px solid rgba(236,72,153,0.2);
    box-shadow: 0 2px 0 0 rgba(236,72,153,0.4), 0 8px 32px rgba(236,72,153,0.12), 0 24px 60px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.06);
}
.card-shine { position: absolute; top: 0; left: 0; right: 0; height: 50%; border-radius: 16px 16px 0 0; background: linear-gradient(180deg, rgba(255,255,255,0.04) 0%, transparent 100%); pointer-events: none; }
.card-glow-1 { position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%); pointer-events: none; }
.card-glow-2 { position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(236,72,153,0.15) 0%, transparent 70%); pointer-events: none; }

.card-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.3rem; }
.card-num { font-family: 'Space Mono', monospace; font-size: .6rem; font-weight: 700; padding: 3px 10px; border-radius: 4px; }
.card-1 .card-num { background: rgba(99,102,241,0.12); color: #818cf8; border: 1px solid rgba(99,102,241,0.2); }
.card-2 .card-num { background: rgba(236,72,153,0.12); color: #ec4899; border: 1px solid rgba(236,72,153,0.2); }
.card-icon-ring { width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 18px; }
.card-1 .card-icon-ring { background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.2); box-shadow: 0 4px 16px rgba(99,102,241,0.2); }
.card-2 .card-icon-ring { background: rgba(236,72,153,0.12); border: 1px solid rgba(236,72,153,0.2); box-shadow: 0 4px 16px rgba(236,72,153,0.2); }

.card-title { font-size: 1.1rem; font-weight: 700; color: #f0f0ff; margin-bottom: .5rem; letter-spacing: -.3px; }
.card-desc  { font-size: .78rem; color: rgba(255,255,255,0.25); line-height: 1.7; margin-bottom: 1.2rem; font-weight: 300; }
.card-tags  { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 1.3rem; }
.tag        { font-size: .62rem; font-weight: 500; padding: 3px 10px; border-radius: 6px; }
.card-1 .tag { background: rgba(99,102,241,0.08); border: 1px solid rgba(99,102,241,0.15); color: rgba(129,140,248,0.7); }
.card-2 .tag { background: rgba(236,72,153,0.08); border: 1px solid rgba(236,72,153,0.15); color: rgba(236,72,153,0.7); }

.layer-hint  { position: absolute; bottom: -6px;  left: 10px; right: 10px; height: 10px; border-radius: 0 0 16px 16px; opacity: .4; }
.layer-hint2 { position: absolute; bottom: -11px; left: 20px; right: 20px; height: 10px; border-radius: 0 0 16px 16px; opacity: .2; }
.card-1 .layer-hint  { background: rgba(79,70,229,0.3); }
.card-1 .layer-hint2 { background: rgba(79,70,229,0.2); }
.card-2 .layer-hint  { background: rgba(219,39,119,0.3); }
.card-2 .layer-hint2 { background: rgba(219,39,119,0.2); }

/* ── Streamlit link buttons ── */
div[data-testid="stLinkButton"] a {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
    padding: .58rem !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: .75rem !important;
    font-weight: 600 !important;
    letter-spacing: .3px !important;
    border: none !important;
    color: #fff !important;
    text-decoration: none !important;
    transition: opacity .2s !important;
}
div[data-testid="stLinkButton"]:nth-of-type(1) a {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    box-shadow: 0 4px 20px rgba(79,70,229,0.4) !important;
}
div[data-testid="stLinkButton"]:nth-of-type(2) a {
    background: linear-gradient(135deg, #db2777, #9d174d) !important;
    box-shadow: 0 4px 20px rgba(219,39,119,0.4) !important;
}
div[data-testid="stLinkButton"] a:hover { opacity: .85 !important; }

/* ── Footer ── */
.footer { position: relative; z-index: 5; text-align: center; padding: 1.2rem 2rem 1.6rem; animation: fade-in 1s 0.4s ease both; }
.footer-inner { display: flex; align-items: center; justify-content: center; gap: 8px; flex-wrap: wrap; }
.f-chip { font-family: 'Space Mono', monospace; font-size: .58rem; color: rgba(255,255,255,0.15); padding: 3px 10px; border: 1px solid rgba(255,255,255,0.05); border-radius: 4px; letter-spacing: .5px; }

/* ── Keyframes ── */
@keyframes fade-down { from { opacity: 0; transform: translateY(-14px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fade-up   { from { opacity: 0; transform: translateY(18px);  } to { opacity: 1; transform: translateY(0); } }
@keyframes fade-in   { from { opacity: 0; } to { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

# ── Navbar ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="nav-logo">DATA<span>GAMI</span></div>
    <div class="nav-pill">GRP · 12D1</div>
    <div class="nav-live"><span class="live-dot"></span>LIVE</div>
</div>
""", unsafe_allow_html=True)

# ── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">🏭 &nbsp; Datagami · Group 12D1</div>
    <div class="hero-title">Manufacturing <span class="accent">AI Platform</span></div>
    <div class="hero-desc">Select a tool to get started</div>
    <div class="stats-row">
        <div class="stat-box"><div class="stat-val">2</div><div class="stat-lbl">AI Tools</div></div>
        <div class="stat-box"><div class="stat-val">4+</div><div class="stat-lbl">Models</div></div>
        <div class="stat-box"><div class="stat-val">∞</div><div class="stat-lbl">Possibilities</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Cards ───────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="card card-1" id="c1">
        <div class="card-shine"></div>
        <div class="card-glow-1"></div>
        <div class="layer-hint"></div>
        <div class="layer-hint2"></div>
        <div class="card-top">
            <span class="card-num">MODULE 01</span>
            <div class="card-icon-ring">🖼️</div>
        </div>
        <div class="card-title">Multimodal Creator</div>
        <div class="card-desc">Enter a manufacturing concept and get a detailed technical narrative along with a photorealistic visual prototype.</div>
        <div class="card-tags">
            <span class="tag">GPT-4o-mini</span>
            <span class="tag">DALL·E 3</span>
            <span class="tag">ChromaDB</span>
        </div>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.link_button("Open Multimodal Creator →", MULTIMODAL_URL, use_container_width=True)

with col2:
    st.markdown("""
    <div class="card card-2" id="c2">
        <div class="card-shine"></div>
        <div class="card-glow-2"></div>
        <div class="layer-hint"></div>
        <div class="layer-hint2"></div>
        <div class="card-top">
            <span class="card-num">MODULE 02</span>
            <div class="card-icon-ring">🔍</div>
        </div>
        <div class="card-title">Multi-Agent Research</div>
        <div class="card-desc">Describe your manufacturing needs and AI agents will research suppliers, pricing, and generate a full procurement report.</div>
        <div class="card-tags">
            <span class="tag">CrewAI</span>
            <span class="tag">Llama 3.3</span>
            <span class="tag">DuckDuckGo</span>
        </div>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.link_button("Open Multi-Agent Research →", MULTIAGENT_URL, use_container_width=True)

# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-inner">
        <span class="f-chip">GPT-4o</span>
        <span class="f-chip">DALL·E 3</span>
        <span class="f-chip">CrewAI</span>
        <span class="f-chip">Llama 3.3</span>
        <span class="f-chip">Streamlit</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 3D Tilt JS ──────────────────────────────────────────────────────────────
st.markdown("""
<script>
function tiltCard(card, e) {
    const r = card.getBoundingClientRect();
    const x = e.clientX - r.left;
    const y = e.clientY - r.top;
    const cx = r.width / 2;
    const cy = r.height / 2;
    const rotY = ((x - cx) / cx) * 10;
    const rotX = -((y - cy) / cy) * 10;
    card.style.transform = `translateY(-10px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
    card.style.boxShadow = card.id === 'c1'
        ? `0 2px 0 0 rgba(99,102,241,0.6), 0 20px 60px rgba(99,102,241,0.3), 0 40px 80px rgba(0,0,0,0.7)`
        : `0 2px 0 0 rgba(236,72,153,0.6), 0 20px 60px rgba(236,72,153,0.25), 0 40px 80px rgba(0,0,0,0.7)`;
}
function resetCard(card) {
    card.style.transform = 'translateY(0) rotateX(0deg) rotateY(0deg)';
    card.style.boxShadow = '';
}
function initTilt() {
    ['c1','c2'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('mousemove', e => tiltCard(el, e));
            el.addEventListener('mouseleave', () => resetCard(el));
        }
    });
}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTilt);
} else {
    initTilt();
}
</script>
""", unsafe_allow_html=True)