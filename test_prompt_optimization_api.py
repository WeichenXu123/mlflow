#!/usr/bin/env python3
"""
Test script for the prompt optimization job API endpoints.
"""

import json
import requests
import time

# MLflow server URL (adjust as needed)
BASE_URL = "http://localhost:5000"

def test_create_job():
    """Test creating a prompt optimization job."""
    print("Testing create job...")
    
    url = f"{BASE_URL}/ajax-api/3.0/mlflow/optimize-prompts"
    data = {
        "dataset_url": "https://example.com/dataset.csv",
        "prompt_url": "https://example.com/prompt.txt",
        "scorer_names": ["accuracy", "relevance"],
        "config": {
            "targetLLM": "gpt-4",
            "algorithm": "dspy"
        }
    }
    
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        job_id = result.get("job_id")
        print(f"Created job with ID: {job_id}")
        return job_id
    else:
        print("Failed to create job")
        return None

def test_get_job(job_id):
    """Test getting a job by ID."""
    print(f"\nTesting get job {job_id}...")
    
    url = f"{BASE_URL}/ajax-api/3.0/mlflow/optimize-prompts/{job_id}"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Job status: {result.get('status')}")
        return result
    else:
        print("Failed to get job")
        return None

def test_list_jobs():
    """Test listing all jobs."""
    print("\nTesting list jobs...")
    
    url = f"{BASE_URL}/ajax-api/3.0/mlflow/optimize-prompts"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        jobs = result.get("jobs", [])
        print(f"Found {len(jobs)} jobs")
        return jobs
    else:
        print("Failed to list jobs")
        return []

def test_cancel_job(job_id):
    """Test canceling a job."""
    print(f"\nTesting cancel job {job_id}...")
    
    url = f"{BASE_URL}/ajax-api/3.0/mlflow/optimize-prompts/{job_id}/cancel"
    response = requests.post(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        print("Job canceled successfully")
        return True
    else:
        print("Failed to cancel job")
        return False

def main():
    """Run all tests."""
    print("Testing Prompt Optimization Job API")
    print("=" * 40)
    
    # Test creating a job
    job_id = test_create_job()
    if not job_id:
        print("Cannot continue without a job ID")
        return
    
    # Wait a moment
    time.sleep(1)
    
    # Test getting the job
    test_get_job(job_id)
    
    # Test listing jobs
    test_list_jobs()
    
    # Test canceling the job
    test_cancel_job(job_id)
    
    # Wait a moment
    time.sleep(1)
    
    # Test getting the canceled job
    test_get_job(job_id)
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    main()
