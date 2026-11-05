import streamlit as st
import requests
from datetime import datetime

# CONFIGURATION
ODDS_API_KEY = "ta_cle_ici"
LEMON_CHECKOUT_VIP = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/ce97ef76-b781-4d29-86c3-8ec98b5d74cf"
LEMON_CHECKOUT_ELITE = "https://trendpulse-ai.lemonsqueezy.com/checkout/buy/1d156794-639b-4cc9-a3ac-d3087f05c7e3"

# DONNÉES DE DÉMO
def get_demo_bets():
    return [
        {
            "home": "PSG", "away": "Lyon",
            "sport": "⚽ Ligue 1",
            "time": "21:00",
            "selection": "Over 2.5 buts",
            "odds": 1.85, "bookmaker": "Winamax",
            "value": 12.8, "stake": 15,
            "stars": "⭐⭐⭐⭐",
        },
        {
            "home": "Real Madrid", "away": "Barça",
            "sport": "⚽ La Liga",
            "time": "21:00",
            "selection": "Victoire Real Madrid",
            "odds": 2.10, "bookmaker": "Betclic",
            "value": 9.4, "stake": 10,
            "stars": "⭐⭐⭐⭐",
        },
        {
            "home": "Lakers", "away": "Celtics",
            "sport": "🏀 NBA",
            "time": "02:00",
            "selection": "Lakers -3.5",
            "odds": 1.92, "bookmaker": "Unibet",
            "value": 7.6, "stake": 8,
            "stars": "⭐⭐⭐",
        }
    ]

# INTERFACE WEB
st.set_page_config(page_title="Le Scanner — Value Bets", page_icon="🎯", layout="wide")

st.markdown("# 🎯 LE SCANNER")
st.markdown("### Plateforme de Value Bets & Gestion de Risques")
st.markdown("---")

page = st.sidebar.radio("📱 Menu", ["🏠 Value Bets du jour", "📊 Statistiques", "💎 S'abonner"])

if page == "🏠 Value Bets du jour":
    st.markdown(f"## 📅 Pronostics du {datetime.now().strftime('%d/%m/%Y')}")
    bets = get_demo_bets()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Value Bets", len(bets))
    col2.metric("💎 Value Moyenne", "+9.9%")
    col3.metric("📈 ROI Estimé", "+8.3%")
    
    st.markdown("---")
    for bet in bets:
        with st.container():
            st.subheader(f"{bet['sport']} | {bet['home']} vs {bet['away']}")
            st.write(f"📌 **Pari :** {bet['selection']}")
            st.write(f"📊 **Cote :** {bet['odds']} ({bet['bookmaker']})")
            st.write(f"💎 **Value :** +{bet['value']}% | 💰 **Mise conseillée :** {bet['stake']}€")
            st.write(f"Évaluation : {bet['stars']}")
            st.markdown("---")

elif page == "📊 Statistiques":
    st.markdown("## 📊 Bilan des performances")
    col1, col2, col3 = st.columns(3)
    col1.metric("Win Rate", "64.2%")
    col2.metric("ROI Mensuel", "+7.8%")
    col3.metric("Profit Total", "+2,340€")

elif page == "💎 S'abonner":
    st.markdown("## 💎 Choisissez votre formule")
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 💬 VIP - 29.99€/mois")
        st.write("• Value Bets quotidiens sur WhatsApp")
        st.write("• Mises calculées")
        st.link_button("S'abonner VIP", LEMON_CHECKOUT_VIP)
    with col2:
        st.success("### 👑 ELITE - 49.99€/mois")
        st.write("• Tout le VIP + Surebets & Live")
        st.write("• Bilan & conseils personnalisés")
        st.link_button("S'abonner Elite", LEMON_CHECKOUT_ELITE)
