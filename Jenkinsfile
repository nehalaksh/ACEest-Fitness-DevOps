
pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
        MINIKUBE_HOME = '/home/s2026ht66016/.minikube'

        DOCKER_IMAGE = 'acest-fitness:latest'
        DEPLOYMENT_NAME = 'acest-fitness'

        PATH = '/usr/local/bin:/usr/bin:/bin'
    }

    stages {

        // Stage 1: Checkout source code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        // Stage 2: Check Python version
        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        // Stage 3: Install project dependencies
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

        // Stage 4: Check Python syntax
        stage('Syntax Check') {
            steps {
                sh '''
                    python3 -m compileall -q .
                    echo "Python syntax check completed"
                '''
            }
        }

        // Stage 5: Check code quality
        stage('Code Quality Check') {
            steps {
                sh '''
                    python3 -m flake8 . \
                        --exclude=.git,__pycache__,.venv \
                        --count \
                        --select=E9,F63,F7,F82 \
                        --show-source \
                        --statistics
                '''
            }
        }

        // Stage 6: Run automated tests
        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m pytest -v
                '''
            }
        }

        // Stage 7: Build Docker image
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE} .
                    docker images
                '''
            }
        }

        // Stage 8: Load Docker image into Minikube
        stage('Load Image into Minikube') {
            steps {
                sh '''
                    echo "Checking Minikube status..."

                    minikube -p minikube status

                    echo "Loading Docker image into Minikube..."

                    minikube -p minikube image load ${DOCKER_IMAGE}

                    echo "Image loading completed"
                '''
            }
        }

        // Stage 9: Deploy application to Kubernetes
        stage('Kubernetes Deployment') {
            steps {
                sh '''
                    echo "Applying Kubernetes deployment..."

                    if [ ! -f deployment.yaml ]; then
                        echo "ERROR: deployment.yaml not found"
                        exit 1
                    fi

                    kubectl apply -f deployment.yaml

                    if [ -f service.yaml ]; then
                        kubectl apply -f service.yaml
                    fi

                    echo "Kubernetes resources applied successfully"
                '''
            }
        }

        // Stage 10: Verify Kubernetes deployment
        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Waiting for application deployment..."

                    kubectl rollout status deployment/${DEPLOYMENT_NAME} \
                        --timeout=120s

                    echo "Deployment details:"
                    kubectl get deployments

                    echo "Pod details:"
                    kubectl get pods -o wide

                    echo "Service details:"
                    kubectl get services

                    echo "Kubernetes deployment verified successfully"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: ACEest Fitness CI/CD pipeline completed!'
        }

        failure {
            echo 'FAILURE: Pipeline failed. Check Console Output for details.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
