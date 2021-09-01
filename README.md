# Twitter-Project
This project focuses on analysing the PubMed data in terms of usage of twitter by biomedical researchers. The github repository contains the links to the datasets 
and the code that was used for our study : ["Unlocking the microblogging potential for science and medicine"](). The repository is under development. 

**Table of contents**

* [How to cite this study](#how-to-cite-this-study)
* [Reproducing results](#reproducing-results)
  * [Modules](#modules)
  * [Data](#data)
  * [Detour scripts](#scripts)
  * [Notebooks for Analysis](#notebooks-and-figures)
* [License](#license)
* [Contact](#contact)


# How to cite this study

> Have to add.


# Reproducing results

## Modules

We have evaluated the PubMed data which contains around 4.25 million scientists collected from 11.61 million papers which were published between 2000 and 2020. We have worked upon 167,000 scientists. Python modules 
used for analysing data are Tweepy, Beautiful Soup 4 and MetaPub. 

## Data

Data we used for our study is PubMed data which contains basic information about the scientists like their first name, last name and journal name. Data can be found at this [link](https://github.com/smangul1/data_reusability). Then we extracted Twitter data using Tweepy and their essential information like citations, K-index etc. using Scholarly module. Following data can be found at : 

1. Final processed data (kdf.csv) -- [link](https://github.com/Mangul-Lab-USC/Twitter-editorial)
2. Data used for converting PMCID to pubmed ID (data4scrap.csv) -- [link](https://drive.google.com/file/d/1IPRxbGCvZH3eaYuJ6iyw8fUwdN6x6fu1/view?usp=sharing)
3. Data used for scrapping (data4origscrap.csv) -- [link](https://drive.google.com/file/d/1pik_kEL2N7qdVz8E28gexRbFTkBQI2-v/view?usp=sharing)
4. Pubmed IDs list (citations.txt) -- [link](https://github.com/Mangul-Lab-USC/Twitter-editorial)

## Detour scripts

Detour scripts are used to prepare certain datasets used in the main analysis and are present in the repository. 

* [Processing Raw Data](https://github.com/Mangul-Lab-USC/Twitter-editorial)
* [Converting PMCID to PubmedID](https://github.com/Mangul-Lab-USC/Twitter-editorial)
* [Getting Citation Count](https://github.com/Mangul-Lab-USC/Twitter-editorial)

## Notebooks

We have prepared Jupyter Notebooks that utilize the data described above to reproduce the results presented in our manuscript.

* [Preparing Data for scrapping](https://github.com/Mangul-Lab-USC/Twitter-editorial)
* [Getting Twitter Data](https://github.com/Mangul-Lab-USC/Twitter-editorial)
* [Data Preparation and Analysis](https://github.com/Mangul-Lab-USC/Twitter-editorial)


# License

This repository is under MIT license. For more information, please read our [LICENSE.md](LICENSE) file.


# Contact

Please do not hesitate to contact us (mangul@usc.edu) if you have any comments, suggestions, or clarification requests regarding the study or if you would like to contribute to this resource.