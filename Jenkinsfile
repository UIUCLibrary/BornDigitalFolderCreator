node {
    stage("Cloning"){
      checkout scm
      stash includes: '*', name: 'source'
    }
}
node {
    stage("Running Tox"){
        unstash 'source'
        sh '$TOX'
        junit '**/junit-*.xml'
    }
    stage("Packaging source"){
        sh '$PYTHON3 setup.py sdist'
        archiveArtifacts artifacts: 'dist/CreateFolders*.tar.gz', excludes: null
    }
}
