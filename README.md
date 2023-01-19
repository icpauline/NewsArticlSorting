# News Articl Sorting
## 1. Introduction
## 2. Project Scope
## 3. Project Methodology:
### 3.1 Architectural Diagram:
<img width="436" alt="Arch" src="https://user-images.githubusercontent.com/115965062/213541207-800c4f47-aa75-4117-b4ea-e8fd747500a7.png">
### 3.2 Terminologies:
| Term  | Description |
| ------------- | ------------- |
| ML  | Machine Learing  |
| API  | Application Programming Interface  |
| Flask  | Framework for deploying the model   |
| AWS  | Amazon Web Service  |
| EC2  | Elastic Compute Cloud   |
| NLP  | Natural Language Processing   |
| SSH  | Secure Shell  |
### 3.3 System Requirements:
  - Windows 7 and above
  - SQL
  - PyCharm
  - HTML
  - CSS
  - WinSCP
  - AWS Account
### 3.4 Tools Used:
<img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537318-d7fb3e62-49d4-4e3c-8714-506588afae78.png">   <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537317-8b726416-bde7-4e4e-9874-c28488d3a7dd.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537315-484a3265-9c1c-43e2-bb46-c35ab1ee64fe.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537311-6149db2a-99e6-4fb7-9d6a-9216a4c352d8.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537309-d37fad0e-65ee-4da4-a176-b5c32a2b9a0d.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537307-57662137-00eb-4472-8b30-921eb42d8d23.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537306-d646f595-9019-4c21-9573-e5f76f76e317.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537303-b020cbbc-f6ff-4942-b175-0438d7a4be1a.png">    <img width=“90” alt="re_logo" src="https://user-images.githubusercontent.com/115965062/213537301-42266a6d-ba61-487b-90c1-627d85b783a9.png">
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
