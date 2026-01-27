# Company-Internal-Chatbot-with-Role-Based-Access-Control-RBAC---Group-1
## Milestone 1 and Milestone 2 Summary

**Milestone 1** builds the foundation of the system. Company documents from different departments are loaded, metadata is added, and large documents are split into smaller chunks. These chunks are converted into numerical embeddings using a sentence transformer model and stored in a Chroma vector database. This makes all documents searchable using semantic similarity.

**Milestone 2** adds security using Role-Based Access Control (RBAC). When a user enters a role and a query, the system first performs semantic search on the vector database and then filters the results using the `allowed_roles` metadata. Only documents that match the user’s role are returned, ensuring users can access only the data they are authorized to view.