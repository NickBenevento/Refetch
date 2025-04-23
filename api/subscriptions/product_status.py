from enum import Enum

class ProductStatus(Enum):
    IN_STOCK = "In stock"
    # maybe add something like 'limited stock' (i.e. "Only 2 left!")?
    OUT_OF_STOCK = "Out of stock"
    UNKNOWN = "Unknown" # Have not fetched yet / could not reach out
