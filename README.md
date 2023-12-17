# INSCRIPTIONS OF LEPCIS MAGNA

## A Python-based web application, built using the Django framework, intended for use by scholars and enthusiasts to research the inscriptions of Lepcis Magna via a user-friendly, research-forward platform.

### Demo: [Watch Demo Video] (XXXX)

**Features:**

- The application can be used to:

    - Register individual users for collaboration
    - Store epigraphic data provided by admins or registered users in SQL database for recall by users
    - Search for inscriptions by location, content, and other identifying data
    - Compile epigraphic dossiers for registered users to use in research

**How to Run:**

1. **Installation:**

   	- Python v.3.11.4 [Download Python] (https://www.python.org/downloads/release/python-3114/) 
    - Django v.4.2.7 [Download Django] (https://www.djangoproject.com/download/)

2. **Set up a virtual environment:**

   	- In the terminal, enter the command `python3 -m venv env`
   	- If using Unix/macOS, enter `source env/bin/activate`
   	- If using Windows, enter `.\env\Scripts\activate`

3. **Run the app:**

    - To start the Django server, enter `python3 manage.py runserver` in the terminal and click the link provided.

**Usage Guide:**

1. **Welcome Page**

    - The first page you encounter will be the Welcome page, which contains a navbar and 'Quick Start Guide' with links to elements accessible to non-registered users, including the full list of inscriptions, search, category and bibliography lists, and the epigraphic indices. 
    - The page header prompts the user to Login or Register to gain full access, which includes the ability to Create an Entry and compile a unique user Dossier.

2. **Login/Register**

    - Clicking the Login link in the navbar or in the Welcome Page header will bring the user to the Login page, which contains a login form and button labeled ‘Login’, as well as a ‘Register here’ link leading to the Register page. ‘Login’ and ‘Register’ links are also found on the right side of the navbar at the top of the page.
    - If visiting for the first time, click the ‘Register here’ link below the login form or the ‘Register’ link in the navbar, which will take the user to the Register page. Upon filling out and successfully submitting the registration form, the user will be logged in automatically.
   	- If already registered, the user should fill out the login form and click the ‘Login’ button.
    - Registration is required for users to access the ‘Create Entry’ and 'Dossier’ functionalities.

3. **User Home**

    - Upon login, the user are directed to the User Home page, which is virtually identical to the Welcome Page, but with access to the 'Create Entry' and 'Dossier' functionalities now available.
    - As seen in the Quick Start Guide and in navbar at the top of the User Home page, there are links to the ‘Create Entry’ and 'Dossier’ pages, as well as a ‘Logout’ link on the right side of the navbar.

4. **Inscriptions**

    - Both registered and non-registered users can access the ‘Inscriptions’ page, which displays basic information for every inscription in the database in a user-friendly card format.
    - Users can click the inscription card, which will take them to the ‘Inscription Detail’ page for that inscription, which includes the following data:
        - ID number
       	- descriptive title
       	- description of the physical inscription (size, material, etc.)
       	- description of the text of the inscription (e.g., size and character of the inscription field)
       	- description of the character and size of the letters
       	- date
       	- findspot (as specific as possible)
       	- original location (if known)
       	- last recorded location
       	- interpretive transcription
       	- diplomatic transcription
		- apparatus criticus for transcriptions
       	- English translation (with future plans for multi-lingual translations)
       	- commentary
       	- bibliography of epigraphic references and secondary sources
       	- images
    - If registered and logged in, the user will be able to add the inscription to their personal epigraphic dossier if not already part of it, and remove it if it is. The user can access their dossier using the 'Dossier’ link in the navbar.

5. **Search**

    - Both registered and non-registered users can access the 'Search' page, which contains a search form in the left-hand column that facilitates query search using keyword terms or filters, including Findspot, Repository, Material, Technique, Object Type, Category, and Language.
    - The results are displayed in the right-hand column in a manner similar to the 'Inscriptions' page.

6. **Categories**

    - Both registered and non-registered users can access the ‘Categories’ page, which displays a list of categories (e.g., honorific, building, funerary, etc.).
   	- Clicking on a category will bring you to a list of inscriptions belonging to that category.

7. **Bibliography**

    - Both registered and non-registered users can access the ‘Bibliography’ page, which displays the bibliography of secondary sources and epigraphic references relevant to the inscriptions included in the database.

8. **Indices**

    - Both registered and non-registered users can access the ‘Indices’ menu containing a series of pages that display indexed lists of epigraphic data relevant to particular inscriptions, including abbreviations, age at death, divine and sacred beings, emperors and imperial family, erasures, findspots, fragments, organizations, people, personal names, place names, symbols, words.
    - The choice of indices is modeled after the Inscriptions of Roman Tripolitania 2021 project (https://irt2021.inslib.kcl.ac.uk/en/)

9. **Create Entry**

    - Registered users can access the ‘Create Entry’ page, which displays a form for the creation and processing of new epigraphic entries, allowing for collaborative data input.
    - NB: If an inscription is added via this form, and not via admin access to the database, the inscription will not be displayed until validated by an admin user.

10. **Dossier**

    - Registered users can access a personal 'Dossier’ page, which displays a list of inscriptions they have added to (and have not subsequently removed from) their own dossier.
   	- This page functions similarly to the ‘Inscriptions’ page with content curated by the specific user.

**Dependencies:**

- Django

**Database Schema:**

- The Django models utilized by this application are found in 'lepcismagna/models.py'.

**Technologies Used:**

- Frontend built using HTML, CSS, and JavaScript, with style enhancements using Bootstrap.
- Backend built using Python and Django, working with a SQLite3 database using Django models.

**License:**

- GPL-3.0

**Future Improvements:**

- Data encryption to protect user identity.
- Integration of comment/suggestion functionality to encourage more robust collaboration.
- Implementation of user profile system so users can communicate and can keep track of user contributions.
- Continue improving the search functionality, including the implementation of search/filter by date (which will require altering the Inscription model to include numerical start/end dates).
- Incorporate multi-lingual translations for international utility.
- Complete data entry for inscriptions from Lepcis Magna.
- Expand database to include inscriptions from across North Africa.
- Long-term goal: Integrate an AI/LLM inscription assistant who can offer suggestions for supplementing fragmentary inscriptions based on the expansive dataset of the Latin epigraphic corpus.

**Credits:**

Thanks to:

- The IRT 2021 project for inspiring the creation of this project and for providing the dataset necessary for the initial build.
- Adrian Stähli, Emma Dench, and Paul Kosmin, who shepherded the dissertation project that birthed the idea to create this database.
- David Malan, Brian Yu, and the Harvard cs50 crew for the knowledge foundations that facilitated this project.