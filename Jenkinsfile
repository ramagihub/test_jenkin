pipeline {
    agent any
    stages { 
        
        stage('Setup') {
            steps {
                // Install Python dependencies (e.g., Selenium) and any other setup tasks erre
		 bat "cd C:\\Users\\91997\\AppData\\Local\\Programs\\Python\\Python38-32"
		bat "python -m venv myenv"
		bat "C:\\Users\\91997\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\myenv\\Scripts\\activate.bat"
                bat "pip install -r requirement.txt"

            }
        }
        stage('Run Selenium Tests') {
            steps {
       		 bat "pytest --alluredir=allure-report1/ test_login.py"
            }
        }
    }
  
}
