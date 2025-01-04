pipeline {
    agent {
        docker {
            image 'python:3.10' // Using the Python Docker image
        }
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Skinny911/pipeline_project.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m unittest discover -s tests -p "test_*.py" > test_results.txt
                cat test_results.txt # Display test results in Jenkins console
                '''
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'test_results.txt', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for more details.'
        }
    }
}
