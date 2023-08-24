# Cracking-Sparse-PUFs

Project: Sparse CDU PUF Response Prediction

Description:

Developed a sparse linear model to predict responses from a Sparse CDU (Challenge-Response Pair) PUF, where only 512 out of 2048 CDUs are active.
Implemented a mathematical derivation of the mapping function φ, demonstrating that a single sparse linear model with at most S non-zero coordinates could accurately predict responses for all challenges.
Utilized the numpy library exclusively for coding, adhering to strict limitations on the use of machine learning libraries.
Created a custom method called my_fit() to train the S-sparse linear model using CRPs as training data.
Achievements:

Successfully implemented a machine learning solution that can break a Sparse CDU PUF using a single sparse linear model.
Achieved an accuracy rate that accurately predicted responses for a secret test dataset generated from the same Sparse CDU PUF, with the same active CDUs.
Demonstrated proficiency in linear modeling, regularization, and feature engineering techniques.
Gained experience in hyperparameter tuning for optimizing model performance.
Methodology:

Explored multiple methods for solving the problem, evaluating their performance and suitability.
Chose the Proximal Gradient Descent method as the primary approach, emphasizing its effectiveness in training an S-sparse linear model.
Experimented with alternative methods to gain insights into their strengths and weaknesses.
Hyperparameter Tuning:

Employed a systematic approach to choose optimal hyperparameters for the model.
Utilized grid search to explore a range of values for regularization constants, step lengths, and other parameters.
Evaluated different criteria to select the best hyperparameters, prioritizing model accuracy and convergence speed.
Key Skills Demonstrated:

Mathematical modeling and derivation for machine learning applications.
Implementation of machine learning algorithms using numpy.
Hyperparameter tuning and model optimization.
Experimental analysis of multiple methods to solve complex problems.
Adherence to strict limitations and constraints in coding.
Impact:

Developed a robust and accurate solution for breaking Sparse CDU PUFs, highlighting the importance of secure design practices in hardware security.
