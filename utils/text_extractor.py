# utils/text_extractor.py
"""
Extract text from various document formats
"""
import PyPDF2
import docx
from pathlib import Path


class TextExtractor:
    """Extract text from PDF, DOCX, and TXT files"""
    
    @staticmethod
    def extract(file_path):
        """
        Extract text from a file based on its extension
        Returns: extracted text as string
        """
        path = Path(file_path)
        extension = path.suffix.lower()
        
        extractors = {
            '.pdf': TextExtractor._extract_pdf,
            '.txt': TextExtractor._extract_txt,
            '.docx': TextExtractor._extract_docx
        }
        
        extractor = extractors.get(extension)
        if not extractor:
            raise ValueError(f"Unsupported file format: {extension}")
        
        return extractor(file_path)
    
    @staticmethod
    def _extract_pdf(file_path):
        """Extract text from PDF"""
        text = []
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text.append(page.extract_text())
        return '\n'.join(text)
    
    @staticmethod
    def _extract_txt(file_path):
        """Extract text from TXT"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    @staticmethod
    def _extract_docx(file_path):
        """Extract text from DOCX"""
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    
    @staticmethod
    def get_stats(text):
        """
        Get text statistics
        Returns: dict with character_count, word_count
        """
        return {
            'character_count': len(text),
            'word_count': len(text.split())
        }