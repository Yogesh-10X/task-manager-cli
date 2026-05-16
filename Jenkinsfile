pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Yogesh-10X/devops-task-manager.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-manager .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f task-manager-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -dit --name task-manager-container task-manager'
            }
        }
    }
}