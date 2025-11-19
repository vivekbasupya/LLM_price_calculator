# config/pricing.py
"""
Pricing configuration for LLM providers
Rates are per 1,000 tokens in USD (Input tokens pricing)
Note: For models with different input/output pricing, using input token pricing as baseline
Last updated: November 2025
"""

PRICING = {
    # ============================================
    # AZURE OPENAI - COMMERCIAL REGIONS
    # ============================================
    "Azure OpenAI": {
        "East US": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-35-turbo": 0.0005,
            "gpt-35-turbo-16k": 0.0010,
            "gpt-4": 0.03,
            "gpt-4-32k": 0.06,
            "text-embedding-ada-002": 0.0001,
            "text-embedding-3-small": 0.00002,
            "text-embedding-3-large": 0.00013
        },
        "East US 2": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-35-turbo": 0.0005,
            "gpt-35-turbo-16k": 0.0010,
            "gpt-4": 0.03,
            "text-embedding-ada-002": 0.0001
        },
        "West US": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-35-turbo": 0.0005,
            "gpt-4": 0.03,
            "text-embedding-ada-002": 0.0001
        },
        "West US 3": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-35-turbo": 0.0005
        },
        "Central US": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-35-turbo": 0.0005
        },
        "North Central US": {
            "gpt-4o": 0.0025,
            "gpt-35-turbo": 0.0005,
            "gpt-4": 0.03
        },
        "South Central US": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-35-turbo": 0.0005,
            "gpt-4": 0.03
        },
        "Canada East": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-35-turbo": 0.0005,
            "gpt-4": 0.03
        },
        "West Europe": {
            "gpt-4o": 0.0030,
            "gpt-4o-mini": 0.00018,
            "gpt-4-turbo": 0.012,
            "gpt-35-turbo": 0.0006,
            "gpt-35-turbo-16k": 0.0012,
            "gpt-4": 0.036,
            "gpt-4-32k": 0.072,
            "text-embedding-ada-002": 0.00012
        },
        "North Europe": {
            "gpt-4o": 0.0030,
            "gpt-4o-mini": 0.00018,
            "gpt-35-turbo": 0.0006,
            "gpt-4": 0.036
        },
        "Sweden Central": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-35-turbo": 0.0005,
            "gpt-4": 0.03
        },
        "Switzerland North": {
            "gpt-4o": 0.0030,
            "gpt-4o-mini": 0.00018,
            "gpt-35-turbo": 0.0006
        },
        "France Central": {
            "gpt-4o": 0.0030,
            "gpt-4o-mini": 0.00018,
            "gpt-35-turbo": 0.0006,
            "gpt-4": 0.036
        },
        "UK South": {
            "gpt-4o": 0.0030,
            "gpt-4o-mini": 0.00018,
            "gpt-35-turbo": 0.0006,
            "gpt-4": 0.036
        },
        "Australia East": {
            "gpt-4o": 0.0035,
            "gpt-4o-mini": 0.00021,
            "gpt-4-turbo": 0.014,
            "gpt-35-turbo": 0.0007,
            "gpt-4": 0.042,
            "text-embedding-ada-002": 0.00014
        },
        "Japan East": {
            "gpt-4o": 0.0035,
            "gpt-4o-mini": 0.00021,
            "gpt-35-turbo": 0.0007,
            "gpt-4": 0.042
        },
        "East Asia": {
            "gpt-4o": 0.0035,
            "gpt-35-turbo": 0.0007
        },
        "South India": {
            "gpt-4o": 0.0035,
            "gpt-4o-mini": 0.00021,
            "gpt-35-turbo": 0.0007,
            "gpt-4": 0.042
        }
    },
    
    # ============================================
    # AZURE GOVERNMENT (US GOV REGIONS)
    # ============================================
    "Azure Government": {
        "US Gov Virginia": {
            "gpt-4o": 0.00275,
            "gpt-4o-mini": 0.000165,
            "gpt-4-turbo": 0.011,
            "gpt-35-turbo": 0.00055,
            "gpt-35-turbo-16k": 0.0011,
            "gpt-4": 0.033,
            "gpt-4-32k": 0.066,
            "text-embedding-ada-002": 0.00011
        },
        "US Gov Arizona": {
            "gpt-4o": 0.00275,
            "gpt-4o-mini": 0.000165,
            "gpt-35-turbo": 0.00055,
            "gpt-4": 0.033,
            "text-embedding-ada-002": 0.00011
        },
        "US Gov Texas": {
            "gpt-4o": 0.00275,
            "gpt-35-turbo": 0.00055,
            "gpt-4": 0.033
        }
    },
    
    # ============================================
    # OPENAI DIRECT API
    # ============================================
    "OpenAI": {
        "Global": {
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "gpt-4-turbo": 0.01,
            "gpt-4": 0.03,
            "gpt-4-32k": 0.06,
            "gpt-3.5-turbo": 0.0005,
            "gpt-3.5-turbo-16k": 0.0010,
            "text-embedding-ada-002": 0.0001,
            "text-embedding-3-small": 0.00002,
            "text-embedding-3-large": 0.00013
        }
    },
    
    # ============================================
    # AWS BEDROCK
    # ============================================
    "AWS Bedrock": {
        "US East (N. Virginia)": {
            "claude-3-opus": 0.015,
            "claude-3-sonnet": 0.003,
            "claude-3-haiku": 0.00025,
            "claude-3.5-sonnet": 0.003,
            "claude-instant": 0.0008
        },
        "US West (Oregon)": {
            "claude-3-opus": 0.015,
            "claude-3-sonnet": 0.003,
            "claude-3-haiku": 0.00025,
            "claude-3.5-sonnet": 0.003
        },
        "EU (Frankfurt)": {
            "claude-3-opus": 0.018,
            "claude-3-sonnet": 0.0036,
            "claude-3-haiku": 0.0003,
            "claude-3.5-sonnet": 0.0036
        },
        "EU (London)": {
            "claude-3-opus": 0.018,
            "claude-3-sonnet": 0.0036,
            "claude-3-haiku": 0.0003
        },
        "Asia Pacific (Tokyo)": {
            "claude-3-opus": 0.018,
            "claude-3-sonnet": 0.0036,
            "claude-3-haiku": 0.0003,
            "claude-3.5-sonnet": 0.0036
        },
        "Asia Pacific (Singapore)": {
            "claude-3-opus": 0.018,
            "claude-3-sonnet": 0.0036,
            "claude-3-haiku": 0.0003
        }
    },
    
    # ============================================
    # GOOGLE CLOUD VERTEX AI
    # ============================================
    "Google Cloud": {
        "US Central": {
            "gemini-1.5-pro": 0.00125,
            "gemini-1.5-flash": 0.000075,
            "gemini-1.0-pro": 0.0005,
            "gemini-pro": 0.0005,
            "text-bison": 0.0005,
            "chat-bison": 0.0005
        },
        "US East": {
            "gemini-1.5-pro": 0.00125,
            "gemini-1.5-flash": 0.000075,
            "gemini-1.0-pro": 0.0005
        },
        "Europe West": {
            "gemini-1.5-pro": 0.0015,
            "gemini-1.5-flash": 0.00009,
            "gemini-1.0-pro": 0.0006,
            "gemini-pro": 0.0006
        },
        "Asia Southeast": {
            "gemini-1.5-pro": 0.0015,
            "gemini-1.5-flash": 0.00009,
            "gemini-1.0-pro": 0.0006
        }
    }
}


def get_providers():
    """Return list of available providers"""
    return list(PRICING.keys())


def get_regions(provider):
    """Return list of regions for a provider"""
    return list(PRICING.get(provider, {}).keys())


def get_models(provider, region):
    """Return list of models for a provider and region"""
    return list(PRICING.get(provider, {}).get(region, {}).keys())


def get_rate(provider, region, model):
    """Get the rate per 1K tokens for a specific configuration"""
    try:
        return PRICING[provider][region][model]
    except KeyError:
        return None


def get_model_info(provider, region, model):
    """
    Get detailed information about a model
    Returns: dict with rate and metadata
    """
    rate = get_rate(provider, region, model)
    if rate is None:
        return None
    
    return {
        'rate_per_1k': rate,
        'provider': provider,
        'region': region,
        'model': model
    }