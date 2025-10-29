🌾 Agricultural Finance ML System

An interactive Machine Learning web application built with Streamlit to analyze and predict agricultural finance outcomes.
This project demonstrates how data science and machine learning can be used to support financial decision-making in the agriculture sector.

🚀 Features

📊 Interactive Dashboard – Visualize data and results using Plotly charts.

🤖 Machine Learning Model Integration – Load and use trained models to make predictions.

🧮 Real-time Predictions – Input financial data and get instant predictions.

💾 Data Upload Support – Upload your own datasets for analysis.

🎨 User-Friendly Interface – Simple and clean UI powered by Streamlit.

🛠️ Tech Stack

Python 3.10+

Streamlit – for building the web interface

Plotly – for interactive data visualization

Pandas – for data manipulation

Scikit-learn / Joblib / Pickle – for loading ML models

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/alx-hackathon.git
cd alx-hackathon


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run streamlit_app.py

🧠 Model Information

The model (model.pkl) is a trained machine learning model designed to predict agricultural finance outcomes based on relevant input data.
Ensure that:

The model.pkl file is present in the root directory.

The model was saved using the same library version you’re loading it with.

If you encounter _pickle.UnpicklingError, recheck your model file or regenerate it using the same Python environment.

📈 Example Usage

Upload your dataset or manually enter input values.

Click Predict to see the model’s output.

View results on an interactive dashboard.

🧩 Troubleshooting

_pickle.UnpicklingError → Ensure model.pkl is not corrupted and was created using pickle or joblib.

SyntaxError: unterminated string literal → Make sure all quotes are properly closed in streamlit_app.py.

ModuleNotFoundError: No module named 'plotly' → Install Plotly using pip install plotly.

👨‍💻 Author

George Ndung'u
💡 Developed during the ALX Hackathon.
🧠 Passionate about AI, Finance, and Data Science.

📜 License

This project is licensed under the MIT License – feel free to use and modify it for educational or research purposes.
