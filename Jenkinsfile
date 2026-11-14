pipeline {
    agent any

    environment {
        PYTHON = 'C:\Users\student\AppData\Local\Python\bin\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python Application'
                bat '"%PYTHON%" -m py_compile app.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Executing application test'
                bat '"%PYTHON%" -m py_compile app.py'
                echo 'Test completed successfully'
    }
}
        stage('Run Application') {
            steps {
                bat '"%PYTHON%" app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }
        failure {
            echo 'CI Pipeline failed'
        }
    }
}
