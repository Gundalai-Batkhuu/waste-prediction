# Commercial and Household Waste Predictor for Australian Cities and States

## Project Overview
A machine learning-based system designed to predict commercial and household waste generation across Australian cities and states. The project utilizes advanced data analytics and multiple modeling techniques to provide accurate waste prediction forecasts.

## Technical Stack

### Core Technologies
- Python 3.10+
- Kedro 0.19.9 (Data Engineering Framework)
- Streamlit 1.29.1 (Web Application Framework)

### Machine Learning & Data Science
- XGBoost 2.1.2
- Scikit-learn 1.5.2
- Facebook Prophet
- LightGBM
- Random Forest
- Joblib (Model Serialization)

### Development Tools
- Poetry (Dependency Management)
- Jupyter Notebooks (Data Analysis & Model Development)

## Key Features

### Data Processing Pipeline
- Modular data preprocessing system
- Feature engineering and selection
- Data cleaning and transformation
- Missing value handling
- Categorical variable encoding

### Machine Learning Models

#### Ensemble Approach
- Advanced ensemble modeling strategy combining:
  - XGBoost (with categorical feature support)
  - LightGBM (gradient boosting framework)
  - Random Forest (bagging-based ensemble)
  - Weighted average ensemble methodology for final predictions

#### Model Configurations
- **XGBoost Configuration**
  - Objective: Squared Error Regression
  - Learning Rate: 0.01
  - Categorical Feature Support Enabled
  - N_estimators: 500
  - Hyperparameter Grid:
    ```python
    {
        'min_child_weight': [1, 5, 10],
        'gamma': [0.5, 1, 1.5, 2, 5],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0],
        'max_depth': [3, 4, 5]
    }
    ```

- **LightGBM Optimization**
  - Application: Regression
  - Objective: Root Mean Squared Error
  - Best Parameters (from GridSearchCV):
    - Learning Rate: 0.3
    - Max Bin: 200
    - Max Depth: 5
    - Min Data in Leaf: 20
    - Num Leaves: 200

#### Model Evaluation Framework
- Cross-Validation:
  - Stratified K-Fold validation
  - Time-series based validation for temporal predictions
- Metrics:
  - R-squared (R²) for regression performance
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)

#### Advanced Features
- Hyperparameter Optimization:
  - GridSearchCV with parallel processing (n_jobs=4)
  - Cross-validated scoring metrics
  - Exhaustive parameter space exploration

- Model Persistence:
  - Serialization using joblib
  - Standardized model saving protocol
  - Integration with Streamlit deployment

#### Time Series Components
- Facebook Prophet Integration:
  - Temporal feature engineering
  - Trend and seasonality decomposition
  - Future prediction capabilities

#### Data Handling
- Separate training approaches for:
  - 2019 and 2021 data segments
  - Mining vs non-mining waste
  - Hazardous waste specific modeling (2008, 2012, 2013)

### Statistical Analysis
- Hypothesis testing
- Statistical validation of results
- Data distribution analysis
- Correlation studies

### Visualization & Reporting
- Interactive data visualizations
- Model performance metrics
- Statistical analysis reports
- Missing data analysis using missingno

## Project Structure
The project follows the Kedro framework structure:
- `conf/`: Configuration files and parameters
- `data/`: Data storage and management
- `notebooks/`: Jupyter notebooks for analysis and modeling
- `src/`: Source code and pipeline definitions
- `app/`: Streamlit application files

## Documentation
- Sphinx documentation system
- API documentation
- Markdown documentation for pipelines
- Jupyter notebooks with analysis documentation

## Development Practices
- Version control with Git
- Modular pipeline architecture
- Test-driven development
- Code quality maintenance with linting tools

## Installation & Deployment
- Poetry-based dependency management
- Streamlit-based web application deployment
- Containerisation support
- Environment management

## Data Sources
- Australian commercial waste data
- Household waste statistics
- Regional waste management data
- Historical waste generation records

This project combines modern data engineering practices with advanced machine learning techniques to provide accurate waste prediction capabilities for Australian municipalities and states.
