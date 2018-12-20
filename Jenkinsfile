pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // sh 'build step command'
            }        
        }
        
      
        stage("SonarQube analysis") {
            steps {
                withSonarQubeEnv('sonar') {
                        // sh './sonar/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner -Dsonar.projectKey=testproject -Dsonar.sources=/root/examples/ -Dsonar.host.url=http://localhost:9000 -Dsonar.login=b6029f0cfea17d68ee8aa0607b7b2aea6683dfb5 -Dsonar.bandit.reportPath=/root/banditReport.json -Dson'
                }
            }
        }
        
        stage('Bandit Analysis') {
            steps {
                sh 'bandit -r ./python-app -o report.json -f json'
            }
            post {
                always {
                     sh '/sonar/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner -Dsonar.projectKey=python -Dsonar.sources=./python-app -Dsonar.host.url=http://sonarqube:9000 -Dsonar.login=9ba67e580e0b13f75b07404f028732945c66a219 -Dsonar.bandit.reportPath=./report.json'
              
                }
            }
        }
        
        stage('Deliver for development') {
            when {
                branch 'development' 
            }
            steps {
                input message: 'Deploy for development ? (Click "Proceed" to continue)'
                //sh 'Deploying to development ...'
            }
        }
        
         stage('Security Gate') {
             steps {
                sh 'sleep 5s'
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        def result = waitForQualityGate()
                        if (result.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${result.status}"
                        } else {
                            echo "Quality gate passed with result: ${result.status}"
                        }
                    }
                }

            }
        }
        
        stage('Deploy for production') {
            when {
                branch 'production'  
            }
            steps {
                input message: 'Deploy to production ? (Click "Proceed" to continue)'
                //sh 'Deploying to production ...'
            }
        }
        
    }
}
