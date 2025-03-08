import streamlit as st
import numpy as np
import joblib

# Load trained Random Forest model
model = joblib.load("blackjack_randomforest_model.pkl")

def estimate_probabilities(player_total, dealer_card, has_ace, zen_count):
    """
    Improved probability calculation using Blackjack strategy rules and Zen count.
    """
    # Base probabilities adjusted to match real-world Blackjack strategy
    if player_total > 21:  
        return 0.00, 1.00, 0.00  # Bust = 100% Loss
    
    if player_total == 21:  
        return 0.95, 0.05, 0.00  # 95% Win if natural 21
    
    # Dealer has a strong card (7+), higher loss chance
    if dealer_card >= 7:
        base_win = max(0.15, min(0.6, (22 - player_total) / 25))
        base_loss = max(0.3, min(0.8, dealer_card / 12))
    
    # Dealer has a weak card (2-6), higher win chance
    else:
        base_win = max(0.3, min(0.7, (22 - player_total) / 20))
        base_loss = max(0.2, min(0.6, dealer_card / 10))
    
    # Adjust based on Zen Count - higher Zen favors player wins
    if zen_count > 3:
        base_win += 0.05
        base_loss -= 0.05
    elif zen_count < -3:
        base_win -= 0.05
        base_loss += 0.05
    
    # Ensure sum is 1
    base_draw = 1 - (base_win + base_loss)
    base_draw = max(0.01, min(0.2, base_draw))

    return base_win, base_loss, base_draw

# Streamlit UI
st.title("♠️ Blackjack AI Advisor 🃏")
st.subheader("Enter your hand details to get AI recommendations")

# User Inputs (Sliders)
player_total = st.slider("Your Hand Total", min_value=4, max_value=21, value=10)
dealer_card = st.slider("Dealer's Visible Card", min_value=1, max_value=10, value=6)
has_ace = st.radio("Do you have an Ace?", ("No", "Yes")) == "Yes"
zen_count = st.slider("Zen Count", min_value=-10, max_value=10, value=0)

# Add a button to trigger prediction (optional)
if st.button("🔮 Get AI Recommendation"):
    # Calculate probabilities dynamically
    prob_win, prob_loss, prob_draw = estimate_probabilities(player_total, dealer_card, has_ace, zen_count)

    # Prepare input data with 7 features
    input_data = np.array([[player_total, dealer_card, int(has_ace), zen_count, prob_win, prob_loss, prob_draw]])

    # Predict action: 0 = Stand, 1 = Hit
    decision = model.predict(input_data)[0]
    decision_text = "**Hit**" if decision == 1 else "**Stand**"

    # Display results
    st.markdown("## 🎰 AI Decision Simulation")
    st.markdown(f"🃏 **Player's Hand:** {player_total}")
    st.markdown(f"🎭 **Dealer's Card:** {dealer_card}")
    st.markdown(f"🎴 **Has an Ace:** {'Yes' if has_ace else 'No'}")
    st.markdown(f"📊 **Zen Count:** {zen_count}")

    st.markdown("### 🤖 AI Recommendation")
    st.markdown(f"🔮 **{decision_text}**")

    st.markdown("### 📊 Expected Outcomes")
    st.markdown(f"🏆 **Win Probability:** {prob_win * 100:.2f}%")
    st.markdown(f"💀 **Loss Probability:** {prob_loss * 100:.2f}%")
    st.markdown(f"⚖️ **Draw Probability:** {prob_draw * 100:.2f}%")

    # Footer
    st.caption("Powered by AI & Machine Learning 🤖♠️")