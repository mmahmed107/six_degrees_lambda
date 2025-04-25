# Six Degrees of Kevin Bacon – Lambda Function

Inspired by the "Six Degrees of Kevin Bacon" concept — the idea that any actor can be linked to Kevin Bacon through six or fewer connections — this project simulates a similar exploration through Wikipedia. Starting from a single article, it follows random internal links to discover a 6-step path across the site.

---

## How It Works

- Starts from a provided Wikipedia path (e.g. `/wiki/Six_Degrees_of_Kevin_Bacon`)
- Randomly selects and follows 6 internal Wikipedia links
- Returns the full list of visited URLs as output

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run tests

```bash
pytest tests/
```

---

## Deploying with Terraform

> Make sure your AWS CLI is configured before running the following:

```bash
cd iac
terraform init
terraform apply -var-file=config/dev.tfvars
```

This will package and deploy the Lambda function, set up IAM roles, and configure logging.

---

## Continuous Integration (CI)

GitHub Actions automatically runs the following on every push:
- Python tests
- Security scan 
- Terraform validation

---
