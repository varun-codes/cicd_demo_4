# CI/CD Usage Documentation

## Overview
The CI/CD workflows streamline the deployment of AI Hub applications across different environments. This automation facilitates the migration of applications from a source environment to a target environment using GitHub Actions.

---

## Setup Instructions

### 1. Prerequisites
Before you begin, ensure you have the following:

- Tokens for both the source and target Instabase environments with the following access:
  - `manage_aihub` (Site permission / Manage AI Hub)
  - `manage_marketplace_apps` (App permission / Marketplace Admin)
  - `write_fs_aihub` (Site permission / Write Any Files to AI Hub Filesystem)
- Access to the Instabase public repository `aihub-apps-ci-cd-workflows`.
  - If you have access, you can clone the repository directly.
  - If you do not have access, you need to manually add the workflows and `.whl` files to your repository. You can obtain these files by raising a Zendesk ticket.

### 2. Setting Up Your Repository
1. Create a new repository in your GitHub organization.
2. If you have access to the Instabase public repository:
   - Clone or download the repository (`aihub-apps-ci-cd-workflows`) locally.
   - Copy the workflow `.yml` files to your new repository.
   - Commit and push these files to the `main` branch of your repository.
3. If you do not have access to the Instabase public repository:
   - Obtain the `.whl` file and workflow `.yml` files by raising a Zendesk ticket.
   - Add these files to your new repository.
   - Commit and push these files to the `main` branch of your repository.

### 3. GitHub Secrets Configuration
To enable the CI/CD workflow, configure the following secrets in your GitHub repository’s **Actions and Secrets** tab:

| Secret Name       | Description                                   |
|-------------------|-----------------------------------------------|
| `SOURCE_HOST_URL` | The URL of the source Instabase environment. |
| `SOURCE_TOKEN`    | The authentication token for the source.     |
| `TARGET_HOST_URL` | The URL of the target Instabase environment. |
| `TARGET_TOKEN`    | The authentication token for the target.     |

### 4. Configuration File Setup
1. Create a feature branch with a name starting as `feature/*` (required).
2. Add a `config.json` file in your feature branch with the following structure:

```json
{
  "source": {
    "is_advanced": true/false, 
    "project_id": "<Build Project ID>",
    "flow_path": "<Advanced App Flow Path>",
    "sb_name": "<Solution Builder Name>",
    "flow_name": "<Solution Build Flow Name>",
    "org": "<Source Organization>",
    "workspace": "<Source Workspace>",
    "app_id": "<App ID>",
    "deployment_id": "<Deployment ID>",
    "dependencies": ["<dependency1>==<version>", "..."]
  },
  "target": {
    "org": "<Target Organization>",
    "workspace": "<Target Workspace>",
    "project_id": "<Target Project ID>"
  },
  "settings": {
    "rebuild": true/false
  },
  "testing": {
    "regression": {}
  },
  "release_notes": "<Release Notes>"
}
```

#### Explanation of Configuration Parameters:
##### Build App:
- `is_advanced: false`
- `project_id`: required
- `project_id(target)`: If the build project already exists in the target and you want to make changes in the same project

##### Advanced App:
- `is_advanced: true`
- `flow_path`: required
- `dependencies`: if applicable

##### Solution Build App:
- `is_advanced: true`
- `sb_name`: required
- `flow_name`: required
- `dependencies`: if applicable

##### Common to All:
- `app_id`: required (when migrating the app)
- `deployment_id`: optional
- `org`: required
- `workspace`: required

##### Settings:
- `rebuild: true` (if you want the project to be recreated in the target environment along with the app migration, only applicable for Build App)
- `regression`: not available currently

##### Release Notes:
- Notes of your change in the app (required)

---

## Instructions to Trigger the Workflows

### 1. Ensure Workflow Permissions
Make sure you have workflow permissions set in the repository’s settings.

### 2. Update the Configuration File
Modify the `config.json` file with your project details.

### 3. Commit and Push Changes
1. Commit the updated `config.json` file to your feature branch.
2. Push it to the remote repository.

### 4. Trigger CI/CD Workflow
- The CI/CD workflow will automatically fetch the project details from the source environment and commit the project data to the feature branch.
- Continue working on your project, and when you want to fetch the latest project data, update the config file (e.g., updating release notes for app changes).
- Commit again to trigger the CI/CD workflow, ensuring that the latest project details are fetched into the feature branch.
- Follow Git best practices such as pulling before committing, resolving merge conflicts, etc.

### 5. Migrate to Target Environment
1. Once your app is ready for migration, merge the feature branch into the `main` branch by creating a pull request (PR).
2. Upon merging the PR, the CI/CD workflow will be triggered, and the app will be migrated to the target environment.

⚠️ **Important:** The app will be migrated to the target environment based on the details in the feature branch, not the source environment. So, ensure the feature branch contains the latest project details before migration.

---

## Sample Configuration File
```json
{
    "source": {
        "is_advanced": true,
        "project_id": "a56eb7e0-657d-497d-8c32-0c41d6314554",
        "flow_path": "SolEng/CI-CD/fs/Instabase Drive/AdvancedApp.ibflow",
        "sb_name": "DL_App",
        "flow_name": "DL_Flow",
        "org": "SolEng",
        "workspace": "CI-CD",
        "app_id": "a56eb7e0-657d-497d-8c32-0c41d6314554",
        "deployment_id": "0194a7fa-7474-7a0b-9b88-78f82c0684c6",
        "dependencies": ["model_DL_ca58a1844ac048a297157de827858c6b==0.0.8"]
    },
    "target": {
        "org": "SolEng",
        "workspace": "CI-CD",
        "project_id": "a56eb7e0-657d-497d-8c32-0c41d6314554"
    },
    "settings": {
        "rebuild": false
    },
    "testing": {
        "regression": {}
    },
    "release_notes": "Initial release v0.0.1 - changed some prompts"
}
```

---

## FAQs
### How can I retrieve the workflows and `.whl` files if I don't have access to the Instabase repository?
Raise a Zendesk ticket to obtain the workflows and `.whl` file from Instabase.

### What should we do if we want to migrate multiple apps?
Each app should have its own separate repository since the `main` branch always contains the latest data for one app.
