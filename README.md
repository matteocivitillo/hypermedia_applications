# 🌿 Yoga Center Web Project – HYP 2024-2025

**Course**: Hypermedia Applications – Web & Multimedia  
**Professor**: Franca Garzotto  
**Team**: [Insert team member names]  
**Exam Session**: June–July  
**Figma Prototype**: [Insert Figma link]  
**Live Demo**: [https://hypermedia-applications-rho.vercel.app/](https://hypermedia-applications-rho.vercel.app/)  
**Repository**: [GitHub](https://github.com/yexin01/hypermedia_applications)

---

## Project Overview

This project is a complete design and development of a website for a Yoga Center. The goal is to promote the center, introduce the teaching staff, and provide information about various activities (classes, retreats, workshops, etc.). The project follows the methodological design approach taught in the HYP course, covering content, navigation, and presentation design with a clear separation of concerns.

---

## Information Architecture (C-IDM Schema)

The content structure is based on the **Content-Interactive Dialogue Model (C-IDM)**:

- **Topic**: The Yoga Center
- **Kinds of Topics**:
  - `Teacher`: Includes image, short bio, and areas of expertise (min. 5 instances)
  - `Activity Type`: Includes title, images, description, and schedule info (min. 8 types)
- **Relevant Relationships**:
  - A teacher teaches or is responsible for one or more activities
  - An activity can be taught by one or more teachers
- **Groups**:
  - All Teachers
  - All Activities
  - Highlights (3–4 selected activities the center promotes)

---

## Navigation Design

The website includes multiple types of abstract pages:

- **Single Topic Page**: Detailed view of the Yoga Center
- **Multiple Topic Pages**: Lists of teachers and activity types
- **Introductory Group Pages**: Overview and previews for each group
- **Transition Pages**: Navigate between semantically related topics
- **Home Page**: Entry point with overview and highlights

**Types of Links** implemented:

- Structural Links  
- Transition Links  
- Group Links  
- Landmarks (site-wide navigation)

Navigation patterns used: **Index**, **Guided Tour**, and **All-to-All**, as appropriate.

---

## Presentation Design

- **Low-Fidelity Wireframes**: For each abstract page (not included in the final report)
- **High-Fidelity Wireframes**: Created in Figma, consistent with abstract pages and C-IDM
- **Mock-up Prototype**: Figma prototype simulating 2–3 realistic user interaction scenarios

---

## Technologies Used

- **Frontend**:
  - HTML + CSS
  - JavaScript (ES6+)
  - Vue.js 3 (composition API, components, props/emits)
  - Nuxt (pages, dynamic routing, layouts, SEO integration)
- **Backend (optional)**:
  - Node.js + Express.js (REST APIs)
  - JSON for content structuring
  - E-R diagram included in the design report

---

## SEO & Accessibility

- Metadata defined using Nuxt’s `useHead()` or `useSeoMeta()`
- Semantic HTML and ARIA roles
- Fully responsive design
- Descriptive alt text for images
- Accessible contrast and clear visual hierarchy

---

## Getting Started Locally

To run the project on your local machine:

### 1. Clone the repository:
```bash
git clone https://github.com/yexin01/hypermedia_applications
cd hypermedia_applications