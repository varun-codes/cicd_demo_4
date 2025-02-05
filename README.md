# AI Hub Apps CI/CD Workflows

This repository contains CI/CD workflows for deploying AI Hub applications across different environments.

## Setup Instructions

### 1. Prerequisites
Before you begin, ensure you have the following:
- Access to both source and target Instabase environments (admin tokens required).
- Access to the `.whl` file in the Instabase public repository `aihub-apps-ci-cd-workflows` or a `.whl` file available in your own repository.

### 2. GitHub Secrets Configuration
The following secrets need to be configured in your GitHub repository:

- `SOURCE_HOST_URL`: The URL of the source environment.
- `SOURCE_TOKEN`: The authentication token for the source environment.
- `TARGET_HOST_URL`: The URL of the target environment.
- `TARGET_TOKEN`: The authentication token for the target environment.

### 3. Configuration File Setup
1. Create a `config.json` file in your repository with the following structure:
```
{
  "source": {
    "is_advanced": true, // set to true if it is an advanced app
    "project_id": "", 
    "flow_path": "", 
    "sb_name": "<Your_Solution_Builder_Name>", 
    "flow_name": "<Your_Flow_Name>", 
    "org": "<Source_Organization>", 
    "workspace": "<Source_Workspace>", 
    "app_id": "<Your_App_ID>", 
    "deployment_id": "<Your_Deployment_ID>", 
    "dependencies": ["<dependency1>==<version>"] 
  },
  "target": {
    "org": "<Target_Organization>", 
    "workspace": "<Target_Workspace>" 
  },
  "settings": {
    "rebuild": false // set to true if you want to rebuild the project
  },
  "testing": {
    "regression": {} // specify regression testing details if needed
  },
  "release_notes": "<Your_Release_Notes>" 
}
```

### 4. Usage
1. Update the configuration file with your project details
2. Commit and push the changes to your feature branch
3. The CI/CD workflow will automatically fetch the project details from the source environment.
4. Merge the feature branch to main to trigger the migration to target environment.



### Sample Config File
```
{
    "source": {
        "is_advanced" : true,
        "host_url": "https://ci-cd-test-1.internal.instabase.com", 
        "token": "v3b43OQ1uzLPD0Y2KASjaOdz0PZuEG",  
        "project_id": "", 
        "flow_path": "",
        "sb_name": "DL_App",
        "flow_name": "DL_Flow",
        "org": "SolEng",
        "workspace": "CI-CD",
        "app_id": "a56eb7e0-657d-497d-8c32-0c41d6314554",
        "deployment_id": "0194a7fa-7474-7a0b-9b88-78f82c0684c6",
        "dependencies": ["model_DL_ca58a1844ac048a297157de827858c6b==0.0.8"]
    },
    "target": {
        "host_url": "https://ci-cd-test-2.internal.instabase.com",   
        "token": "MPf5vjf4ZziLK1HE7Xq8ejERNTCREf",   
        "org": "SolEng",
        "workspace": "CI-CD"              
    },
    "settings": {
        "rebuild": false
    },
    "testing": {
        "regression": {}
    },
    "release_notes": "initial release"
}
```