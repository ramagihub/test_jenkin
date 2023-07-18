pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                // Install Python dependencies (e.g., Selenium) and any other setup tasks
                bat "python3 -m virtualenv -p  venv"
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
