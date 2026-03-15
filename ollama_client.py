#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

class OllamaModelClient:
    def __init__(self, model, base_url="http://localhost:11434", **kwargs):
        self.model = model
        self.base_url = base_url
        self.model_info = kwargs.get("model_info", {})
    
    def generate(self, messages, **kwargs):
        """生成响应"""
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": kwargs.get("temperature", 0.7),
                "max_tokens": kwargs.get("max_tokens", 2048),
                "top_p": kwargs.get("top_p", 0.9)
            }
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        
        return {
            "content": result.get("message", {}).get("content", ""),
            "role": result.get("message", {}).get("role", "assistant")
        }
    
    def generate_stream(self, messages, **kwargs):
        """流式生成响应"""
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": kwargs.get("temperature", 0.7),
                "max_tokens": kwargs.get("max_tokens", 2048),
                "top_p": kwargs.get("top_p", 0.9)
            }
        }
        
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                if "message" in data:
                    yield {
                        "content": data["message"].get("content", ""),
                        "role": data["message"].get("role", "assistant")
                    }
