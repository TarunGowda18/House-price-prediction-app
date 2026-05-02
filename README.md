🏠 House Price Prediction App
A machine learning-powered web application that predicts house prices based on key property features such as square footage, number of rooms, lot size, garage size, and neighborhood quality. Built with a Linear Regression model and deployed using Streamlit.

🚀 Features

🔮 Predict house prices instantly with real-time output
🖥️ Clean, single-page user interface — no sidebar clutter
📋 Input summary table before prediction for review
📊 ±10% estimated price range for better insight
🏷️ Automatic property classification — Premium / Mid-range / Budget
📥 Download prediction results as a CSV file


🛠️ Technologies Used
CategoryToolsLanguagePython 3ML & DataScikit-learn, Pandas, NumPyWeb AppStreamlitSerializationPickle

📂 Project Structure
House-Price-Prediction-App/
│
├── app_house_pred.py        # Main Streamlit application
├── model.pkl                # Trained Linear Regression model
├── scaler.pkl               # Fitted StandardScaler
├── requirements.txt         # Python dependencies
└── house_price_regression_dataset.csv   # Training dataset

📊 Model Details
PropertyDetailAlgorithmLinear RegressionPreprocessingStandardScaler (zero mean, unit variance)Input Features7Evaluation MetricsMAE, MSE, RMSE, R² Score
🔑 Input Features
FeatureDescriptionSquare FootageTotal area of the house (sqft)Num BedroomsNumber of bedrooms (1–5)Num BathroomsNumber of bathrooms (1–3)Year BuiltYear the property was constructedLot SizeSize of the lot (acres)Garage SizeNumber of garage spaces (0–2)Neighborhood QualityQuality score of the neighborhood (1–10)

⚙️ Installation & Setup

Clone the repository

bash   git clone https://github.com/your-username/House-Price-Prediction-App.git
   cd House-Price-Prediction-App

Install dependencies

bash   pip install -r requirements.txt

Run the app

bash   streamlit run app_house_pred.py

🌐 Live Demo
👉 https://house-price-prediction-1212.streamlit.app/

🎯 Use Case
This application helps buyers, sellers, and real estate agents quickly estimate property prices based on key housing features — without needing any technical knowledge.

📸 App Preview

(Add a screenshot of the running app here)


🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or raise an issue.

⭐ Support
If you found this project useful, please consider giving it a star on GitHub — it helps a lot! 🙌
