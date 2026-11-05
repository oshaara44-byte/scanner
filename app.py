import streamlit as st
from datetime import datetime

# ═══════════════════════════════════════════════════
# CONFIGURATION & LIENS
# ═══════════════════════════════════════════════════
ODDS_API_KEY = "ta_cle_ici"

LEMON_CHECKOUT_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_CHECKOUT_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

# Bookmakers mondiaux scannés (affichés dans le hero)
BOOKMAKERS = "bet365, 1xBet, Betsson, Unibet, Winamax, Betclic, Bwin, Sky Bet & Betway"

# ═══════════════════════════════════════════════════
# SYSTÈME DE TRADUCTION (EN par défaut + ES)
# ═══════════════════════════════════════════════════
T = {
    "en": {
        "app_tagline": "Value Bets Algorithm V4.2",
        "nav_home": "🏠 Home & Value Bets",
        "nav_calc": "🧮 Profit Calculator",
        "nav_stats": "📊 Transparency & Stats",
        "nav_offers": "💎 VIP & Elite Plans",
        "guarantee_title": "🔒 100% Guarantee",
        "guarantee_text": "No emotional tips. Only mathematics and odds anomalies.",
        "hero_badge": "🔥 ARBITRAGE & VALUE BETS ALGORITHM",
        "hero_title_1": "Stop Gambling on Luck.",
        "hero_title_2": "Bet on Mathematics.",
        "hero_sub": "The Scanner scans thousands of odds in real time on " + BOOKMAKERS + " and spots bookmaker errors before they correct them.",
        "stat_winrate": "Average Win Rate",
        "stat_roi": "Average Monthly ROI",
        "stat_math": "Mathematical",
        "stat_247": "Real-Time Scan",
        "bets_title": "🔥 Opportunities Detected Today",
        "bets_sub": "Here is a preview of the Value Bets identified by our algorithm:",
        "card_selection": "Selection",
        "card_odds": "Bookmaker Odds",
        "card_stake": "Recommended Stake (Kelly)",
        "card_value": "VALUE",
        "cta_title": "Never Miss an Odds Edge Again!",
        "cta_text": "Join the VIP WhatsApp channel and receive the best odds instantly on your phone.",
        "cta_button": "🚀 Get Instant VIP Access",
        "calc_title": "🧮 Investment Simulator",
        "calc_sub": "Estimate the theoretical growth of your capital using the Kelly Criterion and an average 8.3% monthly ROI.",
        "calc_bankroll": "Your Initial Capital (€)",
        "calc_months": "Investment Duration (Months)",
        "calc_final": "ESTIMATED FINAL CAPITAL",
        "calc_profit": "estimated net profit",
        "calc_disclaimer": "⚠️ Sports betting involves risk. These estimates are based on our average statistical history and are not an absolute guarantee.",
        "stats_title": "📊 History & Transparency",
        "stats_sub": "Every bet recommended by our algorithm is archived and verifiable.",
        "stat_total": "Total Bets Analyzed",
        "stat_winrate2": "Overall Success Rate",
        "stat_margin": "Average Detected Margin",
        "stats_table_title": "🏆 Performance by Discipline",
        "th_discipline": "Discipline",
        "th_bets": "Number of Bets",
        "th_winrate": "Win Rate",
        "th_roi": "Net ROI",
        "offers_title": "💎 Choose Your Access Plan",
        "offers_sub": "Make your subscription profitable from your first Value Bets.",
        "vip_title": "💬 VIP WHATSAPP",
        "vip_sub": "Ideal for regular bettors",
        "vip_f1": "3 to 5 Value Bets per day",
        "vip_f2": "Instant delivery on WhatsApp",
        "vip_f3": "Stake calculation (Kelly)",
        "vip_f4": "Weekly report & tracking",
        "vip_x1": "Surebets & Arbitrage",
        "vip_x2": "Live match alerts",
        "vip_btn": "🚀 Join the VIP",
        "elite_badge": "🔥 MOST POPULAR",
        "elite_title": "👑 ELITE CLUB",
        "elite_sub": "To maximize your profits",
        "elite_f1": "Everything in the VIP plan",
        "elite_f2": "Surebets (guaranteed wins)",
        "elite_f3": "Live alerts during matches",
        "elite_f4": "Personalized Kelly bankroll + 7/7 priority support",
        "elite_btn": "👑 Join the Elite Club",
        "guarantee_box_title": "🛡️ Our Guarantees",
        "guarantee_box_text": "💳 100% secure payment via Lemon Squeezy  •  🔄 Cancel in 1 click  •  📊 Full transparency of results",
        "bet1_time": "Today • 8:45 PM",
        "bet1_sel": "Over 2.5 Goals",
        "bet1_reason": "Anomaly margin detected: market odds at 1.68 vs Winamax 1.88.",
        "bet2_time": "Tomorrow • 9:00 PM",
        "bet2_sel": "Real Madrid Win",
        "bet2_reason": "The algorithm detects an undervaluation of Real Madrid after rotation.",
        "bet3_time": "Tomorrow • 2:30 AM",
        "bet3_sel": "Lakers +4.5 Handicap",
        "bet3_reason": "Boston's away form is overestimated according to our model.",
    },
    "es": {
        "app_tagline": "Algoritmo de Value Bets V4.2",
        "nav_home": "🏠 Inicio & Value Bets",
        "nav_calc": "🧮 Calculadora de Ganancias",
        "nav_stats": "📊 Transparencia y Stats",
        "nav_offers": "💎 Planes VIP y Elite",
        "guarantee_title": "🔒 Garantía 100%",
        "guarantee_text": "Sin pronósticos emocionales. Solo matemáticas y anomalías de cuotas.",
        "hero_badge": "🔥 ALGORITMO DE ARBITRAJE Y VALUE BETS",
        "hero_title_1": "Deja de Apostar por Suerte.",
        "hero_title_2": "Aposta con Matemáticas.",
        "hero_sub": "The Scanner analiza miles de cuotas en tiempo real en " + BOOKMAKERS + " y detecta los errores de los bookies antes de que los corrijan.",
        "stat_winrate": "Tasa de Éxito Media",
        "stat_roi": "ROI Mensual Medio",
        "stat_math": "Matemático",
        "stat_247": "Escaneo en Tiempo Real",
        "bets_title": "🔥 Oportunidades Detectadas Hoy",
        "bets_sub": "Aquí tienes una vista previa de los Value Bets identificados por nuestro algoritmo:",
        "card_selection": "Selección",
        "card_odds": "Cuota del Bookie",
        "card_stake": "Apuesta Recomendada (Kelly)",
        "card_value": "VALUE",
        "cta_title": "¡No Pierdas Ninguna Ventaja de Cuota!",
        "cta_text": "Únete al canal VIP de WhatsApp y recibe las mejores cuotas al instante en tu teléfono.",
        "cta_button": "🚀 Obtén Acceso VIP Instantáneo",
        "calc_title": "🧮 Simulador de Inversión",
        "calc_sub": "Estima el crecimiento teórico de tu capital con el Criterio de Kelly y un ROI medio del 8.3% mensual.",
        "calc_bankroll": "Tu Capital Inicial (€)",
        "calc_months": "Duración de la Inversión (Meses)",
        "calc_final": "CAPITAL FINAL ESTIMADO",
        "calc_profit": "de beneficio neto estimado",
        "calc_disclaimer": "⚠️ Las apuestas deportivas conllevan riesgo. Estas estimaciones se basan en nuestro historial estadístico medio y no son una garantía absoluta.",
        "stats_title": "📊 Historial y Transparencia",
        "stats_sub": "Cada apuesta recomendada por nuestro algoritmo está archivada y verificable.",
        "stat_total": "Total de Apuestas Analizadas",
        "stat_winrate2": "Tasa de Éxito Global",
        "stat_margin": "Margen Medio Detectado",
        "stats_table_title": "🏆 Rendimiento por Disciplina",
        "th_discipline": "Disciplina",
        "th_bets": "Número de Apuestas",
        "th_winrate": "Tasa de Éxito",
        "th_roi": "ROI Neto",
        "offers_title": "💎 Elige Tu Plan de Acceso",
        "offers_sub": "Haz rentable tu suscripción desde tus primeros Value Bets.",
        "vip_title": "💬 VIP WHATSAPP",
        "vip_sub": "Ideal para apostadores regulares",
        "vip_f1": "3 a 5 Value Bets al día",
        "vip_f2": "Entrega instantánea por WhatsApp",
        "vip_f3": "Cálculo de apuestas (Kelly)",
        "vip_f4": "Informe y seguimiento semanal",
        "vip_x1": "Surebets y Arbitraje",
        "vip_x2": "Alertas en vivo",
        "vip_btn": "🚀 Unirse al VIP",
        "elite_badge": "🔥 EL MÁS POPULAR",
        "elite_title": "👑 CLUB ELITE",
        "elite_sub": "Para maximizar tus ganancias",
        "elite_f1": "Todo lo del plan VIP",
        "elite_f2": "Surebets (ganancias garantizadas)",
        "elite_f3": "Alertas en vivo durante los partidos",
        "elite_f4": "Bankroll Kelly personalizado + soporte prioritario 7/7",
        "elite_btn": "👑 Unirse al Club Elite",
        "guarantee_box_title": "🛡️ Nuestras Garantías",
        "guarantee_box_text": "💳 Pago 100% seguro vía Lemon Squeezy  •  🔄 Cancelación en 1 clic  •  📊 Transparencia total de resultados",
        "bet1_time": "Hoy • 20:45",
        "bet1_sel": "Más de 2.5 Goles",
        "bet1_reason": "Margen de anomalía detectado: cuota de mercado en 1.68 vs Winamax 1.88.",
        "bet2_time": "Mañana • 21:00",
        "bet2_sel": "Gana Real Madrid",
        "bet2_reason": "El algoritmo detecta una subvaloración del Real Madrid tras la rotación.",
        "bet3_time": "Mañana • 02:30",
        "bet3_sel": "Lakers +4.5 Hándicap",
        "bet3_reason": "La forma a domicilio de Boston está sobreestimada según nuestro modelo.",
    },
}

def t(key):
    return T[st.session_state.lang].get(key, key)

# ═══════════════════════════════════════════════════
# CONFIGURATION STREAMLIT & STYLES (FOND CLAIR)
# ═══════════════════════════════════════════════════
st.set_page_config(
    page_title="The Scanner — Value Bets",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }

    .hero-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #ECFDF5 100%);
        border: 1px solid #A7F3D0;
        padding: 45px 30px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 20px 40px rgba(16,185,129,0.10);
    }
    .hero-title {
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #065F46 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        color: #475569 !important;
        font-size: 1.15rem !important;
        max-width: 720px;
        margin: 0 auto 20px auto;
    }
    .badge-value {
        background: #D1FAE5;
        color: #047857;
        padding: 6px 14px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #6EE7B7;
        display: inline-block;
    }
    .stat-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .stat-number { font-size: 2.2rem; font-weight: 900; color: #059669; }
    .stat-label { color: #64748B; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }

    .bet-card-v2 {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    }
    .match-header { font-size: 1.3rem; font-weight: 800; color: #0F172A; margin-bottom: 12px; }
    .odds-pill {
        background: #FEF3C7;
        color: #B45309;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 4px 12px;
        border-radius: 8px;
    }
    .price-card {
        background: #FFFFFF;
        border: 2px solid #E2E8F0;
        border-radius: 20px;
        padding: 35px 25px;
        text-align: center;
        height: 100%;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    }
    .price-card.featured {
        border-color: #059669;
        box-shadow: 0 12px 30px rgba(5,150,105,0.18);
    }
    .price-title { font-size: 1.5rem; font-weight: 800; color: #0F172A; }
    .price-amount { font-size: 2.8rem; font-weight: 900; color: #059669; margin: 15px 0; }

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# DONNÉES DE DÉMO (noms propres non traduits)
# ═══════════════════════════════════════════════════
def get_demo_bets():
    return [
        {
            "home": "PSG", "away": "Olympique de Marseille",
            "sport": "⚽ Ligue 1", "league": "France",
            "bookmaker": "Winamax", "odds": 1.88,
            "value": 14.2, "stake": 25, "stars": "⭐⭐⭐⭐⭐",
            "time_key": "bet1_time", "sel_key": "bet1_sel", "reason_key": "bet1_reason",
        },
        {
            "home": "Real Madrid", "away": "FC Barcelona",
            "sport": "⚽ La Liga", "league": "Spain",
            "bookmaker": "bet365", "odds": 2.15,
            "value": 11.5, "stake": 15, "stars": "⭐⭐⭐⭐",
            "time_key": "bet2_time", "sel_key": "bet2_sel", "reason_key": "bet2_reason",
        },
        {
            "home": "LA Lakers", "away": "Boston Celtics",
            "sport": "🏀 NBA", "league": "USA",
            "bookmaker": "1xBet", "odds": 1.95,
            "value": 8.7, "stake": 12, "stars": "⭐⭐⭐⭐",
            "time_key": "bet3_time", "sel_key": "bet3_sel", "reason_key": "bet3_reason",
        },
    ]

# ═══════════════════════════════════════════════════
# SIDEBAR : LANGUE + NAVIGATION
# ═══════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "en"

with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#047857; margin-bottom:2px;'>🎯 LE SCANNER</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#64748B; font-size:0.8rem; margin-top:0;'>{t('app_tagline')}</p>", unsafe_allow_html=True)
    st.markdown("---")

    lang_choice = st.selectbox(
        "🌐 Language / Idioma",
        ["🇬🇧 English", "🇪🇸 Español"],
        index=0 if st.session_state.lang == "en" else 1,
        key="lang_select"
    )
    st.session_state.lang = "en" if "English" in lang_choice else "es"

    st.markdown("---")
    page = st.radio(
        "",
        [t("nav_home"), t("nav_calc"), t("stats_title".replace("📊 ", "")) and t("nav_stats"), t("nav_offers")],
        index=0,
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown(f"""
    <div style="background:#ECFDF5; padding:15px; border-radius:12px; border:1px solid #A7F3D0;">
        <p style="color:#047857; font-weight:700; margin-bottom:5px;">{t('guarantee_title')}</p>
        <p style="color:#475569; font-size:0.8rem; margin:0;">{t('guarantee_text')}</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 1 : ACCUEIL & VALUE BETS
# ═══════════════════════════════════════════════════
if page == t("nav_home"):

    st.markdown(f"""
    <div class="hero-container">
        <span class="badge-value">{t('hero_badge')}</span>
        <h1 class="hero-title">{t('hero_title_1')}<br>{t('hero_title_2')}</h1>
        <p class="hero-subtitle">{t('hero_sub')}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-number">64.2%</div><div class="stat-label">{t("stat_winrate")}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-number">+8.3%</div><div class="stat-label">{t("stat_roi")}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">{t("stat_math")}</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="stat-box"><div class="stat-number">24/7</div><div class="stat-label">{t("stat_247")}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#047857;'>{t('bets_title')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748B;'>{t('bets_sub')}</p>", unsafe_allow_html=True)

    for bet in get_demo_bets():
        st.markdown(f"""
        <div class="bet-card-v2">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span style="color:#64748B; font-size:0.85rem; font-weight:600;">{bet['sport']} • {bet['league']} • {t(bet['time_key'])}</span>
                <span class="badge-value">{t('card_value')} : +{bet['value']}%</span>
            </div>
            <div class="match-header">{bet['home']} vs {bet['away']}</div>
            <div style="display:flex; flex-wrap:wrap; gap:15px; align-items:center; background:#F8FAFC; padding:15px; border-radius:12px; margin-top:10px; border:1px solid #E2E8F0;">
                <div>
                    <span style="color:#64748B; font-size:0.8rem;">{t('card_selection')} :</span><br>
                    <strong style="color:#059669; font-size:1.1rem;">{t(bet['sel_key'])}</strong>
                </div>
                <div style="margin-left:auto;">
                    <span style="color:#64748B; font-size:0.8rem;">{t('card_odds')} :</span><br>
                    <span class="odds-pill">{bet['odds']}</span> <span style="color:#64748B; font-size:0.85rem;">({bet['bookmaker']})</span>
                </div>
                <div style="margin-left:auto;">
                    <span style="color:#64748B; font-size:0.8rem;">{t('card_stake')} :</span><br>
                    <strong style="color:#0F172A; font-size:1.1rem;">{bet['stake']} €</strong>
                </div>
            </div>
            <div style="margin-top:12px; font-size:0.85rem; color:#475569;">💡 <b>{t(bet['reason_key'])}</b></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:linear-gradient(90deg, #059669 0%, #10B981 100%); padding:35px; border-radius:20px; text-align:center; color:#FFFFFF;">
        <h2 style="color:#FFFFFF !important; font-weight:900; margin-bottom:10px;">{t('cta_title')}</h2>
        <p style="font-size:1.1rem; font-weight:600; margin-bottom:20px; color:#ECFDF5;">{t('cta_text')}</p>
        <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background:#FFFFFF; color:#047857; padding:15px 35px; border-radius:50px; text-decoration:none; font-weight:900; font-size:1.1rem; display:inline-block; box-shadow:0 10px 20px rgba(0,0,0,0.15);">{t('cta_button')}</a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATEUR
# ═══════════════════════════════════════════════════
elif page == t("nav_calc"):
    st.markdown(f"<h1 style='color:#047857;'>{t('calc_title')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748B;'>{t('calc_sub')}</p>", unsafe_allow_html=True)

    bankroll = st.slider(t("calc_bankroll"), 100, 5000, 500, 50)
    mois = st.slider(t("calc_months"), 1, 12, 6)

    capital_final = bankroll * ((1 + 0.083) ** mois)
    profit_net = capital_final - bankroll

    st.markdown(f"""
    <div style="background:#FFFFFF; border:2px solid #059669; padding:30px; border-radius:18px; text-align:center; margin-top:20px; box-shadow:0 8px 24px rgba(5,150,105,0.12);">
        <p style="color:#64748B; font-size:0.9rem;">{t('calc_final')}</p>
        <h1 style="color:#059669; font-size:3rem; font-weight:900;">{capital_final:.2f} €</h1>
        <p style="color:#0284C7; font-weight:700; font-size:1.2rem;">+ {profit_net:.2f} € {t('calc_profit')}</p>
    </div>
    """, unsafe_allow_html=True)
    st.caption(t("calc_disclaimer"))

# ═══════════════════════════════════════════════════
# PAGE 3 : STATS
# ═══════════════════════════════════════════════════
elif page == t("nav_stats"):
    st.markdown(f"<h1 style='color:#047857;'>{t('stats_title')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748B;'>{t('stats_sub')}</p>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric(t("stat_total"), "14,820+")
    c2.metric(t("stat_winrate2"), "64.2%")
    c3.metric(t("stat_margin"), "+9.8%")

    st.markdown(f"<h3 style='color:#047857;'>{t('stats_table_title')}</h3>", unsafe_allow_html=True)
    import pandas as pd
    df = pd.DataFrame({
        t("th_discipline"): ["⚽ Football (Ligue 1 & Europe)", "🏀 Basketball (NBA)", "🎾 Tennis (ATP/WTA)", "🏉 Rugby (Top 14)"],
        t("th_bets"): [840, 420, 310, 110],
        t("th_winrate"): ["66.4%", "61.2%", "63.8%", "68.0%"],
        t("th_roi"): ["+9.4%", "+6.2%", "+8.1%", "+11.0%"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════
# PAGE 4 : OFFRES
# ═══════════════════════════════════════════════════
elif page == t("nav_offers"):
    st.markdown(f"<h1 style='color:#047857; text-align:center;'>{t('offers_title')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748B; text-align:center;'>{t('offers_sub')}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_vip, col_elite = st.columns(2)

    with col_vip:
        st.markdown(f"""
        <div class="price-card">
            <div class="price-title">{t('vip_title')}</div>
            <p style="color:#64748B; font-size:0.9rem;">{t('vip_sub')}</p>
            <div class="price-amount">29.99€ <span style="font-size:1rem; color:#64748B;">/ mois</span></div>
            <hr style="border-color:#E2E8F0;">
            <p style="color:#1E293B; text-align:left;">✅ {t('vip_f1')}</p>
            <p style="color:#1E293B; text-align:left;">✅ {t('vip_f2')}</p>
            <p style="color:#1E293B; text-align:left;">✅ {t('vip_f3')}</p>
            <p style="color:#1E293B; text-align:left;">✅ {t('vip_f4')}</p>
            <p style="color:#94A3B8; text-align:left;">❌ {t('vip_x1')}</p>
            <p style="color:#94A3B8; text-align:left;">❌ {t('vip_x2')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(t("vip_btn"), LEMON_CHECKOUT_VIP, use_container_width=True, type="secondary")

    with col_elite:
        st.markdown(f"""
        <div class="price-card featured">
            <span class="badge-value">{t('elite_badge')}</span>
            <div class="price-title" style="margin-top:10px;">{t('elite_title')}</div>
            <p style="color:#64748B; font-size:0.9rem;">{t('elite_sub')}</p>
            <div class="price-amount">49.99€ <span style="font-size:1rem; color:#64748B;">/ mois</span></div>
            <hr style="border-color:#E2E8F0;">
            <p style="color:#1E293B; text-align:left;">✅ <b>{t('elite_f1')}</b></p>
            <p style="color:#1E293B; text-align:left;">✅ <b>{t('elite_f2')}</b></p>
            <p style="color:#1E293B; text-align:left;">✅ {t('elite_f3')}</p>
            <p style="color:#1E293B; text-align:left;">✅ {t('elite_f4')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(t("elite_btn"), LEMON_CHECKOUT_ELITE, use_container_width=True, type="primary")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:16px; padding:25px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.04);">
        <h3 style="color:#047857;">{t('guarantee_box_title')}</h3>
        <p style="color:#64748B;">{t('guarantee_box_text')}</p>
    </div>
    """, unsafe_allow_html=True)
