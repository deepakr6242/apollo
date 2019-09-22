pipeline {
  agent any
  stages {
    stage('stage A') {
      steps {
        sh 'echo running stageA'
      }
      
          stage('stage B') {
      steps {
        sh 'echo running stageB'
      }
    }
  }
}
