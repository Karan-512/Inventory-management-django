pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "${env.JOB_NAME}" 
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'sudo docker compose down'
                    sh 'sudo docker compose up -d --force-recreate --no-deps --build web'
                }
            }
        }

        stage('Testing') {
            steps {
                script {
                    sh 'sudo docker exec ${COMPOSE_PROJECT_NAME}-web-1 python3 manage.py test'
                }
            }
        }
    }

    post {
        always {
            echo 'Build completed.'
        }
    }
}
