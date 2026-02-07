
# 🌾 Crop Yield Prediction System

A Machine Learning based web application that predicts **crop yield** using agricultural, environmental, and seasonal factors. This project combines **data science + web development** to help estimate farm productivity.

---

## 🚀 Features

✔ Predict crop yield using ML model  
✔ Dropdown selection for **Crop, Season, and State**  
✔ Clean and user-friendly web interface  
✔ Real-time prediction from trained model  
✔ Data preprocessing & model pipeline included  

---

## 🗂 Project Structure

```
CROP_YIELD/
│
├── data/
│   └── crop_yield.csv          # Dataset used for training
│
├── models/
│   └── model.pkl               # Trained ML model (generated after training)
│
├── src/
│   ├── preprocess.py           # Data cleaning & preprocessing
│   ├── train_model.py          # Model training script
│   └── predict_pipeline.py     # Handles prediction pipeline
│
├── static/
│   └── style.css               # Frontend styling
│
├── templates/
│   └── index.html              # Web UI page
│
├── app.py                      # Flask backend server
├── requirements.txt            # Required Python libraries
└── README.md                   # Project documentation
```

---

## ⚙️ Technologies Used

- Python 🐍  
- Flask 🌐  
- Scikit-learn 🤖  
- Pandas & NumPy 📊  
- HTML5 + CSS3 🎨  

---

## 📊 Input Features for Prediction

The model uses the following inputs:

- Crop  
- Season  
- State  
- Crop Year  
- Area (hectares)  
- Production (tonnes)  
- Annual Rainfall (mm)  
- Fertilizer Used (kg/hectare)  
- Pesticide Used (kg/hectare)  

---

## 🧠 How the System Works

1. Data is cleaned and preprocessed  
2. Model is trained using `train_model.py`  
3. Model is saved inside the **models/** folder  
4. Flask app loads the model  
5. User enters data on web page  
6. Prediction is displayed instantly  

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

### Step 2: Train the Model

```
python src/train_model.py
```

### Step 3: Run the Flask App

```
python app.py
```

### Step 4: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📌 Output

The system predicts:

> 🌱 **Estimated Crop Yield** based on provided agricultural inputs.

---

## 👩‍💻 Author

Developed as an AI/ML academic project for Crop Yield Prediction.

---

💡 Future Improvements:
- Add weather API integration  
- Deploy on cloud (AWS/Render/Heroku)  
- Add visualization dashboard

## 🔮 Sample Prediction Output

![Prediction Result](static/output.png)


