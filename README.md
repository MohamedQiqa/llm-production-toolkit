<div align="center">

# LLM Deployment Toolkit

[![AWS SageMaker](https://img.shields.io/badge/AWS-SageMaker-FF9900?logo=amazonsagemaker&logoColor=white)](sagemaker/instructions.md)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-232F3E?logo=amazonaws&logoColor=white)](bedrock/instructions.md)
[![Modal](https://img.shields.io/badge/Modal-Serverless_GPU-6C3AED?logo=modal&logoColor=white)](modal/instructions.md)
[![Runpod](https://img.shields.io/badge/Runpod-Serverless-673DE6?logo=runpod&logoColor=white)](runpod/instructions.md)

</div>


Deploy fine-tuned LLMs or any LLM model available on Hugging Face to production across multiple cloud platforms. This repo provides ready-to-use server code, client scripts, and step-by-step deployment guides for each platform — so you can go from a trained model to a live endpoint in minutes.

---

## Supported Platforms

| Platform | Type | What You Get |
|----------|------|-------------|
| **[Modal](modal/instructions.md)** | Serverless GPU | vLLM server with LoRA support, streaming, OpenAI-compatible API |
| **[Runpod](runpod/instructions.md)** | Serverless GPU | vLLM endpoint with OpenAI SDK client |
| **[SageMaker](sagemaker/instructions.md)** | Managed Endpoint | vLLM on AWS with IAM, VPC, and auto-scaling |
| **[Bedrock](bedrock/instructions.md)** | Fully Managed | Custom model import, zero infrastructure |

Each platform folder contains an **`instructions.md`** with full deployment steps, screenshots, and example commands.

---

## Additional Resources

| Folder | Description |
|--------|------------|
| [`aws-setup/`](aws-setup/) | IAM roles, policies, and trust configurations for Bedrock & SageMaker |
| [`aws-services/`](aws-services/) | Bedrock batch inference, evaluation, SageMaker training — using AWS managed services directly (no vLLM) |

---

## Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd <repo-name>
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 2. Configure Environment

Copy the template and fill in your credentials:

```bash
cp .env.example .env
```

### 3. Pick a Platform & Deploy

Each platform has its own `instructions.md` — follow the one that fits your use case:

- **Serverless (easiest):** Start with [Modal](modal/instructions.md) or [Runpod](runpod/instructions.md)
- **AWS Managed:** Use [SageMaker](sagemaker/instructions.md) or [Bedrock](bedrock/instructions.md)
- **AWS IAM Setup:** If new to AWS, start with [aws-setup/](aws-setup/) first

---

## Platform Comparison

| Platform | Scaling | Complexity | Cost Model | Cold Starts |
|----------|---------|------------|------------|-------------|
| **Modal** | Automatic | Low | Per-second GPU | Optimizable |
| **Runpod** | Automatic | Medium | Per-second GPU | Configurable |
| **SageMaker** | Policy-based | Medium-High | Per-hour instance | Warm pools |
| **Bedrock** | Automatic | Low | Per-token | None |

---

## Project Structure

```
├── modal/              # vLLM on Modal (serverless GPU)
│   ├── server.py
│   ├── openai_server.py
│   ├── client.py
│   ├── client_openai.py
│   └── instructions.md
├── runpod/             # vLLM on Runpod (serverless GPU)
│   ├── client_openai.py
│   └── instructions.md
├── sagemaker/          # vLLM on AWS SageMaker
│   ├── client.py
│   └── instructions.md
├── bedrock/            # Custom model on AWS Bedrock
│   ├── bedrock_client.py
│   └── instructions.md
├── aws-setup/          # IAM roles & policies
│   ├── bedrock/
│   └── sagemaker/
├── aws-services/       # AWS managed inference & training
│   ├── bedrock_inference_single.py
│   ├── bedrock_inference_batch.py
│   ├── bedrock_evaluate_batch.py
│   ├── prepare_bedrock_data.py
│   ├── deploy-llm-sagemaker.ipynb
│   └── config.yaml
├── .env.example
├── requirements.txt
└── README.md
```

---

## Hardware Notes

- **Modal L4**: 24GB VRAM — good for 1–7B parameter models
- **SageMaker ml.g6.2xlarge**: L4 GPU, CUDA 12.x compatible

> ⚠️ **CUDA Compatibility**: The vLLM container (`cu129`) requires CUDA 12.x. Use `ml.g6.*` instances on SageMaker. `ml.g5.*` instances run CUDA 11.4 and will fail.

---

## License

This project is licensed under the [MIT License](LICENSE).
