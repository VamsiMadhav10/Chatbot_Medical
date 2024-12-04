# Glauco-Bot

Glauco-Bot is an interactive chatbot that provides users with information about glaucoma. This project is hosted on the web using Streamlit, and it retrieves answers from a pre-defined knowledge base using Dense Passage Retrieval (DPR) with the Llama 3.2-1B-Instruct model.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.x
- pip (Python's package installer)

## Installation and Setup

### 1. Install Dependencies

First, you need to install the required Python libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies from the `requirements.txt` file.


### 2. Running the Application

Once the dependencies are installed, you can launch the chatbot by running the following command:

```bash
streamlit run ui.py
```

This will start a local web server, and the chatbot interface will be available in your browser.

### 3. Interacting with the Chatbot

After the Streamlit app is running, open your browser and you will be able to interact with the chatbot directly. Type in queries related to glaucoma, and the chatbot will provide relevant responses based on the knowledge base.

## How it Works

- The chatbot uses seven unique JSON files containing information on glaucoma:
  - **name**: General information about glaucoma
  - **symptoms**: Symptoms of different types of glaucoma
  - **tips**: Tips for living with glaucoma
  - **diagnosis**: Information on diagnosis methods
  - **risk_factor**: Risk factors for developing glaucoma
  - **medications**: Medications for glaucoma, including details and side effects
  - **treatment**: Different treatment options
  - **types**: Types of glaucoma and their descriptions

- The chatbot retrieves relevant information by performing a similarity search using **Vector Indexing Retrieval** (a form of **Dense Passage Retrieval**).
- The retrieved knowledge is then processed by the `Llama 3.2-1B-Instruct` model to generate a response.

## Screenshots

Screenshots of the chatbot interface can be found in the provided zip folder.


Follow these steps to quickly get Glauco-Bot up and running, and start interacting with the chatbot to explore information about Glaucoma!