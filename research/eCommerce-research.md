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
    - Collaborative filtering 
    - Content-based 
    - Knowledge-based
-   Point 2

