def format_skus(sku_list):
    cleared_list = []
    for sku in sku_list:
        sku = sku.strip()
        if sku:
            clean_sku = sku.upper()
            cleared_list.append(clean_sku)
    return cleared_list        

raw_skus = [
    "  abc-123 ",
    "xyz-999",
    "   ",
    "promo-code",
    "item-A-500  "
]

# Run the function
print(format_skus(raw_skus))