pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vishnuprasad-23/flask-demo-jenkins.git'
            }
        }

        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('Build App') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    nohup python app.py &
                '''
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
