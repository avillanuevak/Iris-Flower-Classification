
import joblib
import pandas as pd

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width):
    """Predicts the Iris species based on input measurements."""
    try:
        # Load the trained model
        model = joblib.load('models/iris_knn_model.joblib')

        # Create a DataFrame from the input measurements
        input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                                  columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

        # Make prediction
        prediction = model.predict(input_data)

        # Map the numerical prediction to species name
        species_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
        predicted_species = species_map[prediction[0]]

        print(f"\nPredicted Iris Species: {predicted_species}")

    except FileNotFoundError:
        print("Error: Model file not found. Please ensure 'iris_knn_model.joblib' is in the 'models/' directory.")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    print("\n--- Iris Species Prediction ---")
    print("Please enter the measurements for the Iris flower:")

    try:
        s_l = float(input("Sepal Length (cm): "))
        s_w = float(input("Sepal Width (cm): "))
        p_l = float(input("Petal Length (cm): "))
        p_w = float(input("Petal Width (cm): "))

        predict_iris_species(s_l, s_w, p_l, p_w)
    except ValueError:
        print("Invalid input. Please enter numerical values for measurements.")

