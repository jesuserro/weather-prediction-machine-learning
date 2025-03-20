# Weather Prediction Project 🌦️

## 📊 Overview

In this project, we aim to predict weather conditions using machine learning models. We focus on two main tasks:
1. **Classification**: Predicting the "type of day" (e.g., sunny, rainy, cloudy).
2. **Regression**: Predicting "how much it will rain" (precipitation percentage).

## 📁 Data Source

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/nikhil7280/weather-type-classification) and can be found in the file `weather_classification_data.csv`. 

## 🛠️ Models Used

### Classification Model
- **Random Forest Classifier**: The primary model used for predicting the type of day. Detailed implementation can be found in `4_random_forest_adjusted.ipynb`.

### Regression Model
- **Random Forest Regressor**: The primary model used for predicting the amount of rainfall. Detailed implementation can be found in `8_random_forest_regressor.ipynb`.

### Other Models Explored
- **K-Nearest Neighbors (KNN)**: Explored in `2_knn_classifier.ipynb`.
- **Gradient Boosting**: Explored in `5_gradient_boosting.ipynb`.

After experimenting with various models, we found that the Random Forest models provided the best performance for both classification and regression tasks.

## 📈 Results

- **Classification Accuracy**: Achieved high accuracy in predicting the type of day using the Random Forest Classifier.
- **Regression Performance**: Successfully predicted the amount of rainfall with the Random Forest Regressor.

## 📚 Conclusion

The Random Forest models were chosen for their superior performance in both classification and regression tasks. This project demonstrates the effectiveness of ensemble methods in weather prediction.

Feel free to explore the notebooks for detailed code and analysis:
- `4_random_forest_adjusted.ipynb`
- `8_random_forest_regressor.ipynb`
- `2_knn_classifier.ipynb`
- `5_gradient_boosting.ipynb`

Happy coding! 😊
