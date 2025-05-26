pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vishnuprasad-23/flask-demo-jenkins.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build App') {
            steps {
                sh 'python app.py &'
            }
        }
    }

    post {
        success {
            echo 'Build and test succeeded.'
        }
        failure {
            echo 'Something went wrong.'
        }
    }
}
