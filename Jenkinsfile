
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat 'python -m py_compile app.py test_app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated tests'
                bat 'python -m unittest -v test_app'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running Python application'
                bat 'python app.py'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }

        failure {
            echo 'CI pipeline failed'
        }
    }
}
