import logging

# Default level of root logger is Warning, therefore need to set a level for it
logger = logging.getLogger('Marketplace service')
logger.setLevel(logging.DEBUG)
console_hdlr = logging.StreamHandler()
console_hdlr.setLevel(logging.INFO)
console_hdlr.setFormatter(logging.Formatter("%(asctime)s: %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_hdlr)
