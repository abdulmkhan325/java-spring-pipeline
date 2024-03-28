pipeline {
  agent any

  stages {
    stage('Check Code Path') {
      steps {
        sh 'echo passed'
        sh 'pwd'
        //git branch: 'test', url: 'https://github.com/abdulmkhan325/java-spring-pipeline.git'
      }
    }
    stage('Check or Install Python3') {
      steps {
        script {
          // Check if Python 3 is installed
          def pythonInstalled = sh(script: 'command -v python3', returnStatus: true)
          if (pythonInstalled != 0) {
            echo 'Python 3 not found, installing...'
            sh 'sudo yum install -y python3'
                    } else {
            echo 'Python 3 is already installed'
          }
        }
      }
    }
    stage('Check or Install Maven') {
      steps {
        script {
          // Check if Maven is installed
          def mvnInstalled = sh(script: 'command -v mvn', returnStatus: true)
          if (mvnInstalled != 0) {
            // Install Maven if not found
            echo 'Maven not found, installing...'
            sh 'sudo yum install -y maven'
            } else {
            echo 'Maven is already installed'
          }
        }
      }
    }
    stage('Check SonarQube Server Reachability') {
      steps {
        script {
            def response = sh(script: "curl -IsS ${SONAR_URL} | head -n 1 | cut -d' ' -f2", returnStdout: true).trim()
            if (response != '200') {
                error "SonarQube server is not reachable. HTTP response code: ${response}"
            } else {
                echo "SonarQube server is reachable"
            }
        }
      }
    }   
    stage('Build with Maven') {
      steps { 
        sh 'ls -ltr'
        sh 'mvn clean package || { echo "Maven build failed"; exit 1; }'
      }
    }
    stage('Check WAR file existence') {
      steps {
                script {
                    def warFile = sh(returnStdout: true, script: 'find target -name "*.war"').trim()
                    if (warFile.isEmpty()) {
                        error 'WAR file not found'
                    } else {
                        echo "Found WAR file: $warFile"
                    }
                }
            }
    } 
    stage('Static Code Analysis') {
      environment {
        SONAR_URL = "http://3.106.57.229:9000/"
      }
      steps {
        withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) { 
          sh 'mvn sonar:sonar -Dsonar.login=$SONAR_AUTH_TOKEN -Dsonar.host.url=${SONAR_URL}'
        }
      }
    }
  }
}
