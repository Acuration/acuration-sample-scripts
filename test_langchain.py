from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

llm = Ollama(
    model="mistral", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

llm("Tell me about the history of AI")


