
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Syntax Check') {
            steps {
                bat 'py -3.15 -m compileall -q .'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -3.15 -m pip install --upgrade pip'
                bat 'py -3.15 -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat 'py -3.15 -m pip install flake8'
                bat 'py -3.15 -m flake8 .'
            }
        }

        stage('Test') {
            steps {
                bat 'py -3.15 -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t aceest-fitness:latest .'
            }
        }
    }

    post {
        success {
            echo 'ACEest-Fitness pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output for details.'
        }
    }
}