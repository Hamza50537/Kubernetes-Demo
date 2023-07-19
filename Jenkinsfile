pipeline {
    agent any 
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
    }
}
