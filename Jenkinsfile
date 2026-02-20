pipeline {
    agent any

    environment {
        DOCKER_IMAGE_FRONTEND = "khalildiop767/frontend"
        DOCKER_IMAGE_BACKEND  = "khalildiop767/backend"
    }

    stages {

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -t $DOCKER_IMAGE_FRONTEND:latest ./frontend
                    docker build -t $DOCKER_IMAGE_BACKEND:latest ./backend
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE_FRONTEND:latest
                        docker push $DOCKER_IMAGE_BACKEND:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

    }
}

