pipeline {
    agent any 
	environment {
        APP_NAME = "home-task"
		TAG = "${env.BRANCH}.${env.COMMIT_HASH}.${env.BUILD_NUMBER}"
		}
    stages {
        stage('Gitlab Login') {
            steps {
                withCredentials([
						string(credentialsId: 'gitlab_user', variable: 'USR'),
						string(credentialsId: 'gitlab_password	', variable: 'PW'),
					]){
						sh '''
							docker login registry.gitlab.com -u ${USR} -p ${PW} 
							echo "Login OK!"
						'''
					  }
            }
        }
		stage('Build Image') {
            steps {
                sh '''
		docker build -t registry.gitlab.com/tasks6711629/task1/app:v${BUILD_NUMBER} .
                docker push registry.gitlab.com/tasks6711629/task1/app:v${BUILD_NUMBER}
                echo "${BUILD_NUMBER}"
                '''
            }
        }
    }
}
