#!/usr/bin/env python3
# Programmatic Prompt Caching SDK wrapper for Anthropic Claude
import anthropic
import os

def query_caching_copilot(user_query, context_docs=None):
    # Initialize Anthropic client with Ephemeral Caching (Beta)
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    system_prompt = (
        "You are an SRE Platform Copilot. "
        "Review logs and runbooks to suggest mitigation actions."
    )
    
    system_blocks = [
        {
            "type": "text",
            "text": system_prompt,
            "cache_control": {"type": "ephemeral"}  # Stable prefix cached
        }
    ]
    
    if context_docs:
        system_blocks.append({
            "type": "text",
            "text": f"\n[CONTEXT]\n{context_docs}",
            "cache_control": {"type": "ephemeral"}  # RAG context cached
        })
        
    response = client.beta.prompt_caching.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=system_blocks,
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    
    # Print cache hits telemetry metrics
    input_tok = response.usage.input_tokens
    cached_tok = response.usage.cache_read_input_tokens
    print(f"[METRIC] Input Tokens: {input_tok} (Cache Read: {cached_tok})")
    
    return response.content[0].text
