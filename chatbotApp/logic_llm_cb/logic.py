from langchain_community.embeddings import HuggingFaceEmbeddings 
import chroma

def answer_query(query):
  model_name = "sentence-transformers/all-mpnet-base-v2"
  model_kwargs = {"device": "cpu"}
  embeddings = HuggingFaceEmbeddings(
    model_name=model_name, 
    model_kwargs=model_kwargs
  )
  # db = Chroma(
  #   collection_name="web_docs", 
  #   embedding_function=embeddings, 
  #   persist_directory=CHROMA_DB_DIRECTORY
  # )
  # llm = LlamaCpp(
  #   model_path="djangoapp/models/llama-2-7b-chat.Q4_0.gguf",
  #   n_gpu_layers=40,
  #   n_batch=512,   # Batch size for model processing
  #   n_ctx=2048,    # Context size
  #   verbose=False, # enable detailed logging or not
  # )

  # chain = RetrievalQAWithSourcesChain.from_chain_type(
  #   llm=llm,
  #   chain_type="stuff",
  #   retriever=db.as_retriever(),
  #   chain_type_kwargs={"prompt": prompt}
  # )