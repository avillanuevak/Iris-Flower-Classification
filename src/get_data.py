import pandas as pd
from sklearn.datasets import load_iris
import os

def get_data():
    """Downloads the Iris dataset and saves it to a CSV file."""
    try:
        iris = load_iris()

        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target

        output_dir = 'data'
        output_path = os.path.join(output_dir, 'iris.csv')
        
        os.makedirs(output_dir, exist_ok=True)

        df.to_csv(output_path, index=False)

    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        print(traceback.format_exc())

if __name__ == '__main__':
    get_data()