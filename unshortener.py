import httpx
from config import REQUEST_TIMEOUT
from logger import logger

async def unshorten_url(url: str) -> str:
    """Resolve shortened URL to its original form"""
    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.head(url, follow_redirects=True)
            final_url = str(response.url)
        
        logger.info(f"Unshortened: {url} → {final_url}")
        return final_url
    except httpx.TimeoutException:
        return "⌛ Request timed out. Try again later."
    except httpx.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
        return "❌ Could not resolve URL. Check if it's valid."
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return "🔧 An unexpected error occurred. Please try again."
