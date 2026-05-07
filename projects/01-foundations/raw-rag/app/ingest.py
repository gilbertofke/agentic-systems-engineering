"""
Raw rag ingestion pipeline

Responsibilities:
1. Load raw documents
2. Chunk the text
3. Generate embeddings
4. Store in FAISS
5. Persist the FAISS index and the chunk metadata
"""

#Imports


#Step 1: Load Raw Documents

def load_document():
   #Open the knowledge base document
   with open("data/knowledge.txt","r") as file:
    raw_text=file.read()
    
    #Return raw document text as a python string
    return raw_text


#Step 2: Split text into chunks
def chunk_text(raw_text,chunk_size=300,overlap=50):
    chunks=[]
    #Split the text into fixed-sized chunks
    for i in range(0,len(raw_text),chunk_size-overlap):
        chunk=raw_text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks




#Step 3:Generate embeddings from the chunks
def generate_embeddings(chunks):
    #Load embedding model
    #Convert text chunks into embedding vectors
    #Ensure each chunk maps correctly to its embedding
    #Return embeddings
    pass

#Step 4: Build FAISS Index
def build_faiss_index(embeddings):
    #Determine embedding dimension
    #Create FAISS structure
    #Add embeddings into the index
    #Return searchable FAISS index
    pass

#Step 5: Save metadata sidecar
def save_metadata():
    #Create metadata records for each chunk
    #Assign stable identifiers to chunks
    #Preseve chunk order relationships
    #Save metadata to JSON file
    pass

#Step 6: Persist FAISS index
def save_faiss_index():
    #Serialize FAISS index structure
    #Save index file to disk
    #Ensure retrieval system can reload index later
    pass

#Main Orchestration flow
def main():
# Execute ingestion pipeline
    raw_text=load_document()
    chunks=chunk_text(raw_text)

    for index,chunk in enumerate(chunks):
        print(f"\n--- Chunk{index +1} ---")
    
        print(chunk)
    print(type(chunks))
    print(len(chunks))


if __name__=="__main__":
    main()