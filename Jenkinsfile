pipeline {
    agent any 
	environment {
        APP_NAME = "home-task"
		TAG = "${env.BRANCH}.${env.COMMIT_HASH}.${env.BUILD_NUMBER}".drop(15)
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
                echo "${TAG}"
                '''
            }
        }
    }
}
