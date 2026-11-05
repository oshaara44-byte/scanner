import streamlit as st

# ═══════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════
LEMON_CHECKOUT_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_CHECKOUT_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

# ═══════════════════════════════════════════════════
# MULTILINGUE : ANGLAIS (défaut) + ESPAGNOL
# ═══════════════════════════════════════════════════
LANGS = {
    "English": "en",
    "Español": "es"
}

TEXT = {
    "en": {
        "title": "LE SCANNER",
        "subtitle": "Value Bets & Risk Management",
        "nav_home": "Home & Value Bets",
        "nav_calc": "Gain Calculator",
        "nav_stats": "Transparency",
        "nav_sub": "VIP & Elite",
        "hero": "Stop Gambling Blindly. Bet with Real Mathematics.",
        "sub_hero": "We scan Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet and Betway in real-time.",
        "cta": "Don't Miss Bookmaker Pricing Errors Again"
    },
    "es": {
        "title": "EL SCANNER",
        "subtitle": "Value Bets y Gestión de Riesgo",
        "nav_home": "Inicio y Value Bets",
        "nav_calc": "Calculadora",
        "nav_stats": "Transparencia",
        "nav_sub": "VIP y Elite",
        "hero": "Deja de Apostar a Ciegas. Apuesta con Matemáticas Reales.",
        "sub_hero": "Escaneamos Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet y Betway en tiempo real.",
        "cta": "No Pierdas Más Errores de Cuota"
    }
}

# ═══════════════════════════════════════════════════
# STYLE : FOND CLAIR + TITRES COLORÉS
# ═══════════════════════════════════════════════════
st.set_page_config(page_title="Le Scanner — Global", page_icon="🎯", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
* { font-family: 'Inter', sans-serif; }
.stApp { background-color: #F8FAFC; }
section[data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 2px solid #E2E8F0; }
h1, h2, h3 { color: #0F172A !important; font-weight: 900 !important; }
.hero-box {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    border-radius: 24px; padding: 50px 30px; color: white; text-align: center;
    box-shadow: 0 25px 50px rgba(15,23,42,0.15); margin-bottom: 30px;
}
.hero-box h1 { color: white !important; font-size: 3rem; line-height: 1.1; margin-bottom: 15px; }
.hero-box p { color: #94A3B8 !important; font-size: 1.2rem; max-width: 700px; margin: 0 auto; }
.badge { background: rgba(16,185,129,0.15); color: #10B981; padding: 6px 14px; border-radius: 50px; font-weight: 700; font-size: 0.8rem; border: 1px solid #10B981; display: inline-block; margin-bottom: 20px; }
.stat-box { background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.stat-num { font-size: 2.2rem; font-weight: 900; color: #10B981; }
.stat-label { color: #64748B; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }
.bet-card { background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 25px; margin-bottom: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.03); }
.price-card { background: white; border: 2px solid #E2E8F0; border-radius: 20px; padding: 35px 25px; text-align: center; height: 100%; }
.price-card.featured { border-color: #10B981; box-shadow: 0 15px 30px rgba(16,185,129,0.15); }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# SIDEBAR : LANGUE + NAVIGATION
# ═══════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 🌍 Language / Idioma")
    lang_name = st.selectbox("Choose / Elige", list(TEXT.keys()), index=0)
    t = TEXT[LANGS[lang_name]]
    
    st.markdown("---")
    st.markdown(f"<h2 style='color:#0F172A; text-align:center;'>{t['title']}</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; text-align:center;'>Value Bets Algorithm</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio("Menu / Menú", [
        t["nav_home"], t["nav_calc"], t["nav_stats"], t["nav_sub"]
    ])

# ═══════════════════════════════════════════════════
# DONNÉES DÉMO (avec bookmakers mondiaux)
# ═══════════════════════════════════════════════════
def get_demo_bets():
    return [
        {
            "home": "PSG", "away": "Marseille",
            "sport": "⚽ Ligue 1", "time": "Today • 20:45",
            "selection": "Over 2.5 Goals",
            "bookmaker": "Winamax", "odds": 1.88,
            "value": 14.2, "stake": 25,
            "analysis": "Anomalie de marge détectée sur le marché des totaux."
        },
        {
            "home": "Real Madrid", "away": "Barcelona",
            "sport": "⚽ La Liga", "time": "Tomorrow • 21:00",
            "selection": "Real Madrid Win",
            "bookmaker": "Bet365", "odds": 2.15,
            "value": 11.5, "stake": 15,
            "analysis": "Sous-évaluation détectée après rotation d'effectif."
        },
        {
            "home": "Liverpool", "away": "Arsenal",
            "sport": "⚽ Premier League", "time": "Tomorrow • 17:30",
            "selection": "Under 2.5 Goals",
            "bookmaker": "Sky Bet", "odds": 2.05,
            "value": 9.1, "stake": 12,
            "analysis": "Statistiques défensives sous-estimées par le bookmaker."
        },
        {
            "home": "Lakers", "away": "Celtics",
            "sport": "🏀 NBA", "time": "Tomorrow • 02:30",
            "selection": "Lakers +4.5",
            "bookmaker": "Betway", "odds": 1.95,
            "value": 8.7, "stake": 12,
            "analysis": "Performance extérieure de Boston surestimée selon notre modèle."
        }
    ]

# ═══════════════════════════════════════════════════
# LISTE DES BOOKMAKERS MONDIAUX
# ═══════════════════════════════════════════════════
BOOKMAKERS_GLOBAL = ["Bet365", "1xBet", "Betsson", "Unibet", "Winamax", "Betclic", "Bwin", "Sky Bet", "Betway"]

# ═══════════════════════════════════════════════════
# PAGE 1 : ACCUEIL
# ═══════════════════════════════════════════════════
if page == t["nav_home"]:
    st.markdown(f"""
    <div class="hero-box">
        <span class="badge">🌍 GLOBAL ALGORITHMIC SCANNER</span>
        <h1>{t['hero']}</h1>
        <p>{t['sub_hero']}</p>
        <p style="margin-top:15px; font-size:0.85rem; color:#64748B;">
            Scanning: {", ".join(BOOKMAKERS_GLOBAL)}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="stat-box"><div class="stat-num">64.2%</div><div class="stat-label">Win Rate</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="stat-box"><div class="stat-num">+8.3%</div><div class="stat-label">Avg ROI</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="stat-box"><div class="stat-num">100%</div><div class="stat-label">Math Based</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="stat-box"><div class="stat-num">24/7</div><div class="stat-label">Real-Time</div></div>', unsafe_allow_html=True)

    st.markdown("<h2 style='margin-top:30px;'>🔴 Live Value Bets Found Today</h2>", unsafe_allow_html=True)
    
    for bet in get_demo_bets():
        with st.container():
            st.markdown(f"""
            <div class="bet-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#64748B; font-size:0.85rem; font-weight:600;">{bet['sport']} • {bet['time']}</span>
                    <span style="background:rgba(220,38,38,0.1); color:#EF4444; padding:4px 12px; border-radius:50px; font-weight:800; font-size:0.8rem;">VALUE +{bet['value']}%</span>
                </div>
                <h3 style="margin-top:10px; color:#0F172A;">{bet['home']} <span style="color:#10B981;">vs</span> {bet['away']}</h3>
                <div style="display:flex; gap:20px; flex-wrap:wrap; margin-top:15px; align-items:center;">
                    <div>
                        <span style="color:#64748B; font-size:0.8rem;">SELECTION:</span><br>
                        <strong style="color:#0F172A;">{bet['selection']}</strong>
                    </div>
                    <div>
                        <span style="color:#64748B; font-size:0.8rem;">BOOKMAKER:</span><br>
                        <strong style="color:#0F172A;">{bet['bookmaker']}</strong>
                    </div>
                    <div style="margin-left:auto;">
                        <span style="color:#64748B; font-size:0.8rem;">ODDS:</span><br>
                        <span style="background:#0F172A; color:#FACC15; padding:6px 14px; border-radius:8px; font-weight:800; font-size:1.2rem;">{bet['odds']}</span>
                    </div>
                    <div>
                        <span style="color:#64748B; font-size:0.8rem;">STAKE (KELLY 1/4):</span><br>
                        <strong style="color:#0F172A; font-size:1.2rem;">{bet['stake']} €</strong>
                    </div>
                </div>
                <p style="margin-top:15px; color:#475569; font-size:0.9rem;">💡 <b>Note:</b> {bet['analysis']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#0F172A; padding:35px; border-radius:20px; text-align:center; color:white;">
        <h2 style="color:white;">{t['cta']}</h2>
        <p style="color:#94A3B8; margin-bottom:20px;">Join the VIP WhatsApp Channel and receive the best value bets instantly.</p>
        <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background:#10B981; color:white; padding:15px 35px; border-radius:50px; text-decoration:none; font-weight:900; font-size:1.1rem;">🚀 Get VIP Access</a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATEUR
# ═══════════════════════════════════════════════════
elif page == t["nav_calc"]:
    st.markdown("<h1>🧮 Investment Simulator</h1>", unsafe_allow_html=True)
    bankroll = st.slider("Initial Capital (€)", 100, 5000, 500, 50)
    mois = st.slider("Duration (Months)", 1, 12, 6)
    final = bankroll * (1.083 ** mois)
    st.metric("Estimated Final Capital", f"{final:.2f} €", f"+{final-bankroll:.2f} €")

# ═══════════════════════════════════════════════════
# PAGE 3 : TRANSPARENCE
# ═══════════════════════════════════════════════════
elif page == t["nav_stats"]:
    st.markdown("<h1>📊 Transparency & Performance</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Bets Analyzed", "14,820+")
    c2.metric("Win Rate", "64.2%")
    c3.metric("Avg Margin", "+9.8%")

# ═══════════════════════════════════════════════════
# PAGE 4 : ABONNEMENT (DEUX BOUTONS CLAIRS, CÔTE À CÔTE)
# ═══════════════════════════════════════════════════
elif page == t["nav_sub"]:
    st.markdown("<h1 style='text-align:center;'>💎 Choose Your Plan</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💬 VIP WHATSAPP")
        st.markdown("**29.99€ / month**")
        st.write("• 3 to 5 Value Bets per day")
        st.write("• WhatsApp delivery")
        st.write("• Stake calculator included")
        st.write("• Daily tracking report")
        if st.button("🚀 Subscribe VIP", key="vip", use_container_width=True):
            st.markdown(f"[👉 Pay with Lemon Squeezy (VIP)]({LEMON_CHECKOUT_VIP})")
    
    with col2:
        st.markdown("### 👑 ELITE CLUB")
        st.markdown("**49.99€ / month**")
        st.write("• Everything in VIP")
        st.write("• Surebets & Guaranteed Wins")
        st.write("• Live Match Alerts")
        st.write("• Priority Support")
        if st.button("👑 Subscribe Elite", key="elite", use_container_width=True):
            st.markdown(f"[👉 Pay with Lemon Squeezy (Elite)]({LEMON_CHECKOUT_ELITE})")
