pipeline {
    agent any
     parameters {
    string(name1: 'USERNAME')
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa1', 'prod'], description: 'Select the deployment environment')}

    stages { 
        
        stage('Setup') {
            steps {
                // Install Python dependencies (e.g., Selenium) and any other setup tasks
		 bat "cd C:\\Users\\91997\\AppData\\Local\\Programs\\Python\\Python38-32"
		bat "python -m venv myenv"
		bat "C:\\Users\\91997\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\myenv\\Scripts\\activate.bat"
                bat "pip install -r requirement.txt"

            }
        }
        stage('Run Selenium Tests') {
            steps {
                // Execute your Selenium test script using Python
		    bat "cd D:\\sample_jenkins"
		    echo "Hello, ${USERNAME}!"
       		    echo "Deploying to ${ENVIRONMENT}"
		    // bat "pytest --alluredir=allure-report1/ test_login.py"
            }
        }
    }
  
}
