 README: IronJack – AI Blackjack Strategy Simulator

 An AI-powered Blackjack decision-making system using Machine Learning and Zen Count strategy.

 📖 Project Overview

IronJack is a Blackjack AI simulation that leverages Machine Learning (Random Forest Classifier) to provide optimal Hit or Stand recommendations based on:
✅ Player’s hand
✅ Dealer’s visible card
✅ Presence of an Ace
✅ Zen Count (Card counting strategy)
✅ Probability of winning, losing, or drawing

The AI model analyzes historical data and applies Blackjack rules to improve decision-making.

🚀 Features

✅ AI-Powered Decision Making – The model recommends the best move (Hit or Stand) based on training data and blackjack strategy.
✅ Realistic Probability Estimations – Uses Zen Count and dealer’s hand strength to adjust winning chances dynamically.
✅ Interactive Web App – Built with Streamlit for easy user interaction.
✅ Machine Learning-Based Predictions – Trained with RandomForestClassifier for optimal predictions.
✅ Custom Simulation – Allows users to input their own hand and simulate game outcomes.


🛠️ Installation Guide

1️⃣ Clone the Repository
git clone https://github.com/your-repo/IronJack.git
cd IronJack

2️⃣ Install Dependencies

Ensure you have Python installed, then run:
pip install -r requirements.txt

Dependencies include:
	•	pandas
	•	numpy
	•	scikit-learn
	•	streamlit


▶️ How to Use

Run the AI Blackjack Web App
streamlit run blackjack_ai.py

This will open an interactive web page where you can input your hand and get AI recommendations.

Simulate Multiple Games

You can also run batch simulations to test AI decisions across multiple rounds:
python simulate_blackjack.py

🎰 How It Works

1️⃣ Data Collection

A dataset of 50,000+ Blackjack hands was generated, including:
	•	Player’s hand value (4 to 21)
	•	Dealer’s visible card (1 to 10)
	•	Has an Ace? (Yes/No)
	•	Zen Count (-10 to +10)
	•	Probability of Win/Loss/Draw
	•	Decision Taken (Hit/Stand)

2️⃣ Model Training

A Random Forest Classifier was trained using this dataset to predict Hit or Stand decisions based on game conditions.

3️⃣ AI Recommendations

The trained model analyzes a hand and predicts the best decision, considering basic Blackjack rules and Zen Count adjustments.

📊 Example Output

🎰 **Blackjack AI Decision Simulation** 🎰
🃏 Player's Hand: 16
🎭 Dealer's Card: 9
🎴 Has an Ace: No
📊 Zen Count: 5

📢 **Recommended Action:** Hit

📊 **Expected Outcomes:**
🏆 Win Probability: 42.5%
💀 Loss Probability: 50.0%
⚖️ Draw Probability: 7.5%


👨‍💻 Author
	•	Borja Cervera – Developer & AI Engineer
