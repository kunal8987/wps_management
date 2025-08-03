from .models import SKU, MSKU
from django.core.exceptions import ValidationError


def clean_and_map_skus(sku_data):
    # Initialize an empty list to store cleaned SKU data
    cleaned_data = []

    # Iterate over each item in the input sku_data list
    for item in sku_data:
        # Extract the SKU code from the item dictionary
        sku_code = item.get("sku_code")
        # Extract the SKU name from the item dictionary
        sku_name = item.get("name")

        # If either sku_code or sku_name is missing, raise a validation error
        if not sku_code or not sku_name:
            raise ValidationError(f"Invalid SKU data: {item}")

        # Get or create a SKU object with the given sku_code and name
        sku, created = SKU.objects.get_or_create(
            sku_code=sku_code, defaults={"name": sku_name}
        )

        # Find the first MSKU object that is related to the SKU
        ms = MSKU.objects.filter(skus=sku).first()
        if ms:
            # If an MSKU is found, append its details to cleaned_data
            cleaned_data.append(
                {
                    "sku_code": sku.sku_code,
                    "sku_name": sku.name,
                    "msku_code": ms.master_sku_code,
                }
            )
        else:
            # If no MSKU is found, append the SKU details with msku_code as None
            cleaned_data.append(
                {
                    "sku_code": sku.sku_code,
                    "sku_name": sku.name,
                    "msku_code": None,
                }
            )

    # Return the list of cleaned and mapped SKU data
    return cleaned_data
