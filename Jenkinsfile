pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                // Install Python dependencies (e.g., Selenium) and any other setup tasks
                python3 -m virtualenv -p  venv
		        source venv/bin/activate
                pip install -r requirements.txt

            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Execute your Selenium test script using Python
                python login.py
            }
        }
    }

    post {
        always {
            // Clean up any resources or artifacts here if needed
        }
    }
}
}
