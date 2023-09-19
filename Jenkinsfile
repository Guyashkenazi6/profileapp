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
    image: drpsychick/dind-buildx-helm
    alwaysPull: true
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
        stage('Build and push helm chart') {
            steps {
                container('dind') {
                    script {
                        withCredentials([usernamePassword(credentialsId: 'dockerHubCreds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                            sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            helm package helmapp
                            helm push helmapp-0.1.0.tgz  oci://registry-1.docker.io/guyashkenazi
                            helm package helmmongo
                            helm push helmdb-0.1.0.tgz  oci://registry-1.docker.io/guyashkenazi
                            '''
                        }
                    }
                }
            }
       }
    }
 post {
        failure {
            emailext (
                to: 'guy0204@gmail.com',
                subject: "Failed: ${currentBuild.fullDisplayName}",
                body: "The build failed. Please check the Jenkins build log for details.",
                attachLog: true,
            )
        }
    }
}
