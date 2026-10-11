groovy

pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Syntax') {
            steps {
                sh 'python3 -m compileall -q app.py tests'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '.venv/bin/ruff check app.py tests'
            }
        }

        stage('Unit Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build --target test \
                        -t aceest-fitness:test-${BUILD_NUMBER} .
                    docker run --rm aceest-fitness:test-${BUILD_NUMBER}
                    docker build --target runtime \
                        -t aceest-fitness:jenkins-${BUILD_NUMBER} .
                '''
            }
        }
    }

    post {
        success {
            echo 'ACEest Fitness BUILD passed.'
        }
        failure {
            echo 'BUILD failed. Review the console logs.'
        }
        always {
            cleanWs()
        }
    }
}