pipeline {
    agent any
    stages {
        stage('Validate develop is up-to-date') {
            steps {
                git credentialsId: 'GitUSERPASS', url: 'https://github.com/morenoscar96/unittests'
                script {
                    def IS_DIFFERENT = sh(script: "git diff origin/develop...origin/master", returnStdout: true)
                    if(IS_DIFFERENT){
                        def NEW_BRANCH = "update/master-develop_2022"
                        branch_exist = sh(script:"git branch | grep  ${NEW_BRANCH}", returnStdout: true)
                        if(branch_exist) {
                        	echo "${NEW_BRANCH} already exist"
                            sh "git checkout ${NEW_BRANCH}"
                        }
                        else {
                            sh "git checkout develop && git pull"
                            sh "git checkout -b ${NEW_BRANCH}"
                    		echo "${NEW_BRANCH} has been created and pushed"
                        }
                        sh "git push origin ${NEW_BRANCH}
                    }
                }
            }
            
        }
        stage('Identify Version') {

            steps {
                git credentialsId: 'GitUSERPASS', url: 'https://github.com/morenoscar96/unittests'
                script {
                    sh '''git checkout master'''
                    def CURRENT_VERSION = sh(script: '''git describe --abbrev=0 --tags''', returnStdout: true)
                    echo "Last tag: ${CURRENT_VERSION}"
                    
                    def (_, version) = CURRENT_VERSION.split('v')
                    def version_bits = version.tokenize('\\.')
                    
                    switch(params.RELEASE_TYPE){
                        case 'major':
                            version_bits[0] = version_bits[0].toInteger() +  1
                            version_bits[1] = '0'
                            version_bits[2] = '0'
                            break
                        case 'minor':
                            version_bits[1] = version_bits[1].toInteger() +  1
                            version_bits[2] = '0'
                            break
                        case 'patch':
                            version_bits[2] = version_bits[2].toInteger() +  1
                            break
                        default:
                            throw new Exception("Invalid release type: ADD_HERE")
                            
                    }
                    
                    env.NEW_VERSION = version_bits.join('.') 
                    echo "New version: ${NEW_VERSION}"
                    
                    slackSend channel: '#jenkins', 
                        color: 'good',
                        message: """
                        *VERSIONING INFO*\n*Release type:* ${params.RELEASE_TYPE}\n*Last prod tag:* ${CURRENT_VERSION}\n*New Version:* ${env.NEW_VERSION}
                        """
                }              
                   
            }

            post {
                failure {
                    slackSend channel: '#jenkins', 
                        color: 'danger',
                        message: """*VERSIONING INFO*\n Invalid release type:* ${params.RELEASE_TYPE}*"""
                }
            }
        }
        stage('Creating RC PR') {
            steps {
                git credentialsId: 'GitUSERPASS', url: 'https://github.com/morenoscar96/unittests'
                script{
                    def NEW_RELEASE="release/${env.NEW_VERSION}"
                    sh """#!/bin/bash
                    #change to develop
                    git checkout develop && git pull

                    #create new or checkout to release branch
                    if [ `git branch | grep  ${NEW_RELEASE}` ]
                    then
                        echo "${NEW_RELEASE} already exist"
                        git checkout ${NEW_RELEASE}
                    else
                        git checkout -b ${NEW_RELEASE}
                        echo "${NEW_RELEASE} has been created and pushed"
                    fi
                    git push origin ${NEW_RELEASE}
                    """    
                }
                
            }
        }
    }
}
