import interfaces.sku
import interfaces.supplier

# Register each interface with the Transformer class
from transformer import Transformer
Transformer.register_interface(interfaces.sku.Impl.name, interfaces.sku.Impl().transform)
Transformer.register_interface(interfaces.supplier.Impl.name, interfaces.supplier.Impl().transform)
