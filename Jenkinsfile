pipeline {
    agent {
        docker {
            image 'python:3.10' // Using the Python Docker image
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Skinny911/pipeline_project.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python3 -m unittest discover -s tests -p "test_*.py" > test_results.txt
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
            deleteDir() // Runs fine because it is already in the context of the Docker agent
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for more details.'
        }
    }
}
