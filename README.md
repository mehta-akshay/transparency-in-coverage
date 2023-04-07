# Transparency-in-coverage
Transparency in Coverage analysis for insurance providers and for patients

## Installation

* Fork or Clone this repo

### What you need
* Python
* JupyterLab or Databricks runtime

## Run
### Python
* You need to ensure the file path's are correct per your files
** The MRF files were downloaded from below sources - 
*** [Health Partners Data](https://www.healthpartners.com/hp/legal-notices/disclosures/transparency/index.html#collapsesection-1)
*** [Wellmark](https://web.healthsparq.com/app/public/#/one/insurerCode=WMRK_I&brandCode=WELLMARK&productCode=MRF/machine-readable-transparency-in-coverage)
*** [UHC](https://transparency-in-coverage.uhc.com/)

#### Run data processing through Jupyter lab or Databricks
* Run python. -> `jupyter ia_health_plans_analysis.ipynb`

#### Run Streamlit app
* Run Web interface app. -> 
```
  cd Transparency_Dashboard 
  unzip Final Dataset Cleaned.csv.zip
  streamline run app.py
```
