pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        DOCKER_IMAGE_FRONTEND = "khalildiop25/frontend"
        DOCKER_IMAGE_BACKEND = "khalildiop25/backend"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/khalildiop25/projet-systeme-repartie1.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE_FRONTEND:latest ./frontend'
                sh 'docker build -t $DOCKER_IMAGE_BACKEND:latest ./backend'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push $DOCKER_IMAGE_FRONTEND:latest'
                sh 'docker push $DOCKER_IMAGE_BACKEND:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}

