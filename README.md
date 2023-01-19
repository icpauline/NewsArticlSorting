# News Articl Sorting
## 1. Introduction
## 2. Project Scope
## 3. Project Methodology:
### 3.1 Architectural Diagram:
### 3.2 Terminologies:
### 3.3 System Requirements:
### 3.4 Tools Used:
!
### 3.5 Interfaces:
  - Input and output news articles are of text format SSH (Secure Shell)
  - SSH (Secure Shell) protocol is used to transfer text messages
  - Syntax error and logical errors are taken into consideration
### 3.6 Error Handling:
The model handled getting inputs, grammatical errors, vector conversion errors, pickle loading, and data transformations with separate exception handlers.!
### 3.7 Performance:
Expected response times
  - The system logged every event so that the user knows which process is running internally.
  - The system identifies at which step logging required.
  - The system logged each and every system flow
### 3.8 Resource Usage:
When a task is performed, it used all the processing power available until its work done.
## 4. Projet Execution
### 4.1 Data Export:
The accumulated data from database is exported in csv format for model training.
### 4.2 Data Processing:
  -	Category names are converted to numerical forms
  - Duplicate values are removed
  - Stop words are removed.
### 4.3 Word to Vectors:
  - Each word is converted to vector using TF-IDF vectorization method
  - Maximum of 5000 features is taken into consideration
### 4.4 Train Test Split:
Data are separated for training and testing purpose. For testing purpose 30% of data is used.
### 4.5 Model Training
The models used for training are logistic Regression, SVC, linear SVC, Decision Tree Classifier, Random Forest Classifier, K Neighbors Classifier, Multinomial Naïve Bayes Classifier, Gaussian Naïve Bayes, and Bernoulli’s Naïve Bayes. Among all these methods Multinomial Naïve Bayes performed well.
### 4.6 Performance Evaluation:
The model's performance was assessed using accuracy score. A 97% accuracy rate was achieved via the Multinomial Naive Bayes algorithm
## 5. Deployment:
The model is deployed using an AWS EC2 instance. Both HTML and CSS were used to design the website. The flask API was used to deploy the model in an AWS EC2 instance.
## 6. Conclusion:
The document included a thorough description of the News Article Sorting Project. News Article Sorting will classify every news article to different categories. This is done based on the learning made by the model. The model is trained with thousands of news articles with their classification to do better prediction. The model could classify any news article with 97% accuracy.  Anyone can utilize the model because it has been installed in an AWS EC2 instance. The project can be enhanced by including user-specific recommendations.
