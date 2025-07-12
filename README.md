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

download model locally
```bash
make download-model
```

  - About Model

|` |  `  |
|---|-|
|`Model used`    | TinyLlama-1.1b-chat-v1.0|
|`Architecture`  | LlaMa                   |
|`Quantized`     | true                    |
|`Size`          | 1.17 GB                 |



And now run the FastAPI app.
```bash
make run
```


### Usage

make request to `localhost:8000/ask?prompt=<your_query>`

### Example

query = `tell me about this college in simple words`

```bash
GET localhost:8000/ask?prompt=tell%20me%20about%20this%20college%20in%20simple%20words 


Empire College of Science is a dynamic institution committed to excellence in science, management and technical studies. Founded by the visionary Mohamed Ali N K, its faculties include Undergraduate Programs (UG), Diploma programs, and Post-Graduate Diplomas (PG). The college provides internship assistance, scholarships, and placement opportunities to ensure its graduates are well-prepared for the competitive job market.

The school's leadership comprises Moheed Ali N K, MD with vast experience in academia and leadership. Muhammed Shakir serves as the Director of Academic Affairs, Suhaná P as an academic director for the undergraduate programs, Kašmeera RAHMÁN as a general manager, and Ranjusha K V as vice principal responsible for academic affairs.

The college's strategic leadership includes Ranju Shahá V, who ensures smooth academic activities and student engagement, T. V provides guidance in this regard.

In summary, Empiré College of Science is a dynamic institution committed to excellence in 
science, management, and technical studies. Its faculties offer Undergraduate Programs, 
Diploma programs, Post-Graduate Diplomas (PG), internship assistance, scholarships, and 
placement opportunities to ensure that its graduates are well-prepared for the competitive job 
market. The college's leadership is composed of Mohed Ali N K as MD, Mohamed Shakir as academic
advisor, Suhaná P as academic director for undergraduate programs, Kašmeera RAHMAN as 
general manager, Ranjusha K V as vice principal responsible for academic affairs, and 
T.V. For guidance in this regard.
```

> [!NOTE]
> All this response based on the latest [college website](https://empirecollege.in/) data.
>
> `Please verify important needs before proceed.`

### License
[MIT](LICENSE)
