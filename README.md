# Cheatsheet for Internal Government Websites

To get this started:
`docker build -t shortcut . && docker run -p 8080:8080 shortcut`

To add an entry:

- Populate entries in temp_db.csv
- Do a `pip install -r requirements.txt` to install dependencies
- Run the converter `python generate_list_json.py` so that the csv file gets converted to js/masterArr.js
- Add and commit it to git
- Bug Nikhil to deploy it on Nectar
