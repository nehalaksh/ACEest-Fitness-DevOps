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
                sh 'python3 --version'
                sh 'python3 -m compileall -q .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pip install flake8 pytest'
            }
        }

        stage('Lint') {
            steps {
                sh 'python3 -m flake8 .'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
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
