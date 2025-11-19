# utils/token_estimator.py
"""
Estimate token counts from text
"""


class TokenEstimator:
    """Simple token estimation based on word count"""
    
    # Average tokens per word ratio for most LLMs
    TOKENS_PER_WORD = 1.33
    
    @staticmethod
    def estimate(text=None, word_count=None):
        """
        Estimate tokens from text or word count
        Args:
            text: String of text to estimate
            word_count: Pre-calculated word count
        Returns: estimated token count (integer)
        """
        if text:
            word_count = len(text.split())
        elif word_count is None:
            return 0
        
        return int(word_count * TokenEstimator.TOKENS_PER_WORD)
    
    @staticmethod
    def estimate_from_stats(stats):
        """
        Estimate tokens from text statistics dict
        Args:
            stats: dict with 'word_count' key
        Returns: estimated token count
        """
        return TokenEstimator.estimate(word_count=stats.get('word_count', 0))