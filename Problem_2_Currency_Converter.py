usd_to_yuan_rate = 6.91  # Exchange rate as of 5 march 2023

def usd_to_yuan(usd):
    yuan = usd * usd_to_yuan_rate
    return yuan

def yuan_to_usd(yuan):
    usd = yuan / usd_to_yuan_rate
    return usd

print("Conversion rate as of March 2023: 1 USD = 6.91 Yuan\n")

# USD to Yuan
print("USD to Yuan:")
print("1 USD =", usd_to_yuan(1), "Yuan")
print("1500 USD =", usd_to_yuan(1500), "Yuan")
print("25000 USD =", usd_to_yuan(25000), "Yuan")

# Yuan to USD
print("\nYuan to USD:")
print("1 Yuan =", yuan_to_usd(1), "USD")
print("1750 Yuan =", yuan_to_usd(1750), "USD")
print("28000 Yuan =", yuan_to_usd(28000), "USD")