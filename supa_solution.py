 

**Titre:** Lors de l'expédition d'une offre de bannissement, un flux de paiement est inversé. Le système ne tient pas compte de la gestion des contrats.

**Plateforme:** issuehunt | Valeur: $402 USD

**Description:**  
Il a été détecté un flux de paiement inversé dans le système actuel, ce qui entraîne une baisse de la valeur brute. Le système n'applique pas les contrôles de gestion des contrats nécessaires pour l'inscription au bannissement.

**Code de livraison:**  
```python
# Calcul du prix en dollars pour une offre de bannissement
def calculate_bounty_price():
    # Supposons que le prix est fixé à 402 USD pour l'offer
    return 402

# Déploiement du livrage
def deploy_bounty():
    # Création du contrat
    contract = Contract("PostBounty", "bounty", "usdc", "mcp")
    
    # Création du livre
    book = Book("MCP PostBounty", "bounty", "402 USD")
    
    # Création du contrat de bannissement
    lock = Lock("lock", "mcp", "402 USD")
    
    # Enregistrement du livre
    book.save(lock)
    
    #