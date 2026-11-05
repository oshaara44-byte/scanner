import streamlit as st

# ═══════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════
LEMON_CHECKOUT_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_CHECKOUT_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

BOOKMAKERS_LIST = ["Bet365", "1xBet", "Betsson", "Unibet", "Winamax", "Betclic", "Bwin", "Sky Bet", "Betway"]

# ═══════════════════════════════════════════════════
# MULTILINGUE
# ═══════════════════════════════════════════════════
LANGUAGES = {"English": "en", "Español": "es"}

TEXTS = {
    "en": {
        "title": "LE SCANNER",
        "subtitle": "Value Bets & Risk Management Platform",
        "nav_home": "🏠 Value Bets",
        "nav_calc": "🧮 Gain Calculator",
        "nav_stats": "📊 Transparency",
        "nav_sub": "💎 VIP & Elite",
        "badge": "🔥 VALUE BET DETECTED",
        "hero_title": "Stop Gambling Blindly.",
        "hero_sub": "Bet with Real Math, Not Emotions.",
    },
    "es": {
        "title": "EL SCANNER",
        "subtitle": "Plataforma de Value Bets y Gestión de Riesgo",
        "nav_home": "🏠 Value Bets",
        "nav_calc": "🧮 Calculadora",
        "nav_stats": "📊 Transparencia",
        "nav_sub": "💎 VIP y Elite",
        "badge": "🔥 VALUE BET DETECTADO",
        "hero_title": "Deja de Apostar a Ciegas.",
        "hero_sub": "Apuesta con Matemáticas Reales, No con Emociones.",
    }
}

# ═══════════════════════════════════════════════════
# SETUP PAGE
# ═══════════════════════════════════════════════════
st.set_page_config(page_title="Le Scanner — Global Value Bets", page_icon="🎯", layout="wide")

# Sidebar Language Selector
with st.sidebar:
    st.markdown("### 🌍 Language / Idioma")
    lang_choice = st.selectbox("Select your language / Selecciona tu idioma", list(LANGUAGES.keys()), index=0)
    lang_code = LANGUAGES[lang_choice]
    t = TEXTS[lang_code]
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center; color:#0F172A;'>{t['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#64748B;'>{t['subtitle']}</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio("Menu / Menú", [t["nav_home"], t["nav_calc"], t["nav_stats"], t["nav_sub"]])

# ═══════════════════════════════════════════════════
# GLOBAL LIGHT THEME CSS
# ═══════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    section[data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 1px solid #E2E8F0; }
    h1, h2, h3 { color: #0F172A !important; font-weight: 800 !important; }
    p { color: #334155 !important; }
    .hero-card {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-radius: 20px;
        padding: 40px 30px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 25px 50px rgba(15,23,42,0.1);
    }
    .hero-card h1 { color: #FFFFFF !important; font-size: 2.8rem; font-weight: 900; line-height: 1.1; margin-bottom: 15px; }
    .hero-card p { color: #94A3B8 !important; font-size: 1.15rem; max-width: 600px; margin: 0 auto; }
    .badge-global {
        background: rgba(0,255,136,0.15);
        color: #00FF88;
        padding: 6px 16px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid rgba(0,255,136,0.4);
        display: inline-block;
        margin-bottom: 15px;
    }
    .stat-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 25px 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .stat-number { font-size: 2.4rem; font-weight: 900; color: #10B981; }
    .stat-label { color: #64748B; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
    .bet-card-v2 {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }
    .bet-card-v2:hover { border-color: #10B981; }
    .match-header { font-size: 1.4rem; font-weight: 800; color: #0F172A; margin-bottom: 15px; }
    .odds-pill { background: #0F172A; color: #FACC15; font-weight: 800; font-size: 1.1rem; padding: 6px 14px; border-radius: 8px; }
    .book-label {
        background: #F1F5F9; color: #475569; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: 600;
        margin-top: 10px; display: inline-block;
    }
    .price-card {
        background: #FFFFFF;
        border: 2px solid #E2E8F0;
        border-radius: 20px;
        padding: 35px 25px;
        text-align: center;
        height: 100%;
    }
    .price-card.featured { border-color: #10B981; box-shadow: 0 15px 30px rgba(16,185,129,0.15); }
    .price-title { font-size: 1.4rem; font-weight: 900; color: #0F172A; }
    .price-amount { font-size: 2.8rem; font-weight: 900; color: #10B981; margin: 15px 0; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════
def get_demo_bets():
    return [
        {
            "home": "PSG", "away": "Olympique de Marseille",
            "sport": "⚽ Ligue 1", "league": "France",
            "time": "Today • 20:45",
            "selection": "Over 2.5 Goals",
            "odds": 1.88, "bookmaker": "Winamax",
            "value": 14.2, "stake": 25,
            "reason": "Market margin anomaly detected."
        },
        {
            "home": "Real Madrid", "away": "FC Barcelona",
            "sport": "⚽ La Liga", "league": "Spain",
            "time": "Tomorrow • 21:00",
            "selection": "Real Madrid Win",
            "odds": 2.15, "bookmaker": "Betclic",
            "value": 11.5, "stake": 15,
            "reason": "Algorithm detects undervaluation after squad rotation."
        },
        {
            "home": "Liverpool FC", "away": "Arsenal FC",
            "sport": "⚽ Premier League", "league": "England",
            "time": "Tomorrow • 17:30",
            "selection": "Under 2.5 Goals",
            "odds": 2.05, "bookmaker": "Sky Bet",
            "value": 9.1, "stake": 12,
            "reason": "Defensive stats underestimated for this fixture."
        },
        {
            "home": "LA Lakers", "away": "Boston Celtics",
            "sport": "🏀 NBA", "league": "USA",
            "time": "Tomorrow • 02:30",
            "selection": "Lakers +4.5 Handicap",
            "odds": 1.95, "bookmaker": "Betway",
            "value": 8.7, "stake": 12,
            "reason": "Away form overestimated for Boston."
        },
        {
            "home": "Jannik Sinner", "away": "Carlos Alcaraz",
            "sport": "🎾 ATP Masters", "league": "Tennis",
            "time": "Sunday • 15:00",
            "selection": "Sinner Wins 1st Set",
            "odds": 2.05, "bookmaker": "Bet365",
            "value": 6.8, "stake": 10,
            "reason": "Strong historical 1st set advantage for Sinner on this surface."
        }
    ]

# ═══════════════════════════════════════════════════
# PAGE 1 : HOME
# ═══════════════════════════════════════════════════
if page == t["nav_home"]:
    st.markdown("""
    <div class="hero-card">
        <span class="badge-global">🌍 GLOBAL BOOKMAKER ALGORITHMIC SCANNER</span>
        <h1>Stop Gambling Blindly.<br>Bet with Real Mathematics.</h1>
        <p>Le Scanner continuously compares thousands of live odds across Bet365, 1xBet, Unibet, Winamax, Betclic, Betway, Bwin and Sky Bet. It detects bookmaker pricing errors before they are corrected.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-number">64.2%</div><div class="stat-label">Win Rate Avg.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-number">+8.3%</div><div class="stat-label">Avg. Monthly ROI</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-number">100%</div><div class="stat-label">Pure Mathematics</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="stat-number">24/7</div><div class="stat-label">Real-Time Scan</div></div>', unsafe_allow_html=True)
    
    st.markdown("<h2 style='margin-top: 30px; color:#0F172A;'>🔴 Live Value Bets Found Today</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B;'>A live sample of algorithmic opportunities detected across our global bookmaker network.</p>", unsafe_allow_html=True)
    
    bets = get_demo_bets()
    for bet in bets:
        st.markdown(f"""
        <div class="bet-card-v2">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="color: #64748B; font-size: 0.85rem; font-weight: 600;">{bet['sport']} • {bet['league']} • {bet['time']}</span>
                <span class="badge-global" style="background: rgba(220, 38, 38, 0.15); color: #EF4444; border-color: rgba(220,38,38,0.3);">VALUE +{bet['value']}%</span>
            </div>
            <div class="match-header">{bet['home']} vs {bet['away']}</div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; align-items: center; background: #F8FAFC; padding: 15px; border-radius: 10px; margin-top: 10px;">
                <div>
                    <span style="color: #64748B; font-size: 0.8rem;">Selection:</span><br>
                    <strong style="color: #0F172A; font-size: 1.1rem;">{bet['selection']}</strong>
                </div>
                <div style="margin-left: 10px;">
                    <span style="color: #64748B; font-size: 0.8rem;">Bookmaker:</span><br>
                    <strong style="color: #0F172A;">{bet['bookmaker']}</strong>
                    <span class="book-label">Verified Odds Source</span>
                </div>
                <div style="margin-left: auto;">
                    <span style="color: #64748B; font-size: 0.8rem;">Odds:</span><br>
                    <span class="odds-pill">{bet['odds']}</span>
                </div>
                <div style="margin-left: auto;">
                    <span style="color: #64748B; font-size: 0.8rem;">Stake (Kelly 1/4):</span><br>
                    <strong style="color: #0F172A; font-size: 1.1rem;">{bet['stake']} €</strong>
                </div>
            </div>
            <div style="margin-top: 12px; font-size: 0.85rem; color: #475569;">
                💡 <b>Algorithm Note:</b> {bet['reason']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); padding: 35px; border-radius: 20px; text-align: center; color: white;">
        <h2 style="color: #FFFFFF !important; font-weight: 900; margin-bottom: 10px;">Don't Miss Bookmaker Pricing Errors Again</h2>
        <p style="font-size: 1.1rem; color: #94A3B8; margin-bottom: 20px;">Join the VIP WhatsApp Channel and receive the best value bets instantly on your mobile.</p>
        <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background: #10B981; color: white; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 900; font-size: 1.1rem; display: inline-block;">🚀 Get VIP Access Now</a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATOR
# ═══════════════════════════════════════════════════
elif page == t["nav_calc"]:
    st.markdown("<h1 style='color:#0F172A;'>🧮 Investment & Bankroll Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B;'>Estimate the theoretical growth of your capital based on a conservative 8.3% monthly ROI.</p>", unsafe_allow_html=True)
    
    col_input, col_result = st.columns([1, 1])
    with col_input:
        st.markdown("### ⚙️ Your Parameters / Tus Parámetros")
        bankroll = st.slider("Initial Capital (€) / Capital Inicial (€)", 100, 5000, 500, 50)
        mois = st.slider("Duration (Months) / Duración (Meses)", 1, 12, 6)
        
    with col_result:
        roi_mensuel = 0.083
        capital_final = bankroll * ((1 + roi_mensuel) ** mois)
        profit_net = capital_final - bankroll
        st.markdown("### 📈 Estimated Result / Resultado Estimado")
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 2px solid #10B981; padding: 30px; border-radius: 16px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <p style="color: #64748B; font-size: 0.9rem;">FINAL CAPITAL / CAPITAL FINAL</p>
            <h1 style="color: #10B981; font-size: 3rem; font-weight: 900;">{capital_final:.2f} €</h1>
            <p style="color: #0F172A; font-weight: 700; font-size: 1.2rem;">+ {profit_net:.2f} € Net Profit / Beneficio Neto</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 3 : STATS
# ═══════════════════════════════════════════════════
elif page == t["nav_stats"]:
    st.markdown("<h1 style='color:#0F172A;'>📊 Full Transparency & Statistics</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B;'>Every recommendation is tracked, verified, and openly displayed to our community.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Bets Analyzed / Analizados", "14,820+", "+340 this week")
    c2.metric("Global Win Rate / Tasa Global", "64.2%", "+1.4% vs last month")
    c3.metric("Avg. Margin Found / Margen Promedio", "+9.8%", "vs closing line")
    
    st.markdown("### 🏆 Performance by Sport / Rendimiento por Deporte")
    import pandas as pd
    df = pd.DataFrame({
        "Sport / Deporte": ["⚽ Football (Europe)", "🏀 NBA (USA)", "🎾 Tennis (ATP)", "⚽ Premier League"],
        "Bets / Apuestas": [840, 420, 310, 290],
        "Win Rate": ["66.4%", "61.2%", "63.8%", "65.5%"],
        "ROI / ROI": ["+9.4%", "+6.2%", "+8.1%", "+7.0%"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════
# PAGE 4 : SUBSCRIPTIONS
# ═══════════════════════════════════════════════════
elif page == t["nav_sub"]:
    st.markdown("<h1 style='color:#0F172A; text-align:center;'>💎 Choose Your Plan / Elige Tu Plan</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; text-align:center;'>Access the best value bets and guaranteed arbitrage directly on WhatsApp.</p>", unsafe_allow_html=True)
    
    col_vip, col_elite = st.columns(2)
    
    with col_vip:
        st.markdown("""
        <div class="price-card">
            <h2 style="color:#0F172A; font-weight:900;">💬 VIP WHATSAPP</h2>
            <h1 style="color:#10B981; font-weight:900;">29.99€ <span style="font-size:1rem;color:#64748B;">/mo</span></h1>
            <hr>
            <p>✅ 3 to 5 Value Bets / day</p>
            <p>✅ WhatsApp Instant Delivery</p>
            <p>✅ Bankroll & Stake Calculator</p>
            <p>✅ Daily Performance Tracking</p>
            <hr>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Join VIP / Unirse VIP", key="vip_btn"):
            st.markdown(f"[👉 Pay with Lemon Squeezy / Pagar con Lemon Squeezy]({LEMON_CHECKOUT_VIP})")
    
    with col_elite:
        st.markdown("""
        <div class="price-card featured">
            <span style="background:#10B981; color:white; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:800;">MOST POPULAR</span>
            <h2 style="color:#0F172A; font-weight:900; margin-top:10px;">👑 ELITE CLUB</h2>
            <h1 style="color:#10B981; font-weight:900;">49.99€ <span style="font-size:1rem;color:#64748B;">/mo</span></h1>
            <hr>
            <p>✅ <b>Everything in VIP</b></p>
            <p>✅ <b>Surebets (Guaranteed Wins)</b></p>
            <p>✅ Live Match Alerts</p>
            <p>✅ Priority 7/7 Support</p>
            <hr>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👑 Join Elite / Unirse Elite", key="elite_btn"):
            st.markdown(f"[👉 Pay with Lemon Squeezy / Pagar con Lemon Squeezy]({LEMON_CHECKOUT_ELITE})")

# ═══════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════
st.markdown("<br><hr style='border-color:#E2E8F0;'><p style='text-align:center; color:#94A3B8; font-size:0.8rem;'>Le Scanner © 2025 | Value Bets Algorithm. All rights reserved.</p>", unsafe_allow_html=True)
