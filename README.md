# 🚗 Car Price Prediction

## 🎯 Objective

- The objective of this project is to predict the selling price of used cars based on key features such as car age, present price, kilometers driven, fuel type, transmission type, and ownership history.

## 📊 Dataset Features
- Car_Name → Brand/model of the car
- Year → Year of purchase (converted to Car Age)
- Selling_Price → Target variable (price of used car in lakhs)
- Present_Price → Current showroom price of the new car
- Driven_kms → Total distance driven
- Fuel_Type → Petrol / Diesel / CNG
- Selling_type → Dealer / Individual
- Transmission → Manual / Automatic
- Owner → Total number of previous owners

## 🔍 Key Insights

- Higher Present Price → Higher Selling Price
- Automatic cars generally have a higher resale value than manual cars
- Petrol cars dominate, while diesel resale value has declined due to rising fuel costs
- Cars sold through Dealers have higher selling prices than Individual sellers
- Lower car age → Higher resale value

## 🤖 Model Training

- I retrained the dataset using Random Forest Regression, and compared it with multiple algorithms:
- Models Compared: Linear Regression, Decision Tree, Random Forest, XGBoost, LightGBM, SVR, KNN

- 🏆 Best Model: Random Forest Regressor
  - Highest R² Score: 0.9554 → Predicts 95.5% of the variance
  - Error Metrics:
      - MAE: 0.6156
      - MSE: 1.1150
      - RMSE: 1.0559
      - R²: 0.9558
  - Random Forest delivered the lowest prediction error across all models.

## ✅ Conclusion

- Built a machine learning model to predict used car prices using important features like car age, present price, kilometers driven, transmission, fuel type, and ownership history.
- Performed data cleaning, feature engineering, and EDA to extract valuable insights.
- Found that Present Price, Car Age, Transmission Type, and Fuel Type strongly influence resale value.
- Random Forest Regressor achieved the best performance (R² ≈ 0.96), making it a reliable model for real-world price prediction.
- This project provides a data-driven solution to help buyers and sellers make smarter decisions in the used car market.

  
