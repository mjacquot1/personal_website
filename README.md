# [Django Soft Design](https://appseed.us/product/soft-ui-design/django/)

Open-source **Django** project crafted on top of **[Soft Design](https://appseed.us/product/soft-ui-design/django/)**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/?AFFILIATE=128200).
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 [Django Soft Design](https://appseed.us/product/soft-ui-design/django/) - `Product page`
- 👉 [Django Soft Design](https://django-soft-ui-free.appseed-srv1.com/) - `LIVE Demo`
- 🛒 **[Django Soft Design PRO](https://appseed.us/product/soft-ui-design-pro/django/)** - `Premium Version`

<br />

> Features: 

- ✅ `Up-to-date Dependencies`
- ✅ Theme: [Django Theme Soft Design](https://github.com/app-generator/django-theme-soft-design), **designed by [Creative-Tim](https://www.creative-tim.com/product/soft-ui-design-system?AFFILIATE=128200)**
- ✅ **Authentication**: `Django.contrib.AUTH`, Registration
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Soft UI Design - Full-Stack Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-soft-ui-design.git
$ cd django-soft-ui-design
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- pages                   # 
   |              |-- custom-index.html  # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize 

When a template file is loaded, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/theme_soft_design
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- sign-in.html         # Sign IN Page
   |    |    |-- sign-up.html         # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |
   |    |-- pages/       
   |         |-- index.html           # Dashboard Page
   |         |-- author.html          # Profile Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

> For instance, if we want to **customize the index.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `home` app
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `index.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/theme_soft_design/template/pages/index.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/pages/index.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom index` can be found at this location:

`home/templates/pages/custom-index.html` 

By default, this file is unused because the `theme` expects `index.html` (without the `custom-` prefix). 

In order to use it, simply rename it to `index.html`. Like this, the default version shipped in the library is ignored by Django. 

In a similar way, all other files and components can be customized easily.

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## [PRO Version](https://appseed.us/product/soft-ui-design-pro/django/)   

**Material Kit 2** is a premium design crafted by the `Creative-Tim` agency on top of Bootstrap 5 Framework. Designed for those who like bold elements and beautiful websites, Material Kit 2 is made of hundreds of elements, designed blocks, and fully coded pages built with an impressive level of quality.

- [Django Soft Design PRO](https://appseed.us/product/soft-ui-design-pro/django/) - product page
  - `Enhanced UI` - more pages and components
  - `Priority` on support

<br />  

![Soft UI Design PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png)

<br />

---
[Django Soft Design](https://appseed.us/product/soft-ui-design/django/) - **Django** Starter provided by **[AppSeed](https://appseed.us/)**