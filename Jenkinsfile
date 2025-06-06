pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'Construyendo el proyecto...'
      }
    }
    stage('Test') {
      steps {
        echo 'Ejecutando pruebas...'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose down -v'
        sh 'docker-compose uo -d -build'
      }
    }
  }
}
