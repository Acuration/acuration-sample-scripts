from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()


from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
all_splits = text_splitter.split_documents(data)


from langchain.embeddings import (
    GPT4AllEmbeddings,
    OllamaEmbeddings,  # We can also try Ollama embeddings
)
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

question = "How can Task Decomposition be done?"
docs = vectorstore.similarity_search(question)

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

llm = Ollama(
    model="mistral:7b-instruct",
    verbose=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)


from langchain import hub

QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-mistral")

# QA chain
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
)

question = "What are the various approaches to Task Decomposition for AI Agents?"
result = qa_chain({"query": question})
print(result)
