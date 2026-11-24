
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'acest-fitness'
        IMAGE_TAG = 'latest'
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
        DEPLOYMENT_NAME = 'acest-fitness'
        CONTAINER_NAME = 'fitness-app'
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --user --upgrade pip

                    if [ -f requirements.txt ]; then
                        python3 -m pip install --user -r requirements.txt
                    fi

                    python3 -m pip install --user pytest flake8
                '''
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python3 -m compileall -q .'
                echo 'Python syntax check completed'
            }
        }

        stage('Code Quality Check') {
            steps {
                sh '''
                    python3 -m flake8 . \
                    --exclude=.git,__pycache__,.venv \
                    --exit-zero
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    if find . -name "test_*.py" \
                       -o -name "*_test.py" | grep -q .; then
                        python3 -m pytest -v
                    else
                        echo "No test files found. Skipping tests."
                    fi
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker images
                '''
            }
        }

        stage('Load Image into Minikube') {
            steps {
                sh '''
                    minikube image load ${IMAGE_NAME}:${IMAGE_TAG}
                    minikube image ls | grep ${IMAGE_NAME}
                '''
            }
        }

        stage('Kubernetes Deployment') {
            steps {
                sh '''
                    kubectl apply -f deployment.yaml

                    if [ -f service.yaml ]; then
                        kubectl apply -f service.yaml
                    fi
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl rollout status deployment/${DEPLOYMENT_NAME} \
                    --timeout=120s

                    kubectl get pods
                    kubectl get services
                    kubectl get deployments
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
            echo 'ACEest Fitness application deployed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
