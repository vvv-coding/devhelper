# Lab 4: Jenkins

## Step 1: Start Jenkins Service
### Dashboard Tasks
1. Check http://localhost:8080

### Commands
```bash
sudo systemctl start jenkins
```

## Step 2: Running Jenkins Pipelines
### Dashboard Tasks
1. Create pipeline in the jenkins dashboard under new Item
2. Pipeline name pipelinedemo
3. Run the pipeline
4. Create a freestyle job
5. Archive the artifact 
6. Run the artifact
7. Write pipeline name and select pipeline
8. Edit pipeline script

### Commands
```file:pipeline
pipeline {
    agent any

    stages {
        stage('Check Python'){
            steps {
                sh 'python3 --version'
            }
        }

        stage('Build'){
            steps {
                git branch: 'master'
                    url: 'https://github.com/[account]/[repo].git'
                    sh 'python3 demo.py > output.txt'
            }
        }

        stage('Archive'){
            steps {
                archiveArtifacts artifacts: 'output.txt'
            }
        }

        stage('Deploy/Use'){
            steps {
                sh 'date'
                sh 'cat output.txt' 
            }
        }
    }
}
```

## Step 3: Saving Jenkins Artefact
### Dashboard Task
1. Save and build
2. Check console output for results

### Commands
```bash
```

## Step 4: Adding Triggers
### Dashboard Tasks
1. Create freestyle project
2. Build Trigger add projects to watch and add the job
3. Select execute and add the below commands
4. Install plugin Build Pipeline
5. Create new view and select build pipeline view and create
6. Give title name and initial job with configurations
7. 1, Just the pipeline number, Just the build name and number, 60 , - , Lightbox
8. Visualize pipeline
9. On configuration of job 1 add post build action with job 2 and click save
10. Go to dashboard and click pipeline view

### Commands
```bash
echo $BUILD_NUMBER
python3 -c "import datetime; print(datetime.datetime.now())
```