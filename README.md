# 🔐 Azure Misconfiguration Scanner (v2)

An open-source security tool designed to detect misconfigurations in Azure environments. This version reflects a full rebuild aligned with a structured 90-day Azure security learning journey.

---

## 📅 Progress Overview (Day 1–14 Completed)

| Day | Task Summary | Status |
|-----|--------------|--------|
| 1   | Project repo setup & secure Git branching | ✅ |
| 2   | Azure CLI login, account/subscription setup | ✅ |
| 3   | Scripting practice with `aws` and `az` CLI | ✅ |
| 4   | Azure environment setup with Key Vault & Storage | ✅ |
| 5   | Role-based access setup for users and groups | ✅ |
| 6   | Built custom Bicep template for secure Key Vault | ✅ |
| 7   | Enabled Key Vault diagnostic logs | ✅ |
| 8   | Deployed policy for public access to Key Vault | ✅ |
| 9   | Verified policy compliance and remediation | ✅ |
| 10  | Resource Group activity logs and diagnostic verification | ✅ |
| 11  | Security Center provisioning tailored for Free Tier | ✅ |
| 12  | Defender for Cloud configuration preview | ✅ |
| 13  | NSG rules port scan and exposure check | ✅ |
| 14  | IAM Role assignment data collection | ✅ |

---

## 🧪 Active Features (as of Day 14)

- 🔍 Key Vault exposure detection
- ⚠️ NSG rule scanner for ports `22` and `3389`
- 🔐 Role assignment exporter
- 🏛️ Azure Policy remediation validation
- 📊 Activity log collection to Log Analytics
- 🧱 Bicep-based IaC for secure provisioning

---

## 🧠 Learning-Focused Design

This project is part of a 90-day challenge focused on building **practical Azure security skills**. It documents:
- Misconfiguration detection
- Logging & monitoring
- Azure policy deployment
- CLI & scripting best practices
- Real-world remediation

---

## 📁 Project Structure

```
az-misconfig-scanner-v2/
│
├── data/                         # JSON exports for role assignments, NSGs, policies
├── policies/                     # JSON/Bicep for policy definitions
├── scripts/                      # Python scripts for scanner logic (coming soon)
├── diagnostics/                  # Diagnostic settings files
├── .github/                      # PR templates, issue templates (planned)
├── README.md                     # This file
└── ...
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/lee-jasaispace/azure-misconfig-scanner-v2.git
cd azure-misconfig-scanner-v2
az login
```

> ⚠️ Note: This tool is currently developed and tested using Azure Free Tier. Certain features (like Defender) may require a Pay-As-You-Go subscription to fully activate.

---

## 🧪 Coming Soon (Next Phases)

- 🔐 Privilege escalation checks
- 🚨 Built-in alert rules
- 📊 Power BI dashboard export
- 🧪 Additional misconfig rules for:
  - Storage
  - SQL Server
  - Kubernetes (AKS)
- 🧱 CI/CD Terraform integration

---

## 🛡️ License

MIT License

---

## 👩🏾‍💻 Built with 💙 by [@lee-jasaispace](https://github.com/lee-jasaispace)