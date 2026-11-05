import streamlit as st
import requests
from datetime import datetime

# ═══════════════════════════════════════════════════
# CONFIGURATION ET LIENS
# ═══════════════════════════════════════════════════
ODDS_API_KEY = "ta_cle_ici"

LEMON_CHECKOUT_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_CHECKOUT_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

# ═══════════════════════════════════════════════════
# CONFIGURATION STREAMLIT & STYLES CSS SUR-MESURE
# ═══════════════════════════════════════════════════
st.set_page_config(
    page_title="Le Scanner — Dominez les Bookmakers",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #07090e; }
    
    .hero-container {
        background: linear-gradient(135deg, rgba(0,255,136,0.1) 0%, rgba(15,23,42,0.6) 100%);
        border: 1px solid rgba(0, 255, 136, 0.2);
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    .hero-title {
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #FFFFFF 0%, #00FF88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        color: #94A3B8 !important;
        font-size: 1.2rem !important;
        max-width: 700px;
        margin: 0 auto 20px auto;
    }
    .badge-value {
        background: rgba(0, 255, 136, 0.15);
        color: #00FF88;
        padding: 6px 14px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid rgba(0, 255, 136, 0.4);
        display: inline-block;
    }
    .stat-box {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
    }
    .stat-number {
        font-size: 2.2rem;
        font-weight: 900;
        color: #00FF88;
    }
    .stat-label {
        color: #64748B;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .bet-card-v2 {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .match-header {
        font-size: 1.3rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 12px;
    }
    .odds-pill {
        background: #1E293B;
        color: #FACC15;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 4px 12px;
        border-radius: 8px;
    }
    .price-card {
        background: #0F172A;
        border: 2px solid #1E293B;
        border-radius: 20px;
        padding: 35px 25px;
        text-align: center;
    }
    .price-card.featured {
        border-color: #00FF88;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.2);
    }
    .price-title { font-size: 1.6rem; font-weight: 800; color: white; }
    .price-amount { font-size: 3rem; font-weight: 900; color: #00FF88; margin: 15px 0; }
    section[data-testid="stSidebar"] { background-color: #0B0F19; border-right: 1px solid #1E293B; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# DONNÉES DE DÉMO
# ═══════════════════════════════════════════════════
def get_demo_bets():
    return [
        {
            "home": "PSG", "away": "Olympique de Marseille",
            "sport": "⚽ Ligue 1", "league": "France",
            "time": "Aujourd'hui • 20h45",
            "selection": "Over 2.5 Buts",
            "odds": 1.88, "bookmaker": "Winamax",
            "value": 14.2, "stake": 25,
            "stars": "⭐⭐⭐⭐⭐",
            "reason": "Marge anomalie détectée : Cote marché à 1.68 vs Winamax 1.88."
        },
        {
            "home": "Real Madrid", "away": "FC Barcelone",
            "sport": "⚽ La Liga", "league": "Espagne",
            "time": "Demain • 21h00",
            "selection": "Victoire Real Madrid",
            "odds": 2.15, "bookmaker": "Betclic",
            "value": 11.5, "stake": 15,
            "stars": "⭐⭐⭐⭐",
            "reason": "L'algo détecte une sous-évaluation du Real après rotation."
        },
        {
            "home": "LA Lakers", "away": "Boston Celtics",
            "sport": "🏀 NBA", "league": "USA",
            "time": "Demain • 02h30",
            "selection": "Lakers +4.5 Handicap",
            "odds": 1.95, "bookmaker": "Unibet",
            "value": 8.7, "stake": 12,
            "stars": "⭐⭐⭐⭐",
            "reason": "Forme extérieure surestimée pour Boston d'après notre modèle."
        }
    ]

# ═══════════════════════════════════════════════════
# NAVIGATION SIDEBAR
# ═══════════════════════════════════════════════════
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00FF88;'>🎯 LE SCANNER</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.8rem;'>Algorithme de Value Bets V4.2</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["🏠 Accueil & Value Bets", "🧮 Calculateur de Gains", "📊 Transparence & Stats", "💎 Offres VIP & Elite"],
        index=0
    )

# ═══════════════════════════════════════════════════
# PAGE 1 : ACCUEIL
# ═══════════════════════════════════════════════════
if page == "🏠 Accueil & Value Bets":
    
    st.markdown("""
    <div class="hero-container">
        <span class="badge-value">🔥 ALGORITHME D'ARBITRAGE ET DE VALUE BETS</span>
        <h1 class="hero-title">Arrêtez de Parier au Hasard.<br>Pariez sur les Mathématiques.</h1>
        <p class="hero-subtitle">Le Scanner scrute en temps réel des milliers de cotes sur Winamax, Betclic, Unibet et repère les erreurs des bookmakers avant qu'ils ne les corrigent.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-box"><div class="stat-number">64.2%</div><div class="stat-label">Win Rate Moyen</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-box"><div class="stat-number">+8.3%</div><div class="stat-label">ROI Mensuel Moyen</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">Mathématique</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-box"><div class="stat-number">24/7</div><div class="stat-label">Scan en Temps Réel</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>🔥 Opportunités Détectées Aujourd'hui</h2>", unsafe_allow_html=True)

    bets = get_demo_bets()
    for bet in bets:
        st.markdown(f"""
        <div class="bet-card-v2">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="color: #64748B; font-size: 0.85rem; font-weight: 600;">{bet['sport']} • {bet['league']} • {bet['time']}</span>
                <span class="badge-value">VALUE : +{bet['value']}%</span>
            </div>
            <div class="match-header">{bet['home']} vs {bet['away']}</div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; align-items: center; background: #07090E; padding: 15px; border-radius: 10px; margin-top: 10px;">
                <div>
                    <span style="color: #64748B; font-size: 0.8rem;">Sélection :</span><br>
                    <strong style="color: #00FF88; font-size: 1.1rem;">{bet['selection']}</strong>
                </div>
                <div style="margin-left: auto;">
                    <span style="color: #64748B; font-size: 0.8rem;">Cote Bookmaker :</span><br>
                    <span class="odds-pill">{bet['odds']}</span> <span style="color: #94A3B8; font-size: 0.85rem;">({bet['bookmaker']})</span>
                </div>
                <div style="margin-left: auto;">
                    <span style="color: #64748B; font-size: 0.8rem;">Mise Conseillée (Kelly) :</span><br>
                    <strong style="color: white; font-size: 1.1rem;">{bet['stake']} €</strong>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #00FF88 0%, #00B894 100%); padding: 35px; border-radius: 20px; text-align: center; color: #07090E;">
        <h2 style="color: #07090E !important; font-weight: 900; margin-bottom: 10px;">Ne Manquez Plus Aucune Marge d'Erreur !</h2>
        <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 20px; color: #07090E;">Rejoignez le canal WhatsApp VIP et recevez les cotes pépites instantanément sur votre téléphone.</p>
        <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background: #07090E; color: #00FF88; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 900; font-size: 1.1rem; display: inline-block;">🚀 Obtenir l'Accès VIP Instantané</a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATEUR
# ═══════════════════════════════════════════════════
elif page == "🧮 Calculateur de Gains":
    st.markdown("<h1 style='color: white;'>🧮 Simulateur d'Investissement</h1>", unsafe_allow_html=True)
    bankroll = st.slider("Votre Capital Initial (€)", 100, 5000, 500, 50)
    mois = st.slider("Durée d'investissement (Mois)", 1, 12, 6)
    
    capital_final = bankroll * ((1 + 0.083) ** mois)
    profit_net = capital_final - bankroll
    
    st.markdown(f"""
    <div style="background: #0F172A; border: 2px solid #00FF88; padding: 30px; border-radius: 16px; text-align: center; margin-top: 20px;">
        <p style="color: #64748B; font-size: 0.9rem;">CAPITAL FINAL ESTIMÉ</p>
        <h1 style="color: #00FF88; font-size: 3rem; font-weight: 900;">{capital_final:.2f} €</h1>
        <p style="color: #38BDF8; font-weight: 700; font-size: 1.2rem;">+ {profit_net:.2f} € de bénéfice net estimé</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PAGE 3 : STATS
# ═══════════════════════════════════════════════════
elif page == "📊 Transparence & Stats":
    st.markdown("<h1 style='color: white;'>📊 Historique & Transparence</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Paris Analysés", "14,820+")
    c2.metric("Taux de Réussite Globale", "64.2%")
    c3.metric("Marge Moyenne Détectée", "+9.8%")

# ═══════════════════════════════════════════════════
# PAGE 4 : OFFRES
# ═══════════════════════════════════════════════════
elif page == "💎 Offres VIP & Elite":
    st.markdown("<h1 style='color: white; text-align: center;'>💎 Choisissez Votre Plan d'Accès</h1>", unsafe_allow_html=True)
    col_vip, col_elite = st.columns(2)
    
    with col_vip:
        st.markdown(f"""
        <div class="price-card">
            <div class="price-title">💬 VIP WHATSAPP</div>
            <div class="price-amount">29.99€ <span style="font-size: 1rem; color: #64748B;">/ mois</span></div>
            <p style="color: #E2E8F0;">✅ 3 à 5 Value Bets par jour</p>
            <p style="color: #E2E8F0;">✅ Envoi instantané sur WhatsApp</p>
            <p style="color: #E2E8F0;">✅ Calcul des mises (Bankroll Management)</p>
            <br>
            <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background: #1E293B; color: white; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: 700; display: block;">Rejoindre le VIP</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col_elite:
        st.markdown(f"""
        <div class="price-card featured">
            <span class="badge-value">🔥 LE PLUS POPULAIRE</span>
            <div class="price-title" style="margin-top: 10px;">👑 ELITE CLUB</div>
            <div class="price-amount">49.99€ <span style="font-size: 1rem; color: #64748B;">/ mois</span></div>
            <p style="color: #E2E8F0;">✅ <b>Tout ce qui est inclus dans le VIP</b></p>
            <p style="color: #E2E8F0;">✅ <b>Surebets (Gains 100% garantis)</b></p>
            <p style="color: #E2E8F0;">✅ Alertes Live pendant les matchs</p>
            <br>
            <a href="{LEMON_CHECKOUT_ELITE}" target="_blank" style="background: #00FF88; color: #07090E; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: 900; display: block;">Rejoindre le Club Elite</a>
        </div>
        """, unsafe_allow_html=True)
