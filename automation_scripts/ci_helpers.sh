#!/bin/bash

# Common CI/CD helper functions

function print_status() {
  local msg="$1"
  echo "[CI STATUS] $msg"
}

function run_tests() {
  # Run tests and fail immediately on error
  print_status "Running unit tests..."
  npm test || { echo "Tests failed"; exit 1; }
  print_status "All tests passed."
}

function build_project() {
  print_status "Building project..."
  npm run build || { echo "Build failed"; exit 1; }
  print_status "Build completed."
}

function deploy() {
  print_status "Deploying application..."
  # Example deploy command
  ./deploy_app.sh
  print_status "Deployment finished."
}

# Run all on invocation if no args
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  run_tests
  build_project
  deploy
fi
