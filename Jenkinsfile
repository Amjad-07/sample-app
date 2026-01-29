pipeline {
  agent any

  environment {
    PROJECT_ID = "neat-pagoda-477804-m8"
    REGION     = "asia-south1"
    REPO       = "sample-repo"

    BACKEND_SERVICE  = "sample-backend"
    FRONTEND_SERVICE = "sample-frontend"

    BACKEND_IMAGE  = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/sample-backend:latest"
    FRONTEND_IMAGE = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/sample-frontend:latest"
  }

  stages {

    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Build Images") {
      steps {
        sh """
          docker build -t ${BACKEND_IMAGE} ./backend
          docker build -t ${FRONTEND_IMAGE} ./frontend
        """
      }
    }

    stage("Auth Docker to Artifact Registry") {
      steps {
        sh """
          gcloud auth configure-docker ${REGION}-docker.pkg.dev -q
        """
      }
    }

    stage("Push Images") {
      steps {
        sh """
          docker push ${BACKEND_IMAGE}
          docker push ${FRONTEND_IMAGE}
        """
      }
    }

    stage("Deploy Backend to Cloud Run") {
      steps {
        sh """
          gcloud run deploy ${BACKEND_SERVICE} \
            --image ${BACKEND_IMAGE} \
            --region ${REGION} \
            --platform managed \
            --allow-unauthenticated \
            --port 8080
        """
      }
    }

    stage("Deploy Frontend to Cloud Run") {
      steps {
        sh """
          gcloud run deploy ${FRONTEND_SERVICE} \
            --image ${FRONTEND_IMAGE} \
            --region ${REGION} \
            --platform managed \
            --allow-unauthenticated \
            --port 80
        """
      }
    }
  }
}
