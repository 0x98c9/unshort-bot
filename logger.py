import logging

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("unshortener.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
