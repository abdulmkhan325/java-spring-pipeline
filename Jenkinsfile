/* groovylint-disable CompileStatic, Indentation, LineLength, NestedBlockDepth, NoDef, UnnecessaryGString, UnnecessaryGetter, VariableTypeRequired */
pipeline {
    agent any

    environment {
      SONAR_URL = "http://13.239.34.240:9000/"  
      JFROG_URL = "http://13.239.34.240:8082/"
      JFROG_REPO = "java-spring-webapp-repo"
      REPO_TYP = "generic"
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
        stage('Create Repository in JFrog Artifactory') {
            steps {
                script {  
                    def repositoryExists = sh(script: "curl -s -o /dev/null -w '%{http_code}' ${JFROG_URL}/artifactory/api/repositories/${JFROG_REPO}", returnStdout: true).trim()
            
                    if (repositoryExists != "200") {
                        // Call the Python script to create the repository
                        sh "python create_artifact_repo.py ${JFROG_URL} ${JFROG_REPO} ${REPO_TYP} ${JFROG_USR_NAME} ${JFROG_USR_PASS}"
                    } else {
                        echo "Repository '${JFROG_REPO}' already exists"
                    }
                }
            }
        }
        // stage('Python Script to Upload WAR') {
        //     steps {
        //         script {
        //             def warFile = sh(script: 'ls target/*.war', returnStdout: true).trim()
        //             if (warFile.isEmpty()) {
        //                 error 'WAR file not found'
        //             } else {
        //                 def warFileName = warFile.split('/')[-1]
        //                 def uploadUrl = "https://<your-artifactory-url>/your-repository/${warFileName}"

        //                 // Call the Python script to upload the WAR file to Artifactory
        //                 sh "python <path-to-your-python-script> ${warFile} ${uploadUrl}"
        //             }       
        //         }
        //     }
        // }
    }
}
