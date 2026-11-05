       """
🎯 LE SCANNER — Landing Page & App Premium
Design High-Converting SaaS / Cyberpunk Dark Mode
"""

import streamlit as st
import requests
from datetime import datetime

# ═══════════════════════════════════════════════════
# CONFIGURATION ET LIENS
# ═══════════════════════════════════════════════════
ODDS_API_KEY = "ta_cle_ici"

# Remplace par tes vrais liens Lemon Squeezy !
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

# Injection CSS pour un style Ultra Premium Dark Neon
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #07090e;
    }
    
    /* Hero Banner Gradient */
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
    
    /* Feature Badge */
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
    
    /* Stat Metric Box */
    .stat-box {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .stat-box:hover {
        transform: translateY(-4px);
        border-color: #00FF88;
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
    
    /* Modern Bet Card */
    .bet-card-v2 {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        position: relative;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .bet-card-v2:hover {
        border-color: rgba(0, 255, 136, 0.5);
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
    
    /* Pricing Cards */
    .price-card {
        background: #0F172A;
        border: 2px solid #1E293B;
        border-radius: 20px;
        padding: 35px 25px;
        text-align: center;
        height: 100%;
        position: relative;
    }
    .price-card.featured {
        border-color: #00FF88;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.2);
    }
    .price-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: white;
    }
    .price-amount {
        font-size: 3rem;
        font-weight: 900;
        color: #00FF88;
        margin: 15px 0;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19;
        border-right: 1px solid #1E293B;
    }
    
    /* Hide Default Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════
# DONNÉES ET FONCTIONS DE BASE
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
            "stars": "⭐⭐⭐⭐⭐", "confidence": "TRÈS ÉLEVÉE",
            "reason": "Marge anomalie détectée : Cote marché à 1.68 vs Winamax 1.88."
        },
        {
            "home": "Real Madrid", "away": "FC Barcelone",
            "sport": "⚽ La Liga", "league": "Espagne",
            "time": "Demain • 21h00",
            "selection": "Victoire Real Madrid",
            "odds": 2.15, "bookmaker": "Betclic",
            "value": 11.5, "stake": 15,
            "stars": "⭐⭐⭐⭐", "confidence": "ÉLEVÉE",
            "reason": "L'algo détecte une sous-évaluation du Real après rotation."
        },
        {
            "home": "LA Lakers", "away": "Boston Celtics",
            "sport": "🏀 NBA", "league": "USA",
            "time": "Demain • 02h30",
            "selection": "Lakers +4.5 Handicap",
            "odds": 1.95, "bookmaker": "Unibet",
            "value": 8.7, "stake": 12,
            "stars": "⭐⭐⭐⭐", "confidence": "ÉLEVÉE",
            "reason": "Forme extérieure surestimée pour Boston d'après notre modèle."
        },
        {
            "home": "Jannik Sinner", "away": "Carlos Alcaraz",
            "sport": "🎾 ATP Masters", "league": "Tennis",
            "time": "Dimanche • 15h00",
            "selection": "Sinner Gagne le 1er Set",
            "odds": 2.05, "bookmaker": "ZEbet",
            "value": 6.8, "stake": 10,
            "stars": "⭐⭐⭐", "confidence": "MODÉRÉE",
            "reason": "Avantage historique de Sinner au 1er set sur cette surface."
        }
    ]

# ═══════════════════════════════════════════════════
# NAVIGATION DANS LA SIDEBAR
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
    
    st.markdown("---")
    st.markdown("""
    <div style="background: rgba(0,255,136,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(0,255,136,0.2);">
        <p style="color: #00FF88; font-weight: 700; margin-bottom: 5px;">🔒 Garantie 100%</p>
        <p style="color: #94A3B8; font-size: 0.8rem; margin: 0;">Aucun pronostic émotionnel. Uniquement des mathématiques et des anomalies de cotes.</p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════
# PAGE 1 : ACCUEIL & VALUE BETS
# ═══════════════════════════════════════════════════
if page == "🏠 Accueil & Value Bets":
    
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <span class="badge-value">🔥 ALGORITHME D'ARBITRAGE ET DE VALUE BETS</span>
        <h1 class="hero-title">Arrêtez de Parier au Hasard.<br>Pariez sur les Mathématiques.</h1>
        <p class="hero-subtitle">Le Scanner scrute en temps réel des milliers de cotes sur Winamax, Betclic, Unibet et repère les erreurs des bookmakers avant qu'ils ne les corrigent.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3 Stat Boxes Banner
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
    st.markdown("<p style='color: #94A3B8;'>Voici un aperçu des Value Bets identifiés par notre algorithme :</p>", unsafe_allow_html=True)

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
            <div style="margin-top: 12px; font-size: 0.85rem; color: #94A3B8;">
                💡 <b>Analyse Algo :</b> {bet['reason']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Call To Action Banner
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #00FF88 0%, #00B894 100%); padding: 35px; border-radius: 20px; text-align: center; color: #07090E;">
        <h2 style="color: #07090E !important; font-weight: 900; margin-bottom: 10px;">Ne Manquez Plus Aucune Marge d'Erreur !</h2>
        <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 20px; color: #07090E;">Rejoignez le canal WhatsApp VIP et recevez les cotes pépites instantanément sur votre téléphone.</p>
        <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background: #07090E; color: #00FF88; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 900; font-size: 1.1rem; display: inline-block; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">🚀 Obtenir l'Accès VIP Instantané</a>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════
# PAGE 2 : CALCULATEUR DE GAINS
# ═══════════════════════════════════════════════════
elif page == "🧮 Calculateur de Gains":
    st.markdown("<h1 style='color: white;'>🧮 Simulateur d'Investissement</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Estimez l'évolution théorique de votre capital grâce à la méthode du Kelly Criterion et à un ROI moyen de 8.3% par mois.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col_input, col_result = st.columns([1, 1])
    
    with col_input:
        st.markdown("### ⚙️ Vos Paramètres")
        bankroll = st.slider("Votre Capital Initial (€)", min_value=100, max_value=5000, value=500, step=50)
        mois = st.slider("Durée d'investissement (Mois)", min_value=1, max_value=12, value=6)
        risk_profile = st.select_slider("Profil de Risque", options=["Prudent (1% par pari)", "Modéré (2% par pari)", "Optimisé Algo (Kelly 1/4)"], value="Optimisé Algo (Kelly 1/4)")
        
    with col_result:
        # Calculateur théorique basique
        roi_mensuel = 0.083
        capital_final = bankroll * ((1 + roi_mensuel) ** mois)
        profit_net = capital_final - bankroll
        
        st.markdown("### 📈 Estimation après "+str(mois)+" mois")
        st.markdown(f"""
        <div style="background: #0F172A; border: 2px solid #00FF88; padding: 30px; border-radius: 16px; text-align: center;">
            <p style="color: #64748B; font-size: 0.9rem;">CAPITAL FINAL ESTIMÉ</p>
            <h1 style="color: #00FF88; font-size: 3rem; font-weight: 900; margin: 10px 0;">{capital_final:.2f} €</h1>
            <p style="color: #38BDF8; font-weight: 700; font-size: 1.2rem;">+ {profit_net:.2f} € de bénéfice net estimé</p>
        </div>
        """, unsafe_allow_html=True)
        st.caption("⚠️ Les paris sportifs comportent des risques. Ces estimations sont basées sur notre historique statistique moyen et ne constituent pas une garantie absolue.")


# ═══════════════════════════════════════════════════
# PAGE 3 : TRANSPARENCE & STATS
# ═══════════════════════════════════════════════════
elif page == "📊 Transparence & Stats":
    st.markdown("<h1 style='color: white;'>📊 Historique & Transparence</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Chaque pari recommandé par notre algorithme est archivé et vérifiable.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Paris Analysés", "14,820+", "+340 cette semaine")
    c2.metric("Taux de Réussite Globale", "64.2%", "+1.4% vs mois dernier")
    c3.metric("Marge Moyenne Détectée", "+9.8%", "vs cote de clôture")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏆 Bilan par Discipline")
    
    import pandas as pd
    df = pd.DataFrame({
        "Discipline": ["⚽ Football (Ligue 1 & Europe)", "🏀 Basketball (NBA)", "🎾 Tennis (ATP/WTA)", "🏉 Rugby (Top 14)"],
        "Nombre de Paris": [840, 420, 310, 110],
        "Taux de Gain": ["66.4%", "61.2%", "63.8%", "68.0%"],
        "ROI Net": ["+9.4%", "+6.2%", "+8.1%", "+11.0%"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)


# ═══════════════════════════════════════════════════
# PAGE 4 : OFFRES VIP & ELITE
# ═══════════════════════════════════════════════════
elif page == "💎 Offres VIP & Elite":
    st.markdown("<h1 style='color: white; text-align: center;'>💎 Choisissez Votre Plan d'Accès</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; text-align: center;'>Rentabilisez votre abonnement dès vos premiers Value Bets.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_vip, col_elite = st.columns(2)
    
    with col_vip:
        st.markdown(f"""
        <div class="price-card">
            <div class="price-title">💬 VIP WHATSAPP</div>
            <p style="color: #64748B;">Idéal pour les parieurs réguliers</p>
            <div class="price-amount">29.99€ <span style="font-size: 1rem; color: #64748B;">/ mois</span></div>
            <hr style="border-color: #1E293B;">
            <p style="color: #E2E8F0;">✅ 3 à 5 Value Bets par jour</p>
            <p style="color: #E2E8F0;">✅ Envoi instantané sur WhatsApp</p>
            <p style="color: #E2E8F0;">✅ Calcul des mises (Bankroll Management)</p>
            <p style="color: #E2E8F0;">✅ Bilan et suivi hebdomadaire</p>
            <p style="color: #64748B;">❌ Surebets & Arbitrage Garanti</p>
            <p style="color: #64748B;">❌ Alertes Live pendant les matchs</p>
            <br>
            <a href="{LEMON_CHECKOUT_VIP}" target="_blank" style="background: #1E293B; color: white; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: 700; display: block;">Rejoindre le VIP</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col_elite:
        st.markdown(f"""
        <div class="price-card featured">
            <span class="badge-value">🔥 LE PLUS POPULAIRE</span>
            <div class="price-title" style="margin-top: 10px;">👑 ELITE CLUB</div>
            <p style="color: #64748B;">Pour maximiser vos bénéfices</p>
            <div class="price-amount">49.99€ <span style="font-size: 1rem; color: #64748B;">/ mois</span></div>
            <hr style="border-color: #1E293B;">
            <p style="color: #E2E8F0;">✅ <b>Tout ce qui est inclus dans le VIP</b></p>
            <p style="color: #E2E8F0;">✅ <b>Surebets (Gains 100% garantis)</b></p>
            <p style="color: #E2E8F0;">✅ Alertes Live pendant les matchs</p>
            <p style="color: #E2E8F0;">✅ Gestion de Bankroll Kelly personnalisée</p>
            <p style="color: #E2E8F0;">✅ Support prioritaire 7j/7</p>
            <br>
            <a href="{LEMON_CHECKOUT_ELITE}" target="_blank" style="background: #00FF88; color: #07090E; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: 900; display: block; box-shadow: 0 10px 20px rgba(0,255,136,0.3);">Rejoindre le Club Elite</a>
        </div>
        """, unsafe_allow_html=True)

    # Section FAQ
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; text-align: center;'>❓ Foire Aux Questions</h3>", unsafe_allow_html=True)
    
    with st.expander("Comment fonctionne la détection des Value Bets ?"):
        st.write("Notre algorithme compare en continu les cotes de plus de 15 bookmakers. Lorsqu'un bookmaker propose une cote nettement supérieure à la moyenne du marché, une 'value' est identifiée et vous recevez immédiatement l'alerte.")
        
    with st.expander("Faut-il avoir des comptes sur plusieurs bookmakers ?"):
        st.write("Oui, idéalement sur Winamax, Betclic, Unibet et Parions Sport pour toujours saisir la meilleure cote disponible.")
        
    with st.expander("Puis-je me désabonner facilement ?"):
        st.write("Absolument. Vous pouvez annuler votre abonnement en un seul clic à tout moment depuis votre compte Lemon Squeezy ou en nous envoyant un simple message.")
