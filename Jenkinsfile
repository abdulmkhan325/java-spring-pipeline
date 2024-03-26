pipeline {
  agent any 

  stages {
    stage('Checkout') {
      steps {
        sh 'echo passed'
        //git branch: 'test', url: 'https://github.com/abdulmkhan325/java-spring-pipeline.git'
      }
    }
    stage('Check Maven') {
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
    stage('Build with Maven') {
      steps {
        sh 'echo Build and Test'
        sh 'mvn -version'
        //sh 'cd java-spring-pipeline'
        sh 'ls -ltr'
        // build the project and create a WAR file
        //sh 'cd java-spring-pipeline && mvn clean package'
      }
    }   
  }
}
