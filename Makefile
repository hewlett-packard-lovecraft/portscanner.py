init:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf port_scanner/__pycache__
	rm -rf port_scanner/scanner/__pycache__

run:
	python app.py
