# Credit Approval Prediction

A machine learning project for predicting whether a loan application should be approved or denied based on applicant information.

## Overview

This project uses a trained scikit-learn model to evaluate a set of financial and personal features from a credit approval dataset. The repository includes a Streamlit app where users can input application values and receive a prediction.

## Features

- Credit approval classification using a trained ML model
- Streamlit-based interactive web interface
- Applicant feature inputs for decision making
- Simple, lightweight deployment for demos and experimentation

## Project Structure

```text
creditApproval-ML/
├── CreditApproval.ipynb     # Model training and exploration notebook
├── CreditApprovalPy.py       # Streamlit application
├── CreditApproval.pkl        # Trained model
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## Tech Stack

- Python
- NumPy
- scikit-learn
- Streamlit
- Joblib

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Z3emah/creditApproval-ML.git
cd creditApproval-ML
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run CreditApprovalPy.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

## Usage

- Enter the applicant feature values in the sidebar.
- Click the `Ask Oracle` button.
- The model returns a prediction: either `Approve Loan` or `Deny Loan`.

## Model Notes

The model is saved in `CreditApproval.pkl` and is loaded by the Streamlit app. This project is intended as a demo or educational ML application and should not be treated as a real financial decision-making system.

## Disclaimer

This project is for educational and demonstration purposes only. It is not a professional credit risk model and should not be used for real financial decisions.

## License

This project does not currently include a license file. Please confirm repository licensing terms before reusing or distributing the code in a production or commercial context.

## Author

Z3emah
