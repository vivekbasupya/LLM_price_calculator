# config/pricing.py
"""
Pricing configuration for LLM providers.

Rates are expressed in USD per 1,000,000 tokens to align with the Azure OpenAI
catalog (November 2025). Each model entry stores separate price points for
standard input tokens, generated output tokens, and cached prompt tokens.
"""

PRICING = {

    # AZURE OPENAI - COMMERCIAL REGIONS

    "Azure OpenAI": {
        "East US": {
            "gpt-4o": {
                "input_per_million": 2.50,
                "output_per_million": 10.00,
                "cached_per_million": 1.25
            },
            "gpt-4o-mini": {
                "input_per_million": 0.15,
                "output_per_million": 0.60,
                "cached_per_million": 0.075
            },
            "gpt-4-turbo": {
                "input_per_million": 10.00,
                "output_per_million": 30.00,
                "cached_per_million": 5.00
            },
           
        }
    },

    # AZURE GOVERNMENT (US GOV REGIONS)

    "Azure Government": {
        "US Gov Virginia": {
            "gpt-4o": {
                "input_per_million": 2.75,
                "output_per_million": 11.00,
                "cached_per_million": 1.375
            },
            "gpt-4o-mini": {
                "input_per_million": 0.165,
                "output_per_million": 0.66,
                "cached_per_million": 0.0825
            },
            "gpt-4-turbo": {
                "input_per_million": 11.00,
                "output_per_million": 33.00,
                "cached_per_million": 5.50
            }
        }
    }
}


def get_providers():
    """Return list of available providers."""
    return list(PRICING.keys())


def get_regions(provider):
    """Return list of regions for a given provider."""
    return list(PRICING.get(provider, {}).keys())


def get_models(provider, region):
    """Return list of models for a provider and region."""
    return list(PRICING.get(provider, {}).get(region, {}).keys())


def get_model_pricing(provider, region, model):
    """Return the pricing dict for a provider/region/model combination."""
    try:
        return PRICING[provider][region][model]
    except KeyError:
        return None


def get_rate(provider, region, model, rate_key="input_per_million"):
    """
    Convenience helper to fetch a specific rate (input/output/cached).
    Defaults to the input cost per million tokens.
    """
    pricing = get_model_pricing(provider, region, model)
    if pricing is None:
        return None
    return pricing.get(rate_key)


def get_model_info(provider, region, model):
    """
    Get detailed information about a model.
    Returns: dict with rates and metadata.
    """
    pricing = get_model_pricing(provider, region, model)
    if pricing is None:
        return None
    
    return {
        'provider': provider,
        'region': region,
        'model': model,
        'pricing': pricing
    }