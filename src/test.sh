curl "https://nul-staff-openai.openai.azure.com/openai/deployments/nul-general-gpt35/chat/completions?api-version=2023-07-01-preview" \



  -H "Content-Type: application/json" \



  -H "api-key: 1a9ba1bf673c45a1adf8fc1118cae181" \



  -d "{



  \"messages\": [{\"role\":\"system\",\"content\":\"Assistant is an AI chatbot that helps users turn any citation into the biblatex format. The user puts in a citation and gets back well-formed biblatex for use in latex documents.\"},{\"role\":\"user\",\"content\":\"The Canadian Press. (2018, October 7). *CAMH reaches settlement with former head of gender identity clinic*. CBC. Retrieved November 18, 2022, from https://www.cbc.ca/news/canada/toronto/camh-settlement-former-head-gender-identity-clinic-1.4854015.\"},{\"role\":\"assistant\",\"content\":\"@online{canadianpress2018,\n  author = {The Canadian Press},\n  title = {{CAMH reaches settlement with former head of gender identity clinic}},\n  year = {2018},\n  month = {October 7},\n  url = {https://www.cbc.ca/news/canada/toronto/camh-settlement-former-head-gender-identity-clinic-1.4854015},\n  organization = {CBC},\n  urldate = {2022-11-18}\n}\"}],



  \"max_tokens\": 350,



  \"temperature\": 0.2,



  \"frequency_penalty\": 0,



  \"presence_penalty\": 0,



  \"top_p\": 0.95,



  \"stop\": null



}"