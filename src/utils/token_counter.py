import re
import tiktoken
from transformers import AutoTokenizer

def count_tokens(text, model="simple"):
    """
    Count tokens in text based on the specified model.
    
    Args:
        text (str): The text to tokenize
        model (str): The tokenization model to use:
            - "simple": Simple whitespace splitting
            - "gpt-3.5-turbo": GPT-3.5 tokenization
            - "gpt-4": GPT-4 tokenization
            - "claude": Claude-style tokenization
            - "llama": LLaMA tokenization
    
    Returns:
        int: The number of tokens
    """
    if not text:
        return 0
        
    if model == "simple":
        # Simple whitespace tokenization
        tokens = text.split()
        return len(tokens)
    
    elif model in ["gpt-3.5-turbo", "gpt-4"]:
        # Use tiktoken for OpenAI models
        try:
            enc = tiktoken.encoding_for_model(model)
            tokens = enc.encode(text)
            return len(tokens)
        except Exception:
            # Fallback to cl100k_base encoding
            enc = tiktoken.get_encoding("cl100k_base")
            tokens = enc.encode(text)
            return len(tokens)
    
    elif model == "claude":
        # Approximate Claude tokenization (character-based)
        # This is an approximation as Claude's exact tokenizer isn't public
        return len(text) // 4  # Approximate 4 characters per token
    
    elif model == "llama":
        # Use HuggingFace tokenizer for LLaMA
        try:
            tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
            tokens = tokenizer.encode(text)
            return len(tokens)
        except Exception:
            # Fallback to simple tokenization if HF model isn't available
            tokens = text.split()
            return len(tokens)
    
    else:
        # Default to simple tokenization
        tokens = text.split()
        return len(tokens)