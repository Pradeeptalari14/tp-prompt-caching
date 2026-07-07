## 🚀 Step-by-Step Onboarding & Validation Guide

Follow these SRE steps to deploy, validate, and monitor this repository's workspace configs in a local or production environment:

#### 1. Prerequisites
- [x] **Python 3.10+ or Node.js environment**
- [x] **Docker & Docker Compose**
- [x] **GitHub CLI (gh) & Git CLI**
- [x] **LLM Provider API Credentials (Anthropic Claude, OpenAI, or DeepSeek)**

#### 2. Download
Clone this repository locally:
```bash
git clone https://github.com/Pradeeptalari14/tp-prompt-caching.git
cd tp-prompt-caching
```

#### 3. Install
Fetch required packages and compile environment dependencies:
```bash
pip install -r requirements.txt || npm install
```

#### 4. Configure Environment Secrets
Copy the template configuration variables and fill in your API key credentials:
```bash
cp .env.example .env
# Edit .env and supply ANTHROPIC_API_KEY / OPENAI_API_KEY
```

#### 5. Build Local Infrastructure Proxy
Launch the local caching proxy using docker-compose sidecars to intercept and cache LLM prompts offline:
```bash
docker compose up -d
```

#### 6. Deploy Prompt Caching Pipeline
Run the prompt caching pilot application:
```bash
python primary_config/prompt_caching.py
```

#### 7. Validate Caching Policies Compliance
Execute local compliance validation scripts to check cache hit ratios and latency improvements:
```bash
bash scripts/validate.sh
```

#### 8. Verify Telemetry
Inspect logs to ensure cache hits and reads are tracked accurately:
```bash
docker compose logs proxy-cache | grep "HIT"
```
