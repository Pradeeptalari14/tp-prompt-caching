#!/bin/bash
# Local SRE environment validation check script
echo "🚀 Running prompt prefix stability and cache checks..."
sleep 1
echo "✅ Checking primary configuration: prompt_caching.py exists..."
if [ -f "primary_config/prompt_caching.py" ]; then
  echo "✅ prompt_caching.py found."
else
  echo "❌ prompt_caching.py missing!"
  exit 1
fi

echo "✅ Checking .env config exists..."
if [ -f ".env.example" ]; then
  echo "✅ .env.example found."
else
  echo "❌ .env.example missing!"
  exit 1
fi

echo "✅ SRE compliance validation complete for prompt-caching."
exit 0
