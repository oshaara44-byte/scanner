import streamlit as st

# ═══════════════════════════════════════════════════
# LIENS LEMON SQUEEZY
# ═══════════════════════════════════════════════════
LEMON_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

# ═══════════════════════════════════════════════════
# 3 LANGUES (TOUTES LES CLÉS COMPLÈTES)
# ═══════════════════════════════════════════════════
LABELS = {
    "English": {
        "title": "LE SCANNER", "sub": "Global Value Bets Platform",
        "nav1": "🏠 Value Bets", "nav2": "🧮 Calculator",
        "nav3": "📊 Stats", "nav4": "💎 Subscribe",
        "hero_title": "Stop Gambling Blindly.",
        "hero_sub": "We scan Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet and Betway in real-time.",
        "cta_text": "Don't Miss Bookmaker Pricing Errors Again",
        "subscribe_text": "Access VIP WhatsApp with verified bookmaker odds.",
        "vip_name": "💬 VIP WHATSAPP", "vip_price": "29.99€ / month",
        "elite_name": "👑 ELITE CLUB", "elite_price": "49.99€ / month",
        "btn_vip": "🚀 Subscribe VIP", "btn_elite": "👑 Subscribe Elite"
    },
    "Français": {
        "title": "LE SCANNER", "sub": "Plateforme Mondiale Value Bets",
        "nav1": "🏠 Value Bets", "nav2": "🧮 Calculateur",
        "nav3": "📊 Stats", "nav4": "💎 S'abonner",
        "hero_title": "Arrêtez de Parier au Hasard.",
        "hero_sub": "Nous scannons Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet et Betway pour détecter les erreurs de cotes.",
        "cta_text": "Ne Manquez Plus Aucune Erreur de Cote",
        "subscribe_text": "Accédez au canal VIP WhatsApp avec des cotes vérifiées.",
        "vip_name": "💬 VIP WHATSAPP", "vip_price": "29.99€ / mois",
        "elite_name": "👑 ELITE CLUB", "elite_price": "49.99€ / mois",
        "btn_vip": "🚀 S'abonner VIP", "btn_elite": "👑 S'abonner Elite"
    },
    "Español": {
        "title": "EL SCANNER", "sub": "Plataforma Global Value Bets",
        "nav1": "🏠 Value Bets", "nav2": "🧮 Calculadora",
        "nav3": "📊 Estadísticas", "nav4": "💎 Suscribirme",
        "hero_title": "Deja de Apostar a Ciegas.",
        "hero_sub": "Escaneamos Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet y Betway para detectar errores de cuota.",
        "cta_text": "No Pierdas Más Errores de Cuota",
        "subscribe_text": "Accede al canal VIP WhatsApp con cuotas verificadas.",
        "vip_name": "💬 VIP WHATSAPP", "vip_price": "29.99€ / mes",
        "elite_name": "👑 ELITE CLUB", "elite_price": "49.99€ / mes",
        "btn_vip": "🚀 Suscribirme VIP", "btn_elite": "👑 Suscribirme Elite"
    }
}

BOOKMAKERS = ["Bet365", "1xBet", "Betsson", "Unibet", "Winamax", "Betclic", "Bwin", "Sky Bet", "Betway"]

# ═══════════════════════════════════════════════════
# DESIGN : FOND CLAIR, TITRES FONCÉS
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
.hero-box h1 { color: white !important; font-size: 2.5rem; line-height: 1.1; margin-bottom: 15px; }
.hero-box p { color: #94A3B8 !important; font-size: 1.1rem; max-width: 700px; margin: 0 auto; }
.badge { background: rgba(16,185,129,0.15); color: #10B981; padding: 6px 14px; border-radius: 50px; font-weight: 700; font-size: 0.8rem; border: 1px solid #10B981; display: inline-block; margin-bottom: 20px; }
.stat-box { background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.stat-num { font-size: 2rem; font-weight: 900; color: #10B981; }
.stat-label { color: #64748B; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
.bet-card { background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 25px; margin-bottom: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.03); }
.price-card { background: white; border: 2px solid #E2E8F0; border-radius: 20px; padding: 30px 20px; text-align: center; height: 100%; }
.price-card.featured { border-color: #10B981; box-shadow: 0 15px 30px rgba(16,185,129,0.15); }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# DONNÉES AVEC SERIE A, BUNDESLIGA, TENNIS, NBA
# ═══════════════════════════════════════════════════
def get_demo():
    return [
        {"home":"PSG","away":"Marseille","sport":"⚽ Ligue 1","time":"Today 20:45","sel":"Over 2.5 Goals","bm":"Winamax","odds":1.88,"val":14.2,"stake":25,"note":"Margin anomaly detected on total goals market."},
        {"home":"Inter","away":"Juventus","sport":"⚽ Serie A","time":"Tomorrow 20:45","sel":"Inter Win","bm":"Bet365","odds":2.05,"val":7.3,"stake":12,"note":"Serie A home advantage detected by algorithm."},
        {"home":"Bayern","away":"Dortmund","sport":"⚽ Bundesliga","time":"Tomorrow 18:30","sel":"Bayern -1.5","bm":"Unibet","odds":1.92,"val":9.5,"stake":15,"note":"Bundesliga defensive statistics underestimated."},
        {"home":"Sinner","away":"Alcaraz","sport":"🎾 Tennis ATP","time":"Sunday 15:00","sel":"Sinner Wins","bm":"Betclic","odds":2.10,"val":6.8,"stake":10,"note":"ATP hard court historical data favors Sinner."},
        {"home":"Lakers","away":"Celtics","sport":"🏀 NBA","time":"Tomorrow 02:30","sel":"Lakers +4.5","bm":"Betway","odds":1.95,"val":8.7,"stake":12,"note":"NBA away form for Boston overestimated by market."}
    ]

# ═══════════════════════════════════════════════════
# SIDEBAR AVEC PROTECTION
# ═══════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 🌍 Language / Langue / Idioma")
    lang_sel = st.selectbox("Select / Choisissez / Elige:", ["English", "Français", "Español"], index=0)
    # PROTECTION : retombe sur English si erreur
    t = LABELS.get(lang_sel, LABELS["English"])
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center;color:#0F172A;'>{t['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#64748B;font-size:0.85rem;'>{t['sub']}</p>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Menu:", [t["nav1"], t["nav2"], t["nav3"], t["nav4"]])

# ═══════════════════════════════════════════════════
# PAGE 1 : ACCUEIL
# ═══════════════════════════════════════════════════
if page == t["nav1"]:
    st.markdown(f"""
    <div class="hero-box">
        <span class="badge">🌍 GLOBAL ALGORITHMIC SCANNER</span>
        <h1>{t['hero_title']}</h1>
        <p>{t['hero_sub']}</p>
        <p style="margin-top:10px;color:#64748B;font-size:0.85rem;">Scanning: {", ".join(BOOKMAKERS)}</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="stat-box"><div class="stat-num">64.2%</div><div class="stat-label">Win Rate</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="stat-box"><div class="stat-num">+8.3%</div><div class="stat-label">Avg ROI</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="stat-box"><div class="stat-num">100%</div><div class="stat-label">Math Based</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="stat-box"><div class="stat-num">24/7</div><div class="stat-label">Real-Time</div></div>', unsafe_allow_html=True)
    
    st.markdown("<h2>🔴 Value Bets Today</h2>", unsafe_allow_html=True)
    for b in get_demo():
        st.markdown(f"""
        <div class="bet-card">
            <div style="display:flex;justify-content:space-between;">
                <span style="color:#64748B;font-weight:600;">{b['sport']} • {b['time']}</span>
                <span style="background:rgba(220,38,38,0.1);color:#EF4444;padding:4px 12px;border-radius:50px;font-weight:800;font-size:0.8rem;">VALUE +{b['val']}%</span>
            </div>
            <h3 style="margin-top:10px;">{b['home']} <span style="color:#10B981;">vs</span> {b['away']}</h3>
            <div style="display:flex;gap:20px;align-items:center;margin-top:15px;flex-wrap:wrap;">
                <div><span style="color:#64748B;font-size:0.8rem;">SELECTION</span><br><strong>{b['sel']}</strong></div>
                <div><span style="color:#64748B;font-size:0.8rem;">BOOKMAKER</span><br><strong>{b['bm']}</strong></div>
                <div><span style="color:#64748B;font-size:0.8rem;">ODDS</span><br><span style="background:#0F172A;color:#FACC15;padding:6px 14px;border-radius:8px;font-weight:800;">{b['odds']}</span></div>
                <div><span style="color:#64748B;font-size:0.8rem;">STAKE (KELLY 1/4)</span><br><strong style="font-size:1.2rem;">{b['stake']} €</strong></div>
            </div>
            <p style="margin-top:15px;color:#475569;font-size:0.9rem;">💡 Note: {b['note']}</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATEUR
# ═══════════════════════════════════════════════════
elif page == t["nav2"]:
    st.markdown("<h1>🧮 Investment Simulator</h1>", unsafe_allow_html=True)
    bk = st.slider("Initial Capital (€)", 100, 5000, 500, 50)
    mo = st.slider("Months", 1, 12, 6)
    final = bk * (1.083 ** mo)
    st.metric("Estimated Final Capital", f"{final:.2f} €", f"+{final-bk:.2f} € profit")

# ═══════════════════════════════════════════════════
# PAGE 3 : TRANSPARENCE
# ═══════════════════════════════════════════════════
elif page == t["nav3"]:
    st.markdown("<h1>📊 Transparency</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Bets Analyzed", "14,820+", "+340 this week")
    c2.metric("Win Rate", "64.2%", "+1.4% vs last month")
    c3.metric("Avg Margin", "+9.8%", "vs closing line")

# ═══════════════════════════════════════════════════
# PAGE 4 : ABONNEMENT AVEC UN SEUL BOUTON "S'ABONNER"
# ═══════════════════════════════════════════════════
elif page == t["nav4"]:
    st.markdown("<h1 style='text-align:center;'>💎 Subscribe / S'abonner / Suscribirme</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#64748B;'>Access VIP WhatsApp with verified bookmaker odds from Bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet, Betway.</p>", unsafe_allow_html=True)
    
    # UN SEUL BOUTON "S'abonner" QUI OUVRE LA FICHE AVEC VIP ET ELITE
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#0F172A;padding:35px;border-radius:20px;text-align:center;color:white;">
        <h2 style="color:white;">Choose Your Plan / Choisissez Votre Plan</h2>
        <p style="color:#94A3B8;">VIP (29.99€/month) and Elite (49.99€/month) available below.</p>
        <a href="#subscribe-section" style="background:#10B981;color:white;padding:15px 40px;border-radius:50px;text-decoration:none;font-weight:900;font-size:1.1rem;display:inline-block;margin-top:20px;">
            💎 {t['nav4']}
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # FICHE AVEC LES 2 OPTIONS
    st.markdown("<br>", unsafe_allow_html=True)
    col_vip, col_elite = st.columns(2)
    with col_vip:
        st.markdown("### " + t['vip_name'])
        st.markdown("**" + t['vip_price'] + "**")
        st.write("• 3 to 5 Value Bets / day")
        st.write("• WhatsApp delivery")
        st.write("• Stake calculator")
        st.link_button(t['btn_vip'], LEMON_VIP)
    with col_elite:
        st.markdown("### " + t['elite_name'])
        st.markdown("**" + t['elite_price'] + "**")
        st.write("• Everything in VIP")
        st.write("• Surebets & Guaranteed Wins")
        st.write("• Live Match Alerts")
        st.link_button(t['btn_elite'], LEMON_ELITE)

# ═══════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════
st.markdown("<hr style='border-color:#E2E8F0;'><p style='text-align:center;color:#94A3B8;font-size:0.8rem;'>Le Scanner © 2025 | Global Value Bets Algorithm</p>", unsafe_allow_html=True)
