<a id="readme-top"></a>

<!-- Shields
LinkedIn
Portfolio
Github
 -->

<br>
<div align="center">
   <!-- TODO -->
   <a href="https://altura-solutions.duckdns.org"><img src="docs/altura-solutions-logo-transparent.png" alt="logo" width="auto" height="80"></a>

   <h3 align="center">Altura Solutions</h3>

   <p align="center">
      Altura Solutions is a fictional <strong>web development agency portal</strong> built with <strong>Django + Wagtail</strong>.  
      It serves as a showcase website for a client-focused company specializing in professional web solutions, including a homepage, service listings, about us, contact page, and future payment integration.
   </p>
</div>

<!-- TABLE OF CONTETS -->
 <details>
   <summary>Table of Contents</summary>
   <ol>
      <li>
         <a href="#demo">Demo</a>
      </li>
      <li>
         <a href="#about-the-project">About the Project</a>
         <ul>
            <li><a href="#built-with">Built With</a></li>
         </ul>
      </li>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#features-implemented">Features Implemented</a></li>
      <li><a href="#roadmap">Roadmap</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#license">License</a></li>
   </ol>
 </details>

<!-- DEMO -->

## Demo

🔗 [Live Demo](https://altura-solutions.duckdns.org)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ABOUT -->

## About The Project

[![Focus Board Screenshot][homepage-banner]](https://altura-solutions.duckdns.org)

### Built With

- [![Python][Python-badge]][Python-url]
- [![Django][Django-badge]][Django-url]
- [![Wagtail][Wagtail-badge]][Wagtail-url]
- [![Stripe][Stripe-badge]][Stripe-url]
- [![DigitalOcean][DigitalOcean-badge]][DigitalOcean-url]
- [![PostgreSQL][Postgres-badge]][Postgres-url]
- [![Bootstrap][Bootstrap-badge]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

1. Clone repo

```sh
git clone git@gitlab.com:javier.beltran.hmo/altura-solutions.git
cd altura-solutions
```

2. Create Virtual Enviroment

```sh
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

```

3. Install Depenencies

```sh
pip install -r requirements.txt

```

4. Setup Database

```sh
python manage.py migrate
python manage.py createsuperuser
```

5. Start Server

```sh
python manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features Implemented

### 🏠 Homepage

- Hero banner with lead text and a call-to-action button.
- Customizable banner with image overlay and text content.
- Responsive layout built with Bootstrap 5.

### 💼 Services

- Wagtail models:
  - `ServiceListingPage` for displaying all services dynamically.
  - `ServicePage` for detailed descriptions of individual services.
- Professional service offerings:
  1. **Bug Fix & Code Optimization** – Fix errors and optimize code for better performance.
  2. **Feature Integration & System Expansion** – Add CRUD features, APIs, or payment systems.
  3. **MVP Design & Development** – Build market-ready Minimum Viable Products.

### 🏢 Company Information

- **About Us** page with company history, mission, and team members.
- **Testimonials** section showcasing client feedback.

### 🏢 Contact & Interaction

- Functional **Contact Page** with email form.
- **Service Listing Page** with dynamic service cards powered by Wagtail.

### 💳 Payments

- **Stripe integration** for secure online service purchases.

### Screenshots

1. **Home Banner**:

   ![Home Banner][homepage-banner]

2. **Projects Section in Home**

   ![Home Proyects Example][homepageproyects]

3. **Service Listing**:

   ![Service Listing Page][servicelisting]

4. **Stripe Integration**:

   ![Checkout][stripe]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

### Summary Checklist

| Feature                          | Status     |
| -------------------------------- | ---------- |
| Homepage with Hero Banner        | ✔️ Done    |
| Customizable Banner (Image/Text) | ✔️ Done    |
| Service Models in Wagtail        | ✔️ Done    |
| Professional Service Offerings   | ✔️ Done    |
| About Us Page                    | ✔️ Done    |
| Contact Page with Email Form     | ✔️ Done    |
| Testimonials Section             | ✔️ Done    |
| Dynamic Service Listing Page     | ✔️ Done    |
| Stripe Integration               | ✔️ Done    |
| Blog/Insights section            | ⬜ Planned |
| SEO optimization                 | ⬜ Planned |
| Responsive improvements          | ⬜ Planned |
| Custom error pages               | ⬜ Planned |

- [ ] **Blog/Insights section** for articles and case studies.
- [ ] **SEO optimization** for all pages.
- [ ] **Responsive improvements** for mobile and tablet.
- [ ] **Custom error pages** (404, 500).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Javier Beltran - [LinkedIn](https://www.linkedin.com/in/javier-alejandro-beltran-montiel-3172222b1/)

Project Link: [https://gitlab.com/javier.beltran.hmo/altura-solutions](https://gitlab.com/javier.beltran.hmo/altura-solutions)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the Unlicense License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Links and images -->

[//]: # "Badge links"
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Wagtail-badge]: https://img.shields.io/badge/Wagtail-43B1B0?style=for-the-badge&logo=wagtail&logoColor=white
[Wagtail-url]: https://wagtail.org/
[Stripe-badge]: https://img.shields.io/badge/Stripe-008CDD?style=for-the-badge&logo=stripe&logoColor=white
[Stripe-url]: https://stripe.com/
[DigitalOcean-badge]: https://img.shields.io/badge/DigitalOcean-0080FF?style=for-the-badge&logo=digitalocean&logoColor=white
[DigitalOcean-url]: https://www.digitalocean.com/
[Postgres-badge]: https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Bootstrap-badge]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[//]: # "Images"
[homepage-banner]: docs/screenshots/homepage-banner.png
[homepageproyects]: docs/screenshots/homepageproyects.png
[servicelisting]: docs/screenshots/servicelisting.png
[stripe]: docs/screenshots/stripe.png
