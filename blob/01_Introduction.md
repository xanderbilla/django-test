# Introduction

The web framework for perfectionists with deadlines.

- Build feature is fast
- Security built-in
- Scales in size well
- Built in pyhton

It is for backend. A full framework written in pyhton.
Other Alternative frameworks are -

For simpler/single page websites, consider [Flask](https://flask.com)

## Features

- Security
- Admin Panel
- Sessions 
- User Management

## History

- Started in 2003 by Adrian Holovaty and Simon Willison (and later, Jacob Kaplan Moss) at a newspaper company in Kansas
- Released as open-source in 2005, and named after the jazz guitarist, Django Reinhardt
- Built to create things fast, under deadlines, with many non-developers, like content creators
- Read more at [Django Design Patterns — The Story of Django](https://www.oreilly.com/library/view/django-design-patterns/9781788831345/dae3e1e9-e244-4dc6-b9d9-ab7a98b91a1a.xhtml)

## Architecture

Uses an MVT pattern:

- **Models** — Interact with the database via an ORM
- **Views** — Handle HTTP requests and return responses
- **Templates** — Create dynamic HTML pages from Python data

![Architecture Image]()

1. User sends an HTTP **request** to Django
2. **URL conf**iguration, contained in `urls.py`, selects a View to handle the request
3. The **View** gets the request and
    - Talks to a database via the **Models**
    - Renders an HTML **Template**
User
4. The View returns an **HttpResponse**
which gets sent to the client to be
rendered as a web page in the browser

```
DJango
    ├───App1
    ├───App2
    ├───...
    ├───AppX
    └───DJango Apps
```

## Resources

- [Official Django site](https://djangoproject.com)
- [Documentation](https://docs.djangoproject.com)
- [Official tutorial](https://djangoproject.com/en/4.2/intro)

## Why create a virtual environment?

- You may have multiple Python versions on your computer
- You may have projects that require different versions of the same external package
- Virtual environments create a "workspace" environment for a specific project
- All installed apps are in one place, without conflicts
- The "python" and "pip" commands point to the same place
- Keeps your environment clean