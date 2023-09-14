pipeline {
    agent {
        kubernetes {
            label 'dind-agent'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: dind
    image: docker:dind
    env:
    - name: DOCKER_HOST
      value: unix:///var/run/docker-dind.sock
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /var/run
      name: docker-sock
  volumes:
  - name: docker-sock
    emptyDir: {}
"""
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'githubCreds', url: 'https://github.com/Guyashkenazi6/profileapp.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                container('dind') {
                    script {
                        sh 'dockerd &'
                        sh 'sleep 5'
                        sh 'docker build -t guyashkenazi/profile-app:latest .'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                container('dind') {
                    script {
                        echo "Running tests..."
                        sh 'docker run guyashkenazi/profile-app:latest test_app.py'
                        echo "Tests completed successfully!"
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                container('dind') {
                    withCredentials([usernamePassword(credentialsId: 'dockerHubCreds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push guyashkenazi/profile-app:latest
                        '''
                    }
                }
            }
        }
    }
}
