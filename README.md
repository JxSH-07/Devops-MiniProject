# Updated ReadMe
# 🚗 Car Price Prediction Web App

**🔗 Live Demo:** [Try it Here](https://car-pred.onrender.com)

---

## 📌 Overview

This project is a **car resale price prediction** web application built using **Linear Regression** and deployed with **Flask**. Users can input vehicle details such as **brand**, **model**, **manufacturing year**, **fuel type**, and **kilometers driven** to estimate the resale value of a car in real time.

The frontend is crafted using **HTML, CSS, and Bootstrap**, offering a smooth and responsive user experience on both desktop and mobile.

---

## ✨ Key Features

- ✅ Real-time price prediction using a trained ML model  
- 🚘 Dropdown inputs for valid selection of car attributes  
- 🧼 Cleaned & preprocessed dataset for better accuracy  
- 📉 Trained using **Linear Regression** on structured car resale data  
- 📱 Mobile-friendly and responsive UI using **Bootstrap**  
- 🔁 Instant results displayed on the same page

---

## 🧠 How It Works

1. User selects input values (company, model, year, fuel type) and enters kilometers driven.
2. Inputs are passed to a **Flask backend** that loads the trained model.
3. Model returns the predicted car price.
4. Result is displayed clearly on the frontend.

---

## 🛠️ Tech Stack

### 🔙 Backend & Model
- **Python** – Data processing & model logic
- **Pandas**, **Scikit-learn** – Preprocessing & training
- **Linear Regression** – ML algorithm used
- **Pickle** – Model serialization for deployment
- **Flask** – Lightweight Python web framework

### 🌐 Frontend
- **HTML**, **CSS**, **Bootstrap** – User interface & responsiveness

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```git clone https://github.com/DEEP-222-N/Car_Pred.git```

```cd mobile-recommender```

### 2. Install Requirements

```pip install -r requirements.txt```


### 3. Run the Flask App

```python app.py```
