
<div align="center" style="color: black;">
  <span ><strong>RAG BASED CHATBOT</strong></span> <br> for <br>
<img src="https://empirecollege.in/wp-content/uploads/2024/10/logo.svg" width="150" height="30"/>
</div>

---

A RAG chatbot that helps college website visitors to get accurate, context-aware answers by combining retrieval-based search with generative AI.


### Do

scrap the data before start
```bash
make scrap  # to scrap data.
```

then,
```bash
make index  # add the retrived data into vector store.
```

And now run the FastAPI app.
```bash
make run
```


### License
[MIT](LICENSE) 
