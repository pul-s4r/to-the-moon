# Stock Portfolio Research

## Options - API

-   [Shopify](https://shopify.dev/docs/storefront-api/reference)
    - Full-service choice, supports many of the storefront-side features required in the spec e.g. customer info, stores, products and orders/transactions
    - There are also [admin-side commands](https://shopify.dev/docs/admin-api) for building basic processes like inventory management
    - Could be emulated if the backend needs to be built from scratch
-   [Algolia](https://www.algolia.com/doc/)
    - General search service - we need to implement the store backend then send product queries over this service
    - Flexible - can index other content e.g. blog posts, FAQs. Might be useful for the recommender but would also encroach on features to implement ourselves
    - Native integrations with Shopify
-   [Axesso](http://api-doc.axesso.de/)
    - Product search service - has integrations with Alibaba, Amazon, TripAdvisor, Walmart
    - This looks like a simplified wrapper to the above platforms, most implement their own API if we need to develop something that orchestrates and ties them together. 

## Useful Links

-   [List - RapidAPI](https://rapidapi.com/collection/essential-ecommerce-apis). 
-   [List - ProgrammableWeb](https://www.programmableweb.com/news/71-ecommerce-apis-seatwave-playme-and-ebay/2012/06/06). 

## Remarks

-   Recommendation techniques 
    - Collaborative filtering ([example](https://realpython.com/build-recommendation-engine-collaborative-filtering/))
        - Suggests results based on historical interactions (e.g. ratings); input is typically a user-item matrix with vectors representing interaction scores
        - Does not require features about items to be known, suitable for recommending new items outside of existing preferences based on activity of other users, though it does not necessarily discriminate between desirable and undesirable items
        - Only recommends frequently interacted items, does not recommend new items with little activity (cold start problem), poor performance on sparse data
        - Limited scalability 
    - Content-based ([example](https://heartbeat.fritz.ai/recommender-systems-with-python-part-i-content-based-filtering-5df4940bd831))
        - Suggests results based on item properties (e.g. name, purpose, target audience/demographic, features); input is typically labels to search the item properties, some definition of structure may be required e.g. word vectors
        - Can be some combination of exploitative (results similar to user preference) or explorative (outside of user preference) 
        - Results independent of user interaction, suitable for recommending items similar to user preferences. Avoids cold start problem
        - Requires significant differentiation between item properties to produce a good result
        - Overspecialisation - will recommend similar items only
    - Knowledge-based ([example](https://towardsdatascience.com/recommendation-system-in-python-lightfm-61c85010ce17))
        - Suggests results with explicit user requirements, defines additional rules for correlation between item features and user requirements
        - Example rules: case based reasoning (recommends items most similar to the use case described by the user's profile)
        - Best suited to making precise, high-information predictions or where complex domain knowledge is required e.g. buying property. Avoids cold start problem problem. 
        - Knowledge acquisition bottleneck: correlation to result criteria needs to be explicitly defined. 
- More complex techniques
    - Hybridisation techniques: weighted, mixed, switching, feature combination, feature augmentation, cascade and meta-level
    - Example: use content filtering to work on the initial set of items, then incorporate collaborative or explorative strategies when enough data on user preference and interaction is collected.
    - AI/compute-driven techniques: Bayesian inference, neural networks, genetic algorithms, fuzzy logic
-  

