/* groovylint-disable CompileStatic, Indentation, LineLength, NestedBlockDepth, NoDef, UnnecessaryGString, UnnecessaryGetter, VariableTypeRequired */
pipeline {
    agent any

    environment {
      WAR_FILE_PATH = "target/*.war"
      SONAR_URL = "http://13.239.34.240:9000/"  
      JFROG_URL = "http://13.239.34.240:8082/artifactory/a1-java-spring-webapp-repo/" 
      JFROG_USR_NAME = credentials('jfrog-username')   
      JFROG_USR_PASS = credentials('jfrog-password')
    }
    
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
        // stage('Check SonarQube Server Reachability') {
        //   steps {
        //     script {
        //       def responseCode = sh(script: "curl -IsS --max-time 5 ${SONAR_URL} | head -n 1 | cut -d' ' -f2", returnStdout: true).trim() 
        //       if (responseCode == "200") {
        //         echo "SonarQube server is reachable"
        //       } else {
        //         error "SonarQube server is not reachable. HTTP response code: ${responseCode}"
        //       }
        //     }
        //   }
        // }
        stage('Build with Maven') {
            steps { 
                sh 'ls -ltr'
                sh 'mvn clean package || { echo "Maven build failed"; exit 1; }'
            }
        }
        stage('Check WAR file') {
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
        // stage('Static Code Analysis') {
        //     steps {
        //         withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) {
        //             sh "mvn sonar:sonar -Dsonar.login=$SONAR_AUTH_TOKEN -Dsonar.host.url=${SONAR_URL}"
        //         }
        //     }
        // }
        stage('Upload WAR using Python Script') {
            steps {
                def response  = sh(script: "curl -s -o /dev/null -w '%{http_code}' ${JFROG_URL}", returnStdout: true).trim()
                    if (response == "200") {
                        echo 'JFrog repository already exists. Proceeding with upload...'
                        sh "python3 upload_to_artifactory.py ${WAR_FILE_PATH} ${JFROG_URL} ${JFROG_USR_NAME} ${JFROG_USR_PASS}"
                    } else {
                        echo "JFrog repository does not exist"
                }
            }
        }
    }
}
