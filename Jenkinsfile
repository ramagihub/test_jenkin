pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                // Install Python dependencies (e.g., Selenium) and any other setup tasks
		    bat "cd C:\\Users\\91997\\AppData\\Local\\Programs\\Python\\Python38-32"
	
                bat "python3 -m virtualenv  venv"
		bat "source venv/bin/activate"
                bat "pip install -r requirements.txt"

            }
        }
        stage('Run Selenium Tests') {
            steps {
                // Execute your Selenium test script using Python
                bat "python login.py"
            }
        }
    }
  
}
