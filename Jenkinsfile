
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
                sh 'py -3.15 -m compileall -q .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'py -3.15 -m pip install --upgrade pip'
                sh 'py -3.15 -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'py -3.15 -m pip install flake8'
                sh 'py -3.15 -m flake8 .'
            }
        }

        stage('Test') {
            steps {
                sh 'py -3.15 -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness:latest .'
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
