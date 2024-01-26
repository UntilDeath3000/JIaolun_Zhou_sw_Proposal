# Literature
## Literature_Review
#### Title:Anatomy of a Large-Scale Hypertextual Web Search Engine(Lawrence, 1998) - Keyword Matching Based Retrieval Model
- Background/Motivation:
The paper provides an overview of the challenges associated with building large-scale search engines, including the need to efficiently crawl and index massive amounts of data while producing high-quality search results. The authors note that despite the importance of these systems, relatively little academic research has been conducted on them.
- Research Question:
The primary research question addressed in the paper is how to build a practical large-scale search engine that can effectively utilize the structure present in hypertext to produce better search results. The authors propose a method for addressing this question by leveraging both link structure and anchor text.
- Application Scenarios:
The paper focuses primarily on the development of a search engine prototype called Google, which was designed to crawl and index the web efficiently and produce more satisfactory search results than existing systems. The authors discuss various aspects of the system, including its architecture, algorithms, and data structures.
- Methodology:
The authors describe their approach to developing the Google search engine prototype, which involves leveraging the structure present in hypertext to improve search quality. They also discuss various technical challenges associated with scaling traditional search techniques to the level required for a large-scale system.
- Results:
The paper provides an in-depth description of the Google search engine prototype, including its architecture, algorithms, and data structures. The authors demonstrate that the system is capable of efficiently crawling and indexing massive amounts of data while producing high-quality search results.
- Intellectual Merits/Practical Impacts:
The paper represents an important contribution to the field of search engine development, particularly in terms of its focus on leveraging the structure present in hypertext to improve search quality. The authors' approach has significant practical implications for organizations seeking to develop large-scale search engines, and their work has helped to push the field forward in terms of understanding and advancing search engine technology. Additionally, the authors' emphasis on open-source development and collaboration has helped to promote transparency and accountability in the field.
#### Title:Distributed Representations of Words and Phrases and their Compositionality(Tomas, 2013) - Semantic Similarity Based Retrieval Model 
- Background/Motivation:
The paper presents an extension of the continuous Skip-gram model, which is an efficient method for learning high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships. The authors aim to improve both the quality of the vectors and the training speed through several extensions, including subsampling of frequent words, negative sampling, and finding phrases in text.
- Research Question:
The research question addressed in the paper is how to improve the quality of the vector representations obtained through the continuous Skip-gram model, as well as the training speed. The authors propose several extensions to address this question, including subsampling of frequent words, negative sampling, and finding phrases in text.
- Application Scenarios:
The proposed extensions to the continuous Skip-gram model can be applied in natural language processing tasks such as information retrieval, machine translation, sentiment analysis, and speech recognition. High-quality distributed vector representations can capture a large number of precise syntactic and semantic word relationships, making them useful for these tasks.
- Methodology:
The authors propose several extensions to the continuous Skip-gram model, including subsampling of frequent words, negative sampling, and finding phrases in text. Subsampling of frequent words involves discarding words that occur too frequently in the training data, which results in faster training and more regular word representations. Negative sampling is a simple alternative to the hierarchical softmax, which allows for faster training without sacrificing the quality of the vector representations. Finding phrases in text involves identifying words that appear frequently together and infrequently in other contexts, allowing for the learning of vector representations for phrases.
- Result:
The authors report improved performance on the analogical reasoning task when using negative sampling compared to the hierarchical softmax and noise contrastive estimation. They also demonstrate that subsampling of frequent words significantly improves training speed and makes the word representations more accurate. Additionally, they show that learning good vector representations for millions of phrases is possible through the identification of phrases in text.
- Intellectual Merits/Practical Impacts:
The proposed extensions to the continuous Skip-gram model have significant intellectual merit as they improve the quality of the vector representations obtained through the model, as well as the training speed. These improvements make the model more practical for real-world applications in natural language processing. The ability to learn high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships can lead to improved performance in tasks such as information retrieval, machine translation, sentiment analysis, and speech recognition. Overall, the proposed extensions have the potential to advance the field of natural language processing and improve the performance of downstream applications.
## Research Idea: Comparing the Accuracy and Efficiency of Keyword Matching Based Retrieval Model and Semantic Similarity Based Retrieval Model by Building Intellectual Question Answering Models
- Background/Motivation:
The popular language models in the market today are mainly based on Keyword Matching Based Retrieval Model and Semantic Similarity Based Retrieval Model.However, the keyword retrieval model is less accurate than Semantic Similarity Based Retrieval Model and Semantic Similarity Based Retrieval Model requires more data than Keyword Retrieval Model. This difference determines that training an accurate language model with a limited dataset has different possibilities in different approaches. The aim of this paper is to compare the accuracy and efficiency of intelligent Q&A models trained by these two different approaches with prioritized datasets.
- Research Question:
Build an intelligent Q&A model based on prioritized dataset. Compare the different accuracy and efficiency of Keyword Retrieval Model and Semantic Similarity Based Retrieval Model in training intelligent Q&A models.
- Application Scenarios:
The proposed intelligent question answering system can be applied in various scenarios such as online customer service, educational platforms, and healthcare services. It can help users quickly find the information they need and improve their overall user experience.
- Methodology:
Propose a simple yet effective approach to building an intelligent question answering system based on keyword matching. Specifically, build a question-answer database by collecting relevant documents and manually labeling them with keywords. Then, use these keywords to match users' questions with the corresponding answers in the database. To evaluate the effectiveness of the approach, we will conduct experiments on several benchmark datasets and compare its performance with other state-of-the-art methods.
- Results:
The experimental results show that this approach achieves comparable accuracy to more complex machine learning-based approaches while being much simpler and easier to implement. Moreover, the approach is highly scalable and can handle large volumes of data efficiently.
- Intellectual Merits/Practical Impacts:
This work contributes to the development of intelligent question answering systems that are accessible to non-experts and can be easily deployed in real-world applications. By reducing the reliance on complex machine learning algorithms and large-scale datasets, the approach can significantly reduce the cost and complexity of building and maintaining intelligent question answering systems. This can lead to wider adoption of these systems and improved user experiences across various domains.

- Flow chart

<img src="Research idea.png" alt="Flow chart">

Source:Whimsical

```
@article{hong2021xgboost,
  title={XGBoost-based prediction modelling and analysis for health literacy assessment},
  author={Hong, Yan and Zhang, Xiaoda and Chen, Jinxiang},
  journal={International Journal of Modelling, Identification and Control},
  volume={39},
  number={3},
  pages={229--235},
  year={2021},
  publisher={Inderscience Publishers (IEL)}
}
@article{davagdorj2020xgboost,
  title={XGBoost-based framework for smoking-induced noncommunicable disease prediction},
  author={Davagdorj, Khishigsuren and Pham, Van Huy and Theera-Umpon, Nipon and Ryu, Keun Ho},
  journal={International journal of environmental research and public health},
  volume={17},
  number={18},
  pages={6513},
  year={2020},
  publisher={MDPI}
}
```
