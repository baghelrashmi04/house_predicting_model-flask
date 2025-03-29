# Housing Price Predictor Web App

This project is a Flask web application that predicts housing prices using a trained Random Forest regression model. Users can input various housing features through a web form, and the app will return a predicted price.




#########################
## Installation

1.  Clone the repository:

    ```bash
    git clone <your-repository-url>
    ```

2.  Navigate to the project directory:

    ```bash
    cd learning_om
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv ll_env
    ```

4.  Activate the virtual environment:

    * macOS/Linux:

        ```bash
        source ll_env/bin/activate
        ```

    * Windows:

        ```bash
        ll_env\Scripts\activate
        ```

5.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```


##############################

## Usage

1.  Run the Flask application:

    ```bash
    python app.py
    ```

2.  Open your web browser and go to `http://127.0.0.1:5000/`.
3.  Enter the housing data in the provided form.
4.  Click the "Predict" button to get the predicted housing price.