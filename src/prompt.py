prompt_template="""
    use the following piece of information to answer the user's question.
    if you are not aware of it, just say you are not aware of it, don't try to make up an answer.
    Context:{context}
    Question:{question}
    
    only return the helpful answer.
    Helpful answer:"""