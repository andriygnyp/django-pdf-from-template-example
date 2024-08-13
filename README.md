# Root cause or Original request

Someone asked me: "make an endpoint which receives JSON and generates PDF from template"

# Installation

All the examples are workable on linux and, I uppose, MacOS.

Create python virtual environment:

```bash
$ virtualenv -p python3 .venv
```

Activate it and install necessary libs:

```bash
$ . .env/bin/activate
$ pip install -r requirements.txt
```

# Usage

Activate virtual environment:
```bash
$ . .env/bin/activate
```

Change directory to `tmpl2pdf` and launch web UI:

```bash
$ cd tmpl2pdf
$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

...
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Index page is as simple as possible. Just to show it works.
But it contains the commands which can be used to download PDF and view it:

```bash
$ curl -X POST http://127.0.0.1:8000/genpdf -d '{"name":"Your name","request":"anything you want to write"}' -o ex.pdf
$ evince ex.pdf
```
